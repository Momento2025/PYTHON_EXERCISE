words = ['sky','apple','rhythm','fly','orange']
for word in words:
    for letter in word:
        if letter.lower() in 'aeiuo':
            print(f'{word} does have a vowel {letter}')
            break
    else:
        print(f'{word} does not have a vowel {letter}')
