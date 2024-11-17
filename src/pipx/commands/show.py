from pathlib import Path
from typing import List

from pipx.constants import ExitCode
from pipx.util import PipxError
from pipx.venv import Venv

# def show() -> ExitCode:
def show(package: str, venv_dir: Path) -> ExitCode:
    venv = Venv(venv_dir)

    if not venv.root.exists():
        raise PipxError(f"venv for {package!r} was not found. Was {package!r} installed with pipx?")
    
    venv.verbose = True

    pip_args: List[str] = ["show", package]

    return venv.run_pip_get_exit_code(pip_args)
