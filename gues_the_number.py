secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('pick (1 - 5): '))
    if guess != secret_number:
        print('wrong! try again')
print('You got this')
