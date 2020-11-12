import os

COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32;1m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36;1m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

'''
# Example printing out some text

hello = "[[red]]hello [[blue]]world[[white]]"
print(colorText(hello))

# Example printing out an ASCII file

f = open("pythonlogo2.txt", "r")
ascii = "".join(f.readlines())
print(colorText(ascii))
'''
