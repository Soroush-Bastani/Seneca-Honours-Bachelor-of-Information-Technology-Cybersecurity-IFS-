#!/usr/bin/env python3
"""
Lab04 Helper: File System Inspection

Inspects:
- Ownership, mode, and timestamps (stat)
- Presence of extended attributes (if supported)
- Optional: print getfacl output when available
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime


def run(cmd: str):
    return subprocess.run(cmd, shell=True, text=True, capture_output=True)


def inspect_path(target: Path) -> None:
    print(f"\n=== Inspecting: {target} ===")
    if not target.exists():
        print("Path does not exist")
        return

    # Basic ls/stat
    ls = run(f"ls -ld {target}")
    print(ls.stdout.strip() or ls.stderr.strip())

    st = run(f"stat {target}")
    print(st.stdout.strip() or st.stderr.strip())

    # ACL (if available)
    facl = run(f"getfacl -p {target}")
    if facl.returncode == 0 and facl.stdout:
        print("\n-- getfacl --")
        print(facl.stdout.strip())
    else:
        print("\n(getfacl not available or no ACL entries)")

    # xattrs (if available)
    lsx = run(f"getfattr -d {target}")
    if lsx.returncode == 0 and lsx.stdout:
        print("\n-- xattrs --")
        print(lsx.stdout.strip())
    else:
        print("\n(no extended attributes or getfattr not available)")


def main() -> None:
    paths = [Path(p) for p in sys.argv[1:]] or [Path.cwd()]
    print(f"FS Inspect started at {datetime.now()}\n")
    for p in paths:
        inspect_path(p)


if __name__ == "__main__":
    main()


