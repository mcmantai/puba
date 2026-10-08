import subprocess
import shutil


def build_package():

    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("build", ignore_errors=True)

    subprocess.run(["python", "-m", "build"], check=True)


def upload_package(token, test=False):

    repo = "testpypi" if test else "pypi"

    subprocess.run(
        [
            "python",
            "-m",
            "twine",
            "upload",
            "--repository",
            repo,
            "dist/*",
            "-u",
            "__token__",
            "-p",
            token,
        ],
        check=True,
    )
