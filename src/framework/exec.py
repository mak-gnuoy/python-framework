from dataclasses import dataclass
import logging
import subprocess
from typing import Optional
import asyncio


@dataclass
class Result:
    returncode: int
    stdout: str
    stderr: str


class Command:
    logger = logging.getLogger(__name__)

    @classmethod
    def run(cls, command: str) -> Result:
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
                shell=True,
            )
            return Result(result.returncode, result.stdout, result.stderr)
        except subprocess.CalledProcessError as e:
            cls.logger.debug(f"Command failed with exit code {e.returncode} {e.stderr}")
            raise RuntimeError(f"Command failed with exit {e}")

    @classmethod
    async def run_async(cls, command: str) -> Result:
        try:
            process = await asyncio.create_subprocess_shell(
                command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )

            stdout, stderr = await process.communicate()
            return Result(process.returncode, stdout.decode(), stderr.decode())

        except subprocess.CalledProcessError as e:
            cls.logger.debug(f"Command failed with exit code {e.returncode} {e.stderr}")
            raise RuntimeError(f"Command failed with exit {e}")
