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

    def encode_cipher(self, message, key):
        encoded_message = ""
        for letter in message:
            if letter in self.alphabet:
                encoded_message += self.alphabet[self.alphabet.index(letter) + key]
            else:
                encoded_message += letter
        return encoded_message

    def decode_cipher(self, message, key):
        decoded_message = ""
        for letter in message:
            if letter in self.alphabet:
                decoded_message += self.alphabet[self.alphabet.index(letter) - key]
            else:
                decoded_message += letter
        return decoded_message
