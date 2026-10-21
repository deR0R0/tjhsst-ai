# Robert Zhao, 2026
import re

def num_43(str):
    pattern = "^(..)*.$"
    match = re.search(pattern, str)
    print ("match strs of odd length: ", match != None)

def num_44(str):
    print ("string is a binary string:", re.search("^0([01]{2})*$|^1[01]([01]{2})*$", str) != None)

# Pre-condition: input is a binary string, so you do not need to check if it's a binary or not.
def num_45(str):
    pattern = r'^\b\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*\b$'
    print ("string is an even binary number:", re.search(pattern, str) != None)

def num_46(str):
    # Current test searches words with 'a' 
    pattern = r"^(10|0)*1*$"
    # Notice that python does not support /i in the pattern. 
    # Use re.I for case insensitive when you match(exact same) or search(has one or more)
    print ("there's a word at least two vowels:", re.search(pattern, str, re.I) != None)

def num_47(str):
    pattern = r"^[bc]*a[bc]*$|^[bc]+$"
    print ("even binary integer string:", re.search(pattern, str) != None)

def num_48(str):
    pattern = r"^([bc]|a[bc]*a)+$"
    print ("binary string including 110:", re.search(pattern, str) != None)

def num_49(str):
    pattern = r"^(2|1[02]*1)([02]|1[02]*1)*$"
    print ("length at least two, but at most four:", re.search(pattern, str) != None)

    d_search = re.search(pattern, str, re.I | re.MULTILINE)
    print ("first word with d on a line:", d_search != None)

while(True):
    input_num = input("Choose the exercise # (31 - 40 or -1 to terminate):")
    if input_num == '-1': exit(0)
    input_str = input("Input string: ")
    eval("num_"+input_num)(input_str)
    print()
    