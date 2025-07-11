import string

def ceaser_encrypt(message, key):

    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    encrypted_messgae = message.lower().translate(cipher)

    return encrypted_messgae

def caeser_decrypt(encrypted_message, key):

    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    message = encrypted_message.translate(cipher)
    return message

message = 'I LOVE FOOD'
key = 3

encrypted_message = ceaser_encrypt(message, key)
print(f'Encrypted message: {encrypted_message}')

decrypted_message = caeser_decrypt(encrypted_message, key)
print(f'Decryted message: {decrypted_message}')