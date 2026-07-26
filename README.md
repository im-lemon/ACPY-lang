# ACPY

ACPY (Ascii-python) is an interpreted esoteric-programming language that is completely turing-complete. How?
The language only allows every character to be it's ASCII value.

For example, the ASCII value for "A" is 65.

So to print "Hello, world!", you'd write:

```ACPY
112 114 105 110 116 40 34 72 101 108 108 111 44 32 119 111 114 108 100 33 34 41                                            
P   R   I   N   T   (  "  H  E   L   L   O   ,      W  O   R   L   D   !  "  )
```

It works by looping through every ASCII value in the and turning it back into characters, and executing that line.


## Tools:

If you want to turn a piece of code into ACPY code, use the `converter.py` file.

usage:

```
python converter.py -m file -i file.txt
```

OR

```
python converter.py -m string -i 'print("Hello, world!")'
```

### Errors:

`FileNotPassedError`

FileNotPassedError means you forgot to pass a file into the interpreter wrapper!

`ACPYSyntaxError`

ACPYSyntaxError appears when you type letters into your ACPY file and try running it.

`UndefinedModeError` (converter)

This error appears when you put in an unsupported mode into the converter CLI mode argument.

`FileNotValidError`

This error appears when the file is not an ACPY file.