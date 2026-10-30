#!/usr/bin/env python3
"""Compare this package with installations; query GitHub only with --upstream."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

from validate_sources import read_release_metadata


def inventory(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
        and not {".DS_Store", "__pycache__", ".git"}.intersection(path.relative_to(root).parts)
    }


def fingerprint(files: dict[str, str]) -> str:
    return hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()


def checkout_state(skill_root: Path) -> dict:
    repo = skill_root.parent.parent
    if not (repo / ".git").exists():
        return {"commit": None, "skill_dirty": None}
    commit = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    changes = subprocess.check_output(
        ["git", "-C", str(repo), "status", "--porcelain", "--untracked-files=all", "--", "skills/super-pm"],
        text=True,
    ).splitlines()
    changes = [line for line in changes if not line.endswith("/.DS_Store") and "/__pycache__/" not in line]
    return {"commit": commit, "skill_dirty": bool(changes)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compare", nargs="+", type=Path, help="Installation directories; defaults to the two standard locations")
    parser.add_argument("--upstream", action="store_true", help="Read GitHub main; never install or update")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    files = inventory(root)
    metadata = read_release_metadata(root)
    report = {
        "reference": {"path": str(root), **metadata, "files": len(files), "sha256": fingerprint(files)},
        "checkout": checkout_state(root),
        "installations": [],
    }
    destinations = args.compare or [Path.home() / ".agents/skills/super-pm", Path.home() / ".codex/skills/super-pm"]
    exit_code = 0
    for destination in destinations:
        destination = destination.expanduser().resolve()
        installed = inventory(destination) if destination.is_dir() else {}
        differences = {
            "modified": sorted(key for key in files.keys() & installed.keys() if files[key] != installed[key]),
            "missing": sorted(files.keys() - installed.keys()),
            "extra": sorted(installed.keys() - files.keys()),
        }
        matches = destination.is_dir() and not any(differences.values())
        report["installations"].append({
            "path": str(destination), "version": read_release_metadata(destination).get("version"),
            "matches_reference": matches, "sha256": fingerprint(installed) if installed else None,
            **differences,
        })
        if not matches:
            exit_code = 1
    if args.upstream:
        try:
            repository = metadata["source"].removeprefix("https://github.com/")
            request = Request(f"https://api.github.com/repos/{repository}/commits/main", headers={"User-Agent": "super-pm-version-check"})
            with urlopen(request, timeout=10) as response:
                remote_commit = json.load(response)["sha"]
            local_commit = report["checkout"]["commit"]
            same_commit = remote_commit == local_commit if local_commit else None
            status = "unknown_checkout" if same_commit is None else "local_changes" if report["checkout"]["skill_dirty"] else "same_commit" if same_commit else "different_commit"
            report["upstream"] = {
                "commit": remote_commit, "matches_checkout_commit": same_commit,
                "status": status,
                "note": "Commit equality is not content equality when the checkout is dirty; different does not establish which is newer.",
            }
            if same_commit is None:
                exit_code = 2
            elif not same_commit or report["checkout"]["skill_dirty"]:
                exit_code = 1
        except (URLError, TimeoutError, KeyError, ValueError) as error:
            report["upstream"] = {"status": "unknown", "error": str(error)}
            exit_code = 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
