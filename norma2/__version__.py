from importlib import metadata

__version__ = ""

try:
    dependencies = metadata.requires("norma2")
except Exception:
    dependencies = []
