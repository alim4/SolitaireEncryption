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
    result = []

    print convert_char_to_val('z')
    print convert_char_to_val('c')
    print convert_val_to_char(convert_char_to_val('Y') + convert_char_to_val('c'))
    print convert_val_to_char(1)

    flag = get_input()
    while flag != 'e' and flag != 'd':
        flag = get_input()

    message = raw_input("What is your message? ")
    deck = raw_input("What is the initial deck? ")

    if flag == 'e':
        result = encrypt_message(message, deck)
    if flag == 'd':
        result = decrypt_message(message, deck)

    print result

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

def encrypt_message(msg, deck):
    result = []
    for i in range(msg.__len__()):
        if msg[i].isspace() or msg[i].isdigit():
            continue
        aa = convert_char_to_val(msg[i])
        bb = convert_char_to_val(deck[i])
        print ("msg: {0} | deck: {1}".format(aa, bb))
        temp = convert_val_to_char((convert_char_to_val(msg[i]) + convert_char_to_val(deck[i])) % 52)
        result.append(temp)

    return result

def decrypt_message(msg, deck):
    result = []
    for i in range(msg.__len__()):
        if msg[i].isspace() or msg[i].isdigit():
            continue
        aa = convert_char_to_val(msg[i])
        bb = convert_char_to_val(deck[i])
        print ("msg: {0} | deck: {1}".format(aa, bb))
        temp = convert_val_to_char((convert_char_to_val(msg[i]) - convert_char_to_val(deck[i])) % 52)
        result.append(temp)

    return result

# Convert a CHARACTER to an ASCII INTEGER
def convert_char_to_val(char):
    c = ''
    base = 'a'
    if char.islower():
        c = ord(char) - ord(base) + 1
    elif char.isupper():
        c = ((ord(char) - ord(base)) % 52) + 7

    return int(c)

# Convert an ASCII INTEGER value to a CHARACTER
def convert_val_to_char(val):
    base = 'a'

    if 26 < val <= 52:
        v = chr((val % 53) + ord('a') - 59)
    else:
        v = chr((val % 52) + ord('a') - 1)


    return v


main()