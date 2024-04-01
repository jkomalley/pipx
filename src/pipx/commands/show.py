from pathlib import Path
from typing import List

from pipx.constants import ExitCode
from pipx.util import PipxError
from pipx.venv import Venv


def show(
    package: str,
    venv_dir: Path,
    include_injected: bool = False,
    files: bool = False,
) -> ExitCode:
    venv = Venv(venv_dir)
    if not venv.python_path.exists():
        raise PipxError(f"venv for {package!r} was not found. Was {package!r} installed with pipx?")
    venv.verbose = True
    pip_args: List[str] = ["show"]
    if files:
        pip_args.append("--files")
    pip_args.append(package)
    if include_injected:
        for injected_package in venv.pipx_metadata.injected_packages:
            pip_args.append(injected_package)
    return venv.run_pip_get_exit_code(pip_args)
