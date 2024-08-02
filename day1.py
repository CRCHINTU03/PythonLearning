out = []

def myfunc(x):
    
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)


myfunc('chittaranjan')
print(out)
