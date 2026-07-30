from errors import FileNotValidError, ACPYSyntaxError

def interpret(file: str):
    if not file.endswith(".acpy"):
        raise FileNotValidError(
            f'File: {file} is not an acpy file. (Expects ".acpy" file-extension.)'
        )

    with open(file, 'r') as f:
        lines = f.read().split("\n")

    for i, line in enumerate(lines):
        if not line:
            continue
        elif not all(char.isdigit() or char == " " for char in line):
            raise ACPYSyntaxError(
                f"Line: {i} contains unallowed characters: {line}"
        )
        else:

            cmd = ""
            for char in line.split(" "):
                char = int(char)
                c=chr(char)
                cmd += c
            namespace = {}
            exec(cmd, namespace)
            cmd = ""