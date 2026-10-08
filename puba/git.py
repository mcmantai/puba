import subprocess
import sys


def ensure_clean_repo():

    result = subprocess.check_output(["git", "status", "--porcelain"]).decode()

    if result.strip():
        print("Git working directory not clean.")
        sys.exit(1)
