

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("type 'encode' to encrypt, type 'decode' to decrypt \n").lower()
text = input("type your message \n").lower()
shift = int(input("type shift nuber \n"))

def encrypt(original_text,shift_amount):
    cipher_text = ''
    for letter in original_text:
        get_index = alphabet.index(letter)
        add_shift_value = (get_index + shift) % 26
        letter_char = alphabet[add_shift_value]
        print(letter_char)
encrypt(original_text=direction,shift_amount=shift)