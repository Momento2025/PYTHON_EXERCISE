import random

def arithmetic(a,b):

    operator = random.choice(['+','-','*','//'])
    if operator == "+":
        return f'{a} + {b} = {a+b}'
    elif operator == "-":
        return f'{a} - {b} = {a-b}'
    elif operator == '*':
        return f'{a} * {b} = {a*b}'
    elif operator == "//":
        if b == 0:
            return 'cant divide to zero'
        
    return f'{a}//{b} = {a//b}'

for _ in range(5):

    a = random.randint(0,100)
    b=random.randint(0,100)

    print(arithmetic(a,b))





