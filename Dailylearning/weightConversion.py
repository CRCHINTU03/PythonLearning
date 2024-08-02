

while  True:
    weight = float(input("Enter your weight: "))
    units = input("Kilograms or Pounds (K or L): ")

    if units == "K":
        weight = weight *  2.205
        units = "L"
        break
    elif units == "L":
        weight = weight / 2.205
        units = "Kgs"
        break
    else:
        print(f'{units} is invalid')
        break
        #units = input("Kilograms or Pounds (K or L): ")
        
print(f"you're weight is {round(weight, 3)} {units}")


