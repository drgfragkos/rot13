# rot13.py
ROT13 is a simple letter substitution cipher, rotating by 13 letters.

rot13.py v0.1 - replace each letter with the 13th letter after it : (c)gfragkos 2014

usage: rot13.py TEXT
   without parameters       Expects input from pipe
   TEXT                     Will rotate any given text

I wanted a program to be able to do ROT13 by accepting input either from pipe or stdin.
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 
13 letters after it, in the alphabet. ROT13 is a special case of the Caesar cipher.
to undo ROT13, the same algorithm is applied, so the same action can be used for 
encoding and decoding. The algorithm provides virtually no cryptographic security.

