import sys

from rich.console import Console

from normatrix.config.config import get_config
from normatrix.main import main

config = get_config(Console(record=True))

ex = main(config)
sys.exit(ex)
