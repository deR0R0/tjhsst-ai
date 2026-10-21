# Robert Zhao, 2026
import re

def num_30(str):
    # Current test checks if the string is '0' 
    pattern = "^0$|^10[01]$"   #notice that python does not want / /
    match = re.search(pattern, str)
    print ("string is either 0, 100, or 101: ", match != None)

def num_31(str):
    # Current test checks if the string is '0' 
    print ("string is a binary string:", re.search("^[01]*$", str) != None)

# Pre-condition: input is a binary string, so you do not need to check if it's a binary or not.
def num_32(str):
    pattern = '0$'
    print ("string is an even binary number:", re.search(pattern, str) != None)

def num_33(str):
    # Current test searches words with 'a' 
    pattern = r"\b[a-z]*[aeiou][a-z]*[aeiou][a-z]*\b"
    # Notice that python does not support /i in the pattern. 
    # Use re.I for case insensitive when you match(exact same) or search(has one or more)
    print ("there's a word at least two vowels:", re.search(pattern, str, re.I) != None)

def num_34(str):
    pattern = r"^1[01]*0$|^0$"
    print ("even binary integer string:", re.search(pattern, str) != None)

def num_35(str):
    pattern = "^[01]*110[01]*$"
    print ("binary string including 110:", re.search(pattern, str) != None)

def num_36(str):
    pattern = "^.{2,4}$"
    print ("length at least two, but at most four:", re.search(pattern, str) != None)

def num_37(str):
    pattern = r"^\d{3} *-? *\d\d *-? *\d{4}$"
    print ("valid social security number:", re.search(pattern, str) != None)

def num_38(str):
    # When you read multiline input such as "I\nAM\nSAM."
    str = str.replace('\\n', '\n')
    pattern = r"^.*?d\w"
    
    # When you want to use /im options:
    d_search = re.search(pattern, str, re.I | re.MULTILINE)
    print ("first word with d on a line:", d_search != None)

def num_39(str):
    pattern = "^0[01]*0$|^1[01]*1$|^[01]$|^$"
    print ("There's same number of 01 substrings as 10 substrings: ", re.search(pattern, str) != None)

while(True):
    input_num = input("Choose the exercise # (31 - 40 or -1 to terminate):")
    if input_num == '-1': exit(0)
    input_str = input("Input string: ")
    eval("num_"+input_num)(input_str)
    print()
    
''' Sample Output
Choose the exercise # (31 - 40 or -1 to terminate):31
Input string: 100
string is either 0, 100, or 101:  True

Choose the exercise # (31 - 40 or -1 to terminate):31
Input string: 1000
string is either 0, 100, or 101:  False

Choose the exercise # (31 - 40 or -1 to terminate):40
Input string: 101
There's same number of 01 substrings as 10 substrings:  True

Choose the exercise # (31 - 40 or -1 to terminate):40
Input string: 100
There's same number of 01 substrings as 10 substrings:  False

Choose the exercise # (31 - 40 or -1 to terminate):40
Input string: 0
There's same number of 01 substrings as 10 substrings:  True

Choose the exercise # (31 - 40 or -1 to terminate):-1
Good bye

 ----jGRASP wedge2: exit code for process is 1.
 ----jGRASP: operation complete.

'''