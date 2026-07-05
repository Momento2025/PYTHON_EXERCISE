import random
def same():
    while True:
        user = input('Pick from chooices (Spade, Heart, Diamond, Clubs) or type to Stop: ').lower()
        
        if user == 'stop':
            print('ended')
            break

        elif not user:
            print('Invalid')
            continue
        elif user not in ['spade','heart','diamond','clubs']:
            print('Pick from choices')
            continue

        letters = random.choice(['s','h','d','c'])
        let = user[0]

        if let == letters:
            print(f'{user},{letters} The same suit. You win!')
        else:
            print(f'{user},{letters} Different suits. Try again.')
same()
