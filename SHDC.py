def SHDC():
    while True:
        user = input('Pick from Choices (Spade,Diamond,Heart,Clubs) or type to stop: ').lower()
        cho = ['spade','heart','diamond','clubs']


        if user == 'stop':
            print('Program ended')
            break
        
        elif not user:
            print('Invalid Pick Again')
            continue

        if user not in cho:
            print('pick from choices')
            continue

        picked=cho[cho.index(user)][0]

        print(f'{user},{picked} well done!')

SHDC()


        
