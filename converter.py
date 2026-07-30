import argparse
from errors import *

class UndefinedModeError(Exception):
    pass

parser = argparse.ArgumentParser()

parser.add_argument("--mode", "-m", help="The mode for the converter.", required=True)
parser.add_argument("--input", "-i", help="The input for the converter, either from a file or a string.", required=True)
parser.add_argument("--path", "-p", help="The path to write the file to.", required=True)
modes = ["text", "file"]
args = parser.parse_args()

if not args.mode in modes:
    raise UndefinedModeError(
        f"Mode: {args.mode} is not supported, try text or file."
    )

elif args.mode == "file":
    with open(args.input, 'r') as f:
        content = f.read()

    text = content

if args.mode == "text":
    text = args.input





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

with open(args.path, 'w') as f:
    f.write(
        c.strip()
    )