import sys
from .pipeline import release, run_checks_only
from .secrets import store_token

HELP_TEXT = """
puba - Safe Python package release tool

Commands:
  auth       Store PyPI token securely
  checks     Run safety checks only (git, secrets, tests)
  publish    Build and upload your package safely
             Options:
               --test   Upload to TestPyPI
               --dry    Run checks and build without uploading
  help       Show this help message
"""


def main():
    if len(sys.argv) < 2:
        print(HELP_TEXT)
        sys.exit(0)

    cmd = sys.argv[1].lower()
    options = sys.argv[2:]

    if cmd == "auth":
        store_token()

    elif cmd == "checks":
        run_checks_only()

    elif cmd == "publish":
        test = "--test" in options
        dry = "--dry" in options
        release(test=test, dry=dry)

    elif cmd == "help":
        print(HELP_TEXT)

    else:
        print(f"Unknown command: {cmd}\n")
        print(HELP_TEXT)
        sys.exit(1)


if __name__ == "__main__":
    main()
