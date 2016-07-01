"""
Title: Mega Projects List - Caesar Cipher
Author: Mandeep Bhutani
Date: 06/20/2016

Problem: Implement a Caesar cipher, both encoding and decoding. The key is an
integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z).
The encoding replaces each letter with the 1st to 25th next letter in the
alphabet (wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts
"HI" to "BC". This simple "monoalphabetic substitution cipher" provides almost
no security, because an attacker who has the encoded message can either use
frequency analysis to guess the key, or just try all 25 keys.
"""


class CaesarCipher(object):

    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2

    def encrypt_message(self, message, key):
        encrypted_message = ""
        for letter in message:
            if letter.upper() in self.alphabet:
                encrypted_message += self.alphabet[self.alphabet.index(letter) + key]
            else:
                encrypted_message += letter
        return encrypted_message

    def decrypt_message(self, message, key):
        decrypted_message = ""
        for letter in message:
            if letter.upper() in self.alphabet:
                decrypted_message += self.alphabet[self.alphabet.index(letter) - key]
            else:
                decrypted_message += letter
        return decrypted_message


def main():
    cipher = CaesarCipher()
    task = str(input('Would you like to encrypt or decrypt your message? '))
    message = str(input('Enter your message: '))
    key = int(input('Enter your key (number between 1-25): '))
    if task == 'encrypt':
        return cipher.encrypt_message(message, key)
    elif task == 'decrypt':
        return cipher.decrypt_message(message, key)
