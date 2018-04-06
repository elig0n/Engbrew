#!/usr/bin/python3
# laycon.py - convert english characters to hebrew layout

import sys

lay = {
        'q': '/', 'w':'\'', 'e': 'ק', 'r': 'ר', 't': 'א', 'y': 'ט', 'u': 'ו', 'i': 'ן', 'o': 'ם', 'p': 'פ',
        'a': 'ש', 's': 'ד', 'd': 'ג', 'f': 'כ', 'g': 'ע', 'h': 'י', 'j': 'ח', 'k': 'ל', 'l': 'ף', '\'': ',', 
        'z': 'ז', 'x': 'ס', 'c':'ב', 'v':'ה', 'b':'נ', 'n':'מ', 'm':'צ', ',':'ת', '.':'ץ', '/':'.'
}

try:
    str = sys.argv[1]
except IndexError:
    print("No argument or string was supplied.")

for c in str:
    if c in lay: 
        print(lay[c], end='')
    else:
        print (c, end='')

print()
