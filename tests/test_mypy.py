import subprocess


class MypyError(Exception):
    pass


def test_mypy() -> None:
    result = subprocess.run(
        ["mypy", "--config-file", "mypy.ini", "."],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if result.returncode != 0:
        output = result.stdout.decode("utf-8").replace("\r\n", "\n\t")
        errors = result.stderr.decode("utf-8").replace("\r\n", "\n\t")
        error_messages = f"stdout:\n\t{output}\nstderr:\n\t{errors}"
        raise MypyError(f"mypy failed with return code {result.returncode}" f"\n{error_messages}")
