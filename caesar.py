'''
This code accepts a key as an integer and plaintext as a string. The code will
shift the plaintext by the key amount in the alphabet,
creating a secret message of sorts. For example, if the word is "Hello" and
a key of 1, the output would be "Ifmmp".
The code will not work if there's more than one argument, the key is not an
integer or if the key is negative.
By: Ben
'''

import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
capitalAlphabet = "ABCDEFHIJKLMNOPQRSTUVWXYZ"

#Function
def caeser(plaintext, key):
    ciphertext = ""
    
    for n in range(0, len(plaintext)):
        if plaintext[n] in alphabet:
            character = (alphabet.index(plaintext[n]) + key) % 26
            cipherletter = alphabet[character]

        elif plaintext[n] in capitalAlphabet:
            character = (capitalAlphabet.index(plaintext[n]) + key) % 26
            cipherletter = capitalAlphabet[character]

        else:
            cipherletter = plaintext[n]

        ciphertext = ciphertext + cipherletter

    print("ciphertext: " + ciphertext)


#Main Program

try:
    number = int(input(sys.argv[0] + " "))
    word = input("plaintext: ")


    if number > 0:
        caeser(word, number)

except ValueError:
    print("")
