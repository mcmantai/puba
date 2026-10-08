# puba

**Safe Python package release CLI.**

Check, build and publish Python packages to PyPI from one command.

## Install

From the project folder:

```bash
python3 -m venv .venv
.venv/bin/pip install -e .
```

This also installs `keyring`, `build` and `twine`.

Optional tools, used if installed:

- [`pytest`](https://pytest.org): runs your tests
- [`gitleaks`](https://github.com/gitleaks/gitleaks): scans for secrets

## Usage

### 1. Store your PyPI token (one time)

```bash
puba auth
```

The token is saved in your system keyring (macOS Keychain, Windows Credential Manager, or a Linux keyring backend).

### 2. Run the safety checks

```bash
puba checks
```

This:

1. Makes sure `build` and `twine` are installed (offers to install them if not)
2. Fails if the git working directory has uncommitted changes
3. Scans for secrets with `gitleaks` (skipped if not installed)
4. Runs `pytest` (skipped if not installed or no tests are found)
5. Builds the package into `dist/`

Nothing is uploaded.

### 3. Publish

```bash
puba publish          # run the checks, build and upload to PyPI
puba publish --test   # upload to TestPyPI instead
puba publish --dry    # run the checks and build, but don't upload
```

### Help

```bash
puba help
```

## Token lookup

When publishing, the token is taken from, in order:

1. The `PYPI_TOKEN` environment variable
2. The system keyring (saved with `puba auth`)
3. A prompt

The same token is used for PyPI and TestPyPI.

## CI

```bash
export PYPI_TOKEN=pypi-xxxxxxxxxxxx
puba publish
```

## License

MIT
