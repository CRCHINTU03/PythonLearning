"""

def sumOfCurrentandPreviousNumbers(num1,num2):
    for i in range (num1,num2):
        sum = i + (i-1)
        print(f"current Number:  {i}  previous Number : {i-1}  Sum: {sum} ")

print(sumOfCurrentandPreviousNumbers(1,10))


"""



print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    
    previous_num = i # values of previous number  1,2,3,4,5,6,7,8,9