import random
def dice_roll():
    val = random.choice([1,2,3,4,5,6])
    return f'The outcome is {val}'
for i in range(5):
    print(dice_roll())