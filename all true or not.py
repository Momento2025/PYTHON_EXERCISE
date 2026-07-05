import random
def vowel():
    let = ['a','e','i','o','u']
    val = chr(random.randint(ord('a'),ord('z')))

    if val in let:
        return val,True
    else:
        return val,False
print(vowel())

