#!/usr/bin/env python3
"""
Lab04 Helper: File Permissions and ACL Demonstration

Safely demonstrates:
- Creating sample files/directories
- Applying chmod and POSIX ACLs
- Verifying effective access using subprocess as another user

Note: Requires Linux with acl tools installed (setfacl/getfacl) and a test user.
Run within a disposable lab environment.
"""

import os
import subprocess
from pathlib import Path
from datetime import datetime


LAB_ROOT = Path.home() / "SPR100_Labs" / "Lab04" / "work"
TEST_USER = os.environ.get("LAB04_TEST_USER", "fsuser")


def run(cmd: str, check: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, shell=True, text=True, capture_output=True, check=check)


def ensure_setup() -> None:
    LAB_ROOT.mkdir(parents=True, exist_ok=True)
    (LAB_ROOT / "secret.txt").write_text(f"confidential {datetime.now()}\n")
    (LAB_ROOT / "notes.txt").write_text("team notes\n")

    run(f"sudo adduser {TEST_USER} --disabled-password --gecos \"\"", check=False)


def show(title: str, cmd: str) -> None:
    print(f"\n=== {title} ===")
    res = run(cmd)
    if res.stdout:
        print(res.stdout.strip())
    if res.stderr and res.returncode != 0:
        print("[stderr]", res.stderr.strip())


def main() -> None:
    print("Lab04: File Permissions and ACL Demo")
    ensure_setup()

    os.chdir(LAB_ROOT)
    show("Initial listing", "ls -la")

    # Base permissions
    show("chmod secret=600, notes=644", "chmod 600 secret.txt && chmod 644 notes.txt && ls -l")
    show("stat secret.txt", "stat secret.txt")

    # Access as other user (expect read denied before ACL)
    show(
        f"{TEST_USER} read secret (expected denied)",
        f"sudo -u {TEST_USER} bash -lc 'cat {LAB_ROOT}/secret.txt || echo denied'",
    )

    # Apply ACL read-only for test user
    show("setfacl grant r-- to test user", f"setfacl -m u:{TEST_USER}:r-- secret.txt && getfacl secret.txt")
    show(
        f"{TEST_USER} read secret (expected OK)",
        f"sudo -u {TEST_USER} bash -lc 'cat {LAB_ROOT}/secret.txt && echo OK'",
    )
    show(
        f"{TEST_USER} write secret (expected denied)",
        f"sudo -u {TEST_USER} bash -lc 'echo x >> {LAB_ROOT}/secret.txt || echo write denied'",
    )

    # Clean up ACLs
    show("remove ACL from secret", "setfacl -b secret.txt && getfacl secret.txt")

    print("\nDemo complete. Review outputs above for analysis.")


if __name__ == "__main__":
    main()


