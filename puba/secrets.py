import os
import keyring
import getpass
import platform

SERVICE = "puba"


def get_pypi_token():
    """
    Retrieve the PyPI token safely.
    Order:
      1. Environment variable
      2. Keyring
      3. Prompt user
    """
    # 1. Env var
    token = os.getenv("PYPI_TOKEN")
    if token:
        print("Using PyPI token from environment variable.")
        return token

    # 2. Keyring
    token = keyring.get_password(SERVICE, "puba")
    if token:
        backend = keyring.get_keyring()
        print(f"Using PyPI token stored in {backend}.")
        return token

    # 3. Prompt
    token = getpass.getpass("Enter PyPI token: ")
    return token


def store_token():
    """
    Prompt the user for PyPI token and store it securely.
    """
    token = getpass.getpass("Enter PyPI token: ")

    keyring.set_password(SERVICE, "puba", token)

    system = platform.system()

    if system == "Darwin":
        location = "macOS Keychain"
    elif system == "Windows":
        location = "Windows Credential Manager"
    elif system == "Linux":
        location = "Linux Keyring backend (may vary)"
    else:
        location = "Unknown secure store"

    print(
        f"PyPI token stored securely in {location}. You can now run 'puba publish' without re-entering it."
    )
