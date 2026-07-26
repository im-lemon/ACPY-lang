import sys
from interpreter import interpret
from errors import *

if not len(sys.argv) == 2:
    raise FileNotPassedError(
        "No file was passed. Aborting..."
    )

else:
    file = sys.argv[1]
    interpret(file)