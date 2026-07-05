import random
def user():
    value=[random.choice([True,False]) for _ in range(3)]

    if all (value):
        print('All true')
    elif not any(value):
        print('All False')
    else:
        result_True=value.count(True)
        result_False=value.count(False)
        print(f'{result_True} True and {result_False} False')
    
for _ in range(10):
    user()

