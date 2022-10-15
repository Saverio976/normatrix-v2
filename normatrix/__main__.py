import sys
from pathlib import Path

from rich.console import Console

from normatrix.config.config import get_config
from normatrix.config.config_class import OutputFormat
from normatrix.main import main
from normatrix.utils import open_file

config = get_config(Console(record=True))

ex = main(config)

out = None
outfilext = None
outfile = ".normatrix.report"
if config.format == OutputFormat("HTML"):
    out = config.console.export_html()
    outfilext = ".html"
if config.format == OutputFormat("MARKDOWN"):
    out = config.console.export_text()
    outfilext = ".txt"
if out:
    Path(f"{outfile}{outfilext}").write_text(out)
    open_file(f"{outfile}{outfilext}")

sys.exit(ex)
