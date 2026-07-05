
def caesar(text, shift, encrypt = True):
    if not isinstance(shift,int):
        return 'Shift must be an integer value'
    if shift < 1 or shift >5:
        return 'Shift must be an integer between 1 and 25'
    
    if not encrypt:
        shift = -shift
   
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet=alphabet[shift:]+alphabet[0:shift]
    translation_table = str.maketrans(alphabet,shifted_alphabet)
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text,shift)

def decrypt(text, shift):
    return caesar(text, shift, False)
  
encrypted_text = decrypt('freeCodeCamp', 3)
decrypted_text=caesar(encrypted_text, 3)
print(encrypted_text)
print(decrypted_text)



