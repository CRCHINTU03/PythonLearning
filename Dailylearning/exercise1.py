
"""


num1 = int(input("enter num1 :"))

num2 = int(input("enter num2 :"))

multiplication = num1 * num2

addition  = num1 + num2

if multiplication < 1000:
    print(f'The value of the two numbers is {multiplication} ')
else:
    print(f'The Value of the two numbers is {addition}')


"""


def multiplicationAndSumNumbers(num1,num2):

    product = num1 * num2
    sum = num1 + num2
    
    if product < 1000:
        return(f'The value of the two numbers is {product} ')
    else:
        return (f'The Value of the two numbers is {sum}')
    

print(multiplicationAndSumNumbers(30,40))
print(multiplicationAndSumNumbers(20,30))
