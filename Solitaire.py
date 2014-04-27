__author__ = 'anthonylim'


# Anthony Lim
# alim4@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 3
#
# Solitaire encryption

def main():
    deck = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12'

    flag = get_input()
    while flag != 'e' and flag != 'd':
        flag = get_input()

    message = raw_input("What is your message? ")
    deck = raw_input("What is the initial deck? ")

    if flag == 'e':
        encrypt_message(message, deck)
    if flag == 'd':
        decrypt_message(message, deck)

    return 0

def get_input():
    input = raw_input('Encrypt (e) or decrypt (d)?: ')
    flag = ''
    if input == 'e':
        flag = 'e'
    elif input == 'd':
        flag = 'd'
    else:
        print 'INVALID INPUT. Try again.'
        flag = 'n'

    return flag

def encrypt_message (msg, deck):
    return

def decrypt_message (msg, deck):
    return

# Convert a CHARACTER to an ASCII INTEGER
def convert_char_to_val(char):
    c = ''
    base = 'a'
    if char.islower():
        c = ord(char) - ord(base) + 1
    elif char.isupper():
        c = ((ord('A') - ord('a')) % 26) + 7

    return int(c)

# Convert an ASCII INTEGER value to a CHARACTER
def convert_val_to_char(val):
    base = 'a'
    v = ''
    if val < 27:
        v = chr(val + ord(base) - 1)
    else:
        v = chr(val + ord(base) - 59)

    return v


main()