x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
z = int(input("Enter value for z: "))
n = int(input("Enter value for n: "))

result = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                result.append([i, j, k])

print(result)

"""

list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print(list)

"""