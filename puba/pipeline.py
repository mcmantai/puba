from .git import ensure_clean_repo
from .checks import run_secret_scan, run_tests, check_installs
from .build import build_package, upload_package
from .secrets import get_pypi_token


def release(test=False, dry=False):
    print(f"Checking installs...")
    check_installs()

    print("Checking git state...")
    ensure_clean_repo()

    print("Scanning for secrets...")
    run_secret_scan()

    print("Running tests...")
    run_tests()

    print("Building package...")
    build_package()

    if dry:
        print("Dry run complete")
        return

    token = get_pypi_token()

    print("Uploading package...")
    upload_package(token, test)

    print("Release complete")


def run_checks_only():
    """
    Run safety checks without uploading package.
    Useful for CI or pre-release verification.
    """
    print(f"Checking installs...")
    check_installs()

    print("Checking git state...")
    ensure_clean_repo()

    print("Scanning for secrets...")
    run_secret_scan()

    print("Running tests...")
    run_tests()

    print("Building package...")
    build_package()

    print("All checks passed. Package is ready for release.")
