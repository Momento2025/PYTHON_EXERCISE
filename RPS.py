import random
def rps():
    while True:
        user = input('Pick from choices(rock,paper,scissor) or type to quit: ').lower()
        if user == 'quit':
            print('End')
            break

        if not user:
            print('Invalid pick again')
            continue

        if user not in ['rock','paper','scissor']:
            print('Pick again')
            continue

        letter = user[0]
        comp = random.choice(['r','p','s'])

        if letter == comp:
            print('It\'s a tie')
            continue
        
        elif(
            letter == 'r' and comp == 'p' or
            letter == 'p' and comp == 's' or
            letter == 's' and comp == 'r'
        ):
            print(f'{user},{comp} You lose')

        else:
            print(f'{user},{comp} You win')

rps()