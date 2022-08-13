import os

jn = os.path.join

# if current working directory is "rom2books", change working directory to upper level
if os.path.basename(os.path.abspath(".")) == "rom2books":
    os.chdir("..")

from src.resources import Resources
from src import utils
from src.utils import dumpobj
from src import plot

__all__ = ["os", "jn", "Resources", "utils", "dumpobj", "plot"]
