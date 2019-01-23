#! /usr/bin/python3
import subprocess
from copy import copy
from migen import *
from migen.fhdl import verilog
from migen.fhdl.verilog import convert

##### string converters ####
# change plaintext to a matrix
def textconverter(text):
        size = len(text) # size of plaintext

        #to hold the plaintext matrix
        newText = [] 

        # copy text into newText
        for i in range(size):
                newText.append(text[i])
        
        return newText

# change key text to a matrix
def keyconverter(key):
        size = len(key) # size of key
        assert size == 16

        #to hold the key matrix
        newkey = [] 

        # copy key into newkey
        for i in range(size):
                newkey.append(key[i])
        
        return newkey
    
def hexCharToInt(ch):
        if ch=='0' or ch=='1' or ch=='2' or ch=='3' or ch=='4' or ch=='5' or ch=='6' or ch=='7' or ch=='8' or ch=='9':
            return int(ch)
        elif ch=='a' or ch=='b' or ch=='c' or ch=='d' or ch=='e' or ch=='f': 
            return int(ch,16)
        else:
            return 0