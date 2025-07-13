import string
import random
import json

def generate_cipher_key():
    alphabet = string.ascii_lowercase
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)


    cipher_key = dict(zip(alphabet, shuffled_alphabet))
    return cipher_key

def encrypt_message(message_text, cipher_key):
    message_text = message_text.lower()
    encrypted_text = ""

    for original_character in message_text:
        if original_character in cipher_key:
            encrypted_text += cipher_key[original_character]
        else:
            encrypted_text += original_character  # keep punctuation/spaces

    return encrypted_text

def encrypt_messages(message_text, cipher_key):
    message_text = message_text.lower()
    encrypted_text = ""

    for original_character in message_text:
        if original_character in cipher_key:
            encrypted_text += cipher_key[original_character]
        else:
            encrypted_text += original_character  # keep punctuation/spaces

    return encrypted_text

def  save_cipher_key(filename='cipher_key.json'):
    with open(filename,'r') as key_file:
        return json.load(key_file)

