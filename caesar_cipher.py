# The following code is a Caesar cipher encryption program that takes 
# the message and the offset value as inputs

# Inputs for the emcryption
message_to_be_encrypted = input("Enter the message to be encrypyed: ")
cipher_offset_value = int(input("Enter the offset value for the characters: "))

# Caesar cipher definition function
def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # no diatrical marks
    alphabet_with_diatrics = 'aàâăāãåæbcçčdeéëėfghiïjklmnñoôpqrřsştuûŭvwxyzž' # Iv'e included the common diatrical marks in the English language
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(message_to_be_encrypted, cipher_offset_value)