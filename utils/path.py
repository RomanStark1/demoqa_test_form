import tests
import os
from pathlib import Path

def absolut_path(path):
    file_path = str(Path(tests.__file__).parent.parent.joinpath(f'src/{path}'))
    return os.path.abspath(file_path)