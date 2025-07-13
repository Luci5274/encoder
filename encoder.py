import random
import string

alphabet = string.ascii_lowercase

shuffled = list(alphabet)
random.shuffle(shuffled)

cipher = dict(zip(alphabet,shuffled))

message = input('text to encrypt: ').lower()

encrypted = ' '

for char in message :
    if char in cipher:
        encrypted += cipher[char]
    else:
        encrypted += char

print(f'\n encrypted message:{encrypted}')

print("\n Cipher key used:")
for org_char, enc_char in cipher.items():
    print(f"{org_char} -> {enc_char}")
