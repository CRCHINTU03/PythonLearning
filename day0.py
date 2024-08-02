## which means that the Python code is executed line by line. This makes it easy to test and debug code. ---( interpreted)
# 

##first_name = "bro"
#last_name = "brolash"

#fullname = first_name + " " + last_name
#print(fullname)
#print(type(fullname)) -- to get the type of the data variable.


#age = 21 data type = integer whole numbers integers
#age += 1
#print(age)
#print(type(age)) // to get the type of the variable (data type)

#height = 163.5  data type = float
#print("you'r height is " + str(height) + " cm.") // how to concate . with other data types .// here with string we use 
#print(type(height))

#human = False
#print( "are you a human " + str(human))
#print(type(human))

# multiple assignment to assign values for multiple variables at same time in one line of cede

#bro , age , human = "brocode" , 21, True
#print(bro)
#print(age)
#print(human)

#lisa = bunny = maker = 30
#print(lisa)
#print(bunny)
#print(maker)

# string methods 

#name = "bro code"

#print(len(name)) # length of the string
#print(name.find("o")) # finds the first occurance of specific value
# print(name.capitalize())  - will capitalize the first alphabet
#print(name.upper()) - will upper case all alphabets
#print(name.lower()) - will lower case all letters
#print(name.isdigit()) #- will check if there are any digits
#print(name.count("o")) # count of occurance of alphabet
#print(name.replace("r","t")) -- would replace a character with a new one .


# typecasting 

#getValue1 = 1
#getValue2 = 3.0
#getValue3 = "6"

 
#getValue1 = int(getValue1)  - converting into  a int data type
#getValue2 = int(getValue2) - converting into  a int data type
#getValue3 = int(getValue3) - converting into  a int data type


#getValue1 = float(getValue1)   - convert into a float data type
#getValue2 = float(getValue2)  - convert into a float data type
#getValue3 = float(getValue3) - convert into a float data type


#getValue1 = str(getValue1) - convert into a string data type
#getValue2 = str(getValue2) - convert into a string data type
#getValue3 = str(getValue3) - convert into a string data type

#print(getValue1)
#print(getValue2)
#print(getValue3)

# user input where the user would provide the input values .. data is fetched from the user

#  this input data can be can be assigned to other variables and use in later required events / tasks


# always the data stored and received from the user would a string type.
#name = input("What's your name ? ")  - input() 
#age = int(input("what's your age ? ")) - so we would perfprm the necessary casting based on our requirements . we used int to get the age as value of integer.
#height = float(input("How tall are you ? ")) -- we use float casting to get the decimal values .

#print("My name is " + name) --  would print the value stored in the name variable .
#print( "you are " + str(age) + " years old") -- would print the value stored in age variable ... but it is a int variable so we need to convert it into a str variable by casting as we cannot concate int , float values with other strings.
#print("my height is " + str(height) + " cm talls") -- similary way we have typecasted a float value into a str so that we can perfrom .. concatentation.



# Math module  and its methods and functions.

#import math

#pi = 3.14 
#x = 1
#y = 2
#z =3

#print(round(pi)) we would round the pi to nearest whole number
#print(abs(pi)) we get only the +ve integers
#print(pow(pi,3)) the variable pi would be multiplied by itself with power times.
#print(math.ceil(pi)) would round to the next whole number
#print(math.floor(pi)) would round to the previous whole number
#print(math.sqrt(pi)) would print the squrt of the variable
#print(max(x,y,z)) would print the max values of the n variables 
#print(min(x,y,z)) would print the  min values of the n variables.


# string operations // slicing && indexing 

#name = "bro code"


# // using indexing property to index a string
#first_name = name[0:3] // indexing of a string [start: stop: step]
#last_name = name[4:]  
#funcky_name = name[::2] 
#reversed_name = name [::-1] // a way to reverse a string 

#print(first_name)
#print(last_name)
#print(funcky_name)
#print(reversed_name)

#// slicing property

#website1 = "https://google.com"
#website2 = "https://wikipedia.com"

#getSliceValue = slice(8,-4)  // we do define a variable to assign the slice property we cannot directly assign it to the variable which 
# we want to change like we did using indexing property.

# once a variable is assigned to the slice property we can call it varx[slicevariable] like this.

# +ve indexing and -ve indexing to get the index positions of various strings .
#print(website1[getSliceValue])
#print(website2[getSliceValue])

# statements in ( if , elif, else)

#age = int(input("enter you're age : "))

#if age == 100:
 #   print("you're lucky to be alive for these many years ")
#elif age>=18:
 #   print("you're legal citzen")
#elif age<0:
 #   print("you're yet to be born")
#else:
 #   print("you're not a taxing paying citizen yet")

## be careful indentation matters ... a lot ..


## logical operators ( && ,, || , !) = (and,or ,not)

## not operator will be used to execute one or more condtions if it is true.

## loops.

## loop1 - while loop - will execture it's block of code , as long as it's condition is true.

## there will be possiblity to create a infinite loop

##name = "" // one way

#name = None // another way

#while not name:
  #  name = input("enter your name : ")

#print("hello " +name)

## 
##### For loop  a statement that will execture it's code a limited amount of time.


#for i in range(10):
 #   print(i)


#or j in range(50,100):
  #  print(j)

#for k in "bro code":
 #   print(k)

#import time // importing time module

#for seconds in range(10,0,-1): range of 10 ,0 with start 10 and end 0 and step -1 index
    #print(seconds) print the value
   # time.sleep(2) it slow down the loop and result value by 2 seconds because of sleep function

#print(" Happy life")


## Nestead for loop

#rows = int(input("Enter number of rows: "))
#columns = int(input("Enter number of columns "))
#symbol = input("Enter your desired symbol")

#for i in range(rows):
   # for j in range(columns):
   #     print(symbol , end="")
  #  print()

# loop control statements .. break continue pass

# break - it would terminate the loop entirely

# continue -  it would skip the iteration and move to a new variable

# pass - acts as a place holder .

#while True:
  #  name = input("enter you're name: ")
  #  if name != "":
   #     break

#phone_nbr = "123-456-7890"

#for i in phone_nbr:
  #  if i == "-":
     #   continue
   # print(i,end = "")


#for i in range(1,21):
 #   if i == 13:
  #      pass
  #  else:
   #     print(i,end = "")

### data type - list 

## list - used to store a mutiple place in a single variable.

#food = ["pizza" , "hamburger", "hotdog", "spaghetti", "pudding"]

#food[0] = "sushi"

#food.append("fruit")
#food.insert(2,"lionshare")
#food.pop()
#food.sort()
#food.remove("hotdog")



#for x in food:
   # print(x , end=" ")



## neasted list 2D list =  a list of lists


#drinks = ["coffe","tea","greentea"]

#snacks = ["puffs","eggrice", "lays"]

#dinner = ["indianfood", "mexicanfood", "italinfood"]

#food = [drinks,snacks,dinner]

#food[1][2]


### in lists we can insert different data types it

#### tuple // ordered and unchangeable

#getInformation = ("brocode", 21, "teacher")

#print(getInformation)
#print(getInformation.count("brocode"))
#print(getInformation.index(21))

#for x in getInformation:
   # print(x, end=" ")


# set = collection which is unordered , unindexed . No duplicate values.


#utensils = {"fork", "spoon", "knife"}

#dishes = {"bowl", "plates","cup","knife"}

#print(utensils)
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.pop()
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)


#print(dishes.difference(utensils))
#print(dishes.intersection(utensils))


#for i in utensils:
 #   print(i, end = " ")

 ### dictionay -- a chasngeable , unordered collection of unique key : value pairs 
 ###              fast because they use hasing ( allows to access values quickly)

capitals = {'usa':'washingthon DC',
            'India': 'delhi',
            'china':'beijing',
            'russia':'moscow'}

#capitals.update({'germany':'Berlin'})
#capitals.update({'usa':'las vegas'})

#print(capitals['russia'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#for key,value in capitals.items():
  #  print(key, value)

# *args = is parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments.

#def add(*numbers):
 #   sum = 0
  #  numbers = list(numbers)
   # numbers[0] = 0
    #for i in numbers:
     #   sum += i
    #return sum

#print(add(1,2,3,4,5,6))


## **kwargs = parameter that will pack all argument into a dictionary
## useful so that a function can accept a varying amount of keywords.


#def hello(**kwargs):
  #  print("Hello", end = " ")
   # for key,value in kwargs.items():
    #    print(value,end=" ")

#hello(title="Mr.",content=" male", middle = "dude",first="bro", last = "code")


# str.format() = optional method that gives users more control when displaying output

#number = 3.1405467
#print("the number is : {:.2f}".format(number))


## random module

#import random

#x = random.randint(1,6)
#y = random.random()

#my_list = ['rock','paper','scissors']
#choice = random.choice(my_list)

#cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

#random.shuffle(cards)
#print(cards)

## exception = events detected during execution that interrupt the flow of a program
"""
try:
    numeraartor = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numeraartor / denominator
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by zeroo")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
else:
    print(result)
finally:
    print("used in file handling")

"""
"""
import os

path = "/Users/chitntu_03/FreeCodeCamp/JS-INITIAL"

if os.path.exists(path):
    print("that location exists!")
    if os.path.isfile(path):
        print("that is file:")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("that location does not exists")


"""

# to read a file

"""
import os

try:
    with open("/Users/chitntu_03/FreeCodeCamp/JS-INITIAL/RPS.html") as file:
        print(file.read())
except FileNotFoundError:
    print("file does not exists")


"""

# to write a file
"""
import os 

text = "if we do not want to rewrite the file \n use a method append instead of w write"

with open('text.txt','a') as file:
    file.write(text)

"""

# copy a file 

#import shutil

#shutil.copyfile('text.txt','copy.txt')(src,desc)


# to move a file in python
"""
import os

source = "copy.txt"
desctination = "/Users/chitntu_03/JS_Bro/copy1.txt"

try:
    if os.path.exists(desctination):
        print("There is already a file")
    else:
        os.replace(source,desctination)
        print( source + " was moved")
except FileNotFoundError:
    print(source + " was not found")

"""


# to delete files using python
""" 
import os
import shutil

path = "folder"

try:
    #os.remove(path)
    #os.removedirs(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("file does not exist")
except PermissionError:
    print("you don'nt have the permission to delete the folder")
except OSError:
    print("you cannot delete that using the function")
else:
    print("the file has been sucessfully deleted")


"""



























