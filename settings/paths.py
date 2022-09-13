import pathlib
from typing import Final

ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
FILES_PATH: Final[pathlib.Path] = ROOT_PATH.joinpath("files_storage")
