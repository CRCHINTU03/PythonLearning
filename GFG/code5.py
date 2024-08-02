"""
In this question, we'll use Regex to validate a password. You will be provided a string str which you have to validate.

The validation rules are as follows:

The string is valid only if it starts with lowercase characters, followed by special characters !@#$% followed by numbers.
In any other case the string is not valid.





def validate(str):
    pat= "[a-z]+[!@#$%]+[0-9]"
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False

def validate(str):
    pat= '^[a-z]+[^\w]+[\d+]'##your pattern here
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False
"""
import re
def validate(str):
    pat= r'\w+\W+\d+'
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False