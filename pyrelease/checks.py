import subprocess
import importlib.util
import sys

DEV_DEPS = ["build", "twine"]


def check_installs():
    missing = []

    for tool in DEV_DEPS:
        if importlib.util.find_spec(tool) is None:
            missing.append(tool)

    if not missing:
        return

    print(f"⚠️ Missing required tools: {', '.join(missing)}")

    response = input("Install them now? [y/N]: ").strip().lower()

    if response != "y":
        print("Install manually with: pip install build twine")
        sys.exit(1)

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
        print("✅ Dev tools installed.")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dev tools.")
        sys.exit(1)


def run_secret_scan():

    try:
        subprocess.run(["gitleaks", "detect", "--no-git"], check=True)
    except FileNotFoundError:
        print("gitleaks not installed — skipping secret scan")


import subprocess


def run_secret_scan():
    try:
        subprocess.run(["gitleaks", "detect", "--no-git"], check=True)
    except FileNotFoundError:
        print("gitleaks not installed — skipping secret scan")


def run_tests():
    """Run pytest if available. Skip if no tests are found."""
    try:
        result = subprocess.run(["pytest"], capture_output=True, text=True)
        if result.returncode == 5:
            print("No tests found — skipping test step.")
        elif result.returncode != 0:
            raise RuntimeError(f"Tests failed with exit code {result.returncode}")
        else:
            print("Tests passed successfully.")
    except FileNotFoundError:
        print("pytest not installed — skipping tests.")
