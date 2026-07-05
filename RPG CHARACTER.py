#RPG character building
def create_character(name,strength,intelligence,charisma):
    if not isinstance(name,str):
        return 'The character name should be a string'
    if name =='':
        return 'The character should have a name'
    if len(name) >10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    
    #stat validation

    if not all (isinstance(stats,int) for stats in [strength,intelligence,charisma]):
        return 'All stats should be integers'
    if any(stats < 1 for stats in [strength,intelligence,charisma]):
        return 'All stats should be no less than 1'
    if any(stats > 4 for stats in [strength,intelligence,charisma]):
        return 'All stats should be no more than 4'
    if strength+intelligence+charisma != 7:
        return 'The character should start with 7 points'
    
    #

    str_line = 'STR' +  '●' * strength + '○' * (10-strength)
    int_line = 'INT' +  '●' * intelligence + '○' * (10-intelligence)
    chr_line = 'CHR' +  '●' * charisma + '○' * (10-charisma)

    return f'{name}\n{str_line}\n{int_line}\n{chr_line}'

print(create_character('ren',4,2,1))
