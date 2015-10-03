#!/bin/env python2.7
# -*- coding: utf-8 -*-
# decipher.py
# Author:   Adrian Marin Portillo
# Date:     October 3rd 2015
# Version:  1.0
# Location: https://github.com/mangu93
# Translating easy encriptions methods
# The translation is made into english.

import re
import sys
import binascii


# Cesar: D:M -> D-K (mod 26)
def cesar(line,k):
	line_ret = ""
	for letter in line:
		if letter.isalpha():
			num = ord(letter)
			num += k
			if letter.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num +=26
			elif letter.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
			line_ret+=chr(num)
		else:
			line_ret+=letter
	return line_ret

#Reverse the letters
def atbash(line):
	alphabet = u'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9'.split()
	backward = u'Z Y X W V U T S R Q P O N M L K J I H G F E D C B A z y x w v u t s r q p o n m l k j i h g f e d c b a 9 8 7 6 5 4 3 2 1 0'.split()
	line_ret = ""
	for letter in line:
		if letter in alphabet:
			for i in xrange(len(alphabet)):
				if alphabet[i] == letter:
					pos = i
			line_ret+=backward[pos]
		else:
			line_ret+=letter
	return line_ret

#Numbers for letters
def az(line):
	alphabet = u'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
	numbers =  u'1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26'.split()
	line_ret=""
	CARRIS_REGEX=r'([0-9]{1,2})|(\s)|(\?)'
	pattern = re.compile(CARRIS_REGEX)
	for match in pattern.finditer(line):
		if match.group(0) in numbers:
			pos = numbers[int(match.group(0))-1]
			letter = alphabet[int(pos)-1]
			line_ret += letter
		else:
			line_ret += match.group(0)
	return line_ret

#Binary to ASCII text.
def binary(line):
	line_ret = binascii.unhexlify('%x' % line)
	return line_ret

#Vigenère method
def vigenere(line, key):
	line_ret=""
	keyIndex = 0
	key = key.upper()
	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for symbol in line:
		num = LETTERS.find(symbol.upper())
		if num!= -1:
			num -= LETTERS.find(key[keyIndex])
			num %= len(LETTERS)
			if symbol.isupper():
				line_ret+=LETTERS[num]
			elif symbol.islower():
				line_ret+=(LETTERS[num]).islower()
			keyIndex +=1
			if keyIndex == len(key):
				keyIndex=0
		else:
			line_ret+=symbol
	return line_ret

#Support functions

def isText(line):
	return not(any(char.isdigit() for char in line))

#Main function
def main():
	if len(sys.argv) == 1:
		input = raw_input("Enter the text.\n")
		#Text ones.
		if isText(input):
			print "ATBASH: " + atbash(input)
			for a in range(1,26):
				print "CESAR MOD " + str(a) + " " + cesar(input,a)
		else:
			try:
				n = int(input,2)
				print "BINARY: " + binary(n)
			except ValueError:
				print "A1Z26 : " + az(input)
		
if __name__ == '__main__':
	main()
