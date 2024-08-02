email = input("enter you email: ")

index = email.index("@")

username = email[:index]
domain = email[index:]

print(f"you're username is {username} and your domain is {domain}")

