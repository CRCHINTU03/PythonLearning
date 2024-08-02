"""

Given a string S, the task is to determine whether the string starts and ends with the characters 'gfg' (case insensitive). 
In order to complete this task, you need to utilize the string functions S.lower(), S.upper(), S.startswith('string2'), and S.endswith('string2'). 
By using these functions, you can check if the given string S meets the specified conditions of starting and ending with 'gfg'.

"""

def gfg(S):
    b = S.lower()
    if(b.startswith("gfg") and b.endswith("gfg")):  
        print ("Yes")
    else:
        print ("No")

