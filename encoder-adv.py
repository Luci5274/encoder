import string
import random
import json

def menu():
    print("\nCipher Tool")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")

    user_choice = input("Make your choice: ")

    if user_choice == "1":
        user_message = input("Enter message to encrypt: ")
        cipher_key = generate_cipher_key()
        encrypted_output = encrypt_message(user_message, cipher_key)

        print(f"\nEncrypted Message:\n{encrypted_output}")
        save_cipher_key(cipher_key)

        menu()  # Return to menu

    elif user_choice == "2":
        encrypted_input = input("Enter the encrypted message: ")
        cipher_key = load_cipher_key()
        decrypted_output = decrypt_message(encrypted_input, cipher_key)

        print(f"\nDecrypted Message:\n{decrypted_output}")

        menu()  # Return to menu

    elif user_choice == "3":
        print("Goodbye!")
        exit()

    else:
        print("Invalid choice. Try again.")
        menu()  # Retry menu on bad input

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

def save_cipher_key(cipher_key, filename="cipher_key.json"):
    with open(filename, "w") as key_file:
        json.dump(cipher_key, key_file)
    print(f"Cipher key saved to {filename}")

def load_cipher_key(filename="cipher_key.json"):
    with open(filename, "r") as key_file:
        return json.load(key_file)

def decrypt_message(encrypted_text, cipher_key):
    reverse_cipher_key = {substituted_letter: original_letter for original_letter, substituted_letter in cipher_key.items()}
    decrypted_text = ""

    for encrypted_character in encrypted_text:
        if encrypted_character in reverse_cipher_key:
            decrypted_text += reverse_cipher_key[encrypted_character]
        else:
            decrypted_text += encrypted_character

    return decrypted_text

if __name__ == "__main__":
    menu()
