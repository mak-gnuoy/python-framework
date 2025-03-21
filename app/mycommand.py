import asyncio

from framework.exec import Command

if __name__ == "__main__":
    result = Command.run("ls -alh")
    print(
        f"returncode={result.returncode}\nstdout=\n{result.stdout}stderr=\n{result.stderr}"
    )

    result = asyncio.run(Command.run_async("ls -alh"))
    print(
        f"returncode={result.returncode}\nstdout=\n{result.stdout}stderr=\n{result.stderr}"
    )
