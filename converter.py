import argparse
from errors import *

class UndefinedModeError(Exception):
    pass

parser = argparse.ArgumentParser()

parser.add_argument("--mode", "-m", help="The mode for the converter.", required=True)
parser.add_argument("--input", "-i", help="The input for the converter, either from a file or a string.")
modes = ["string", "file"]
args = parser.parse_args()

if not args.mode in modes:
    raise UndefinedModeError(
        f"Mode: {args.mode} is not supported, try text or file."
    )

elif args.mode == "file":
    with open(args.input, 'r') as f:
        content = f.read()

    text = content.strip()

if args.mode == "text":
    text = args.input.strip()





def convert(text: str):
    end = ""
    for char in text:
        c = ord(char)
        c = str(c)
        c = f"{c} "
        end += c

    return end


c = convert(
    text
)

print(c)