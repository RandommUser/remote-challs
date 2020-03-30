#!/usr/bin/env python3

import sys
import string
import re

pattern = re.compile("^[a-zA-Z ]+$")

def pUsage():
        print("usage: ./phakakos.py <a-zA-Z string>")
        exit(1)

def morse_letter(letter):
	code={
	"a": ".-",
	"b": "-...",
	"c": "-.-.",
	"d": "-..",
	"e": ".",
	"f": "..-.",
	"g": "--.",
	"h": "....", 
	"i": "..", 
	"j": ".---", 
	"k": "-.-", 
	"l": ".-..", 
	"m": "--",
	"n": "-.", 
	"o": "---", 
	"p": ".--.", 
	"q": "--.-", 
	"r": ".-.", 
	"s": "...", 
	"t": "-", 
	"u": "..-", 
	"v": "...-", 
	"w": ".--", 
	"x": "-..-", 
	"y": "-.--",
	"z": "--..",
	}
	return code.get(letter, "invalid")

def morse_word(word):
        if (pattern.match(word) == None):
                pUsage()
        morseWord =""
        for c in word:
                if (c.isalpha()) == True:
                        morseWord+=morse_letter(c.lower())
                elif (c == ' '):
                        morseWord+=' '
                else:
                        pUsage()
        print(morseWord)

def mainLoop():
        if len(sys.argv) == 2:
                morse_word(sys.argv[1])
        else:
        	pUsage()

if __name__ == '__main__':
	mainLoop()
exit()
