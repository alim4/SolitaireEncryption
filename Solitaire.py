__author__ = 'anthonylim'


# Anthony Lim
# alim4@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 3
#
# Solitaire encryption

def main():
    # deck = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12"
    result = []

    flag = get_input()
    while flag != 'e' and flag != 'd':
        flag = get_input()

    message = raw_input("What is your message? ")
    deck = raw_input("What is the initial deck? ")

    if flag == 'e':
        result = encrypt_message(message, deck)
    if flag == 'd':
        result = decrypt_message(message, deck)

    print "Result: {0}".format(''.join(result))

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
            result.append(" ")
            continue
        # Choose correct deck index to use as cipher
        deck = shuffle(deck)
        shift = convert_char_to_val(deck[0])

        #print shift
        #print "deck shift: " + deck[shift + 1]
        enc_ltr = encrypt_letter(msg[i], deck[(shift+1) % deck.__len__()])
        result.append(enc_ltr)

    return result

def decrypt_message(msg, deck):
    result = []
    for i in range(msg.__len__()):
        if msg[i].isspace() or msg[i].isdigit():
            result.append(" ")
            continue
        # Choose correct deck index to use as cipher
        deck = shuffle(deck)
        print deck[0]
        shift = convert_char_to_val(deck[0])

        #print shift
        #print "deck shift: " + deck[shift + 1]
        enc_ltr = decrypt_letter(msg[i], deck[(shift+1) % deck.__len__()])
        result.append(enc_ltr)

    return result

def encrypt_letter(ltr, key):
    '''
    Works on per letter basis
    Returns a letter with given offset based on key
    '''
    offset = convert_char_to_val(key)
    letter = convert_char_to_val(ltr)
    enc_ltr = convert_val_to_char((letter + offset) % 52)
    return enc_ltr

def decrypt_letter(ltr, key):
    '''
    Works on per letter basis
    Returns a decrypted letter
    '''
    offset = convert_char_to_val(key)
    letter = convert_char_to_val(ltr)
    dec_ltr = convert_val_to_char((letter - offset) % 52)
    return dec_ltr

def shuffle(deck):
    '''
    Given the deck, shuffles using the Solitaire algorithm
    Returns the shuffled deck
    '''
    # Find first Joker (1), find next index
    joker_i = deck.index('1')
    next_i = joker_i + 1

    # Swap
    mydeck = list(deck)

    # If joker is in last index in deck
    if joker_i == deck.__len__()-1:
        mydeck = swap(mydeck, joker_i, 1)
    else:
        mydeck = swap(mydeck, joker_i, next_i)

    # print "Joker 1: \t" + ''.join(mydeck)

    # Move second joker down two places
    joker_i2 = mydeck.index('2')
    next_i2 = (joker_i2 + 2) % deck.__len__()

    if joker_i2 > deck.__len__()-2:
        mydeck = swap(mydeck, joker_i2, 1)
    else:
        # If 2 is last index
        if next_i2 == 0:
            mydeck.insert(1, mydeck.pop(joker_i2))
            #mydeck = swap(mydeck, joker_i2, 1)
        # If 2 is second to last index
        # elif next_i2 == 1:
        #     mydeck = swap(mydeck, joker_i2, 1)
        else:
            #mydeck = swap(mydeck, joker_i2, next_i2)
            mydeck.insert(next_i2, mydeck.pop(joker_i2))

    # print "Joker 2: \t" + ''.join(mydeck)

    # Triple Cut
    # Find first instance of a joker to determine
    # where to cut and in what order
    for i in mydeck:
        if i == '1':
            first = '1'
            second = '2'
            break
        elif i == '2':
            first = '2'
            second = '1'
            break

    right = mydeck[mydeck.index(second)+1:mydeck.__len__()]
    mydeck[mydeck.index(second)+1:mydeck.__len__()] = mydeck[0:mydeck.index(first)]
    mydeck[0:mydeck.index(first)] = right

    # print "Triple cut: " + ''.join(mydeck)

    # Shift top
    if mydeck[-1] != '1' and mydeck[-1] != '2':
        num_to_shift = convert_char_to_val(mydeck[-1])
        len = mydeck.__len__() - 1
        last_char = list(mydeck[-1])
        shift = mydeck[0:num_to_shift]
        left_side = mydeck[num_to_shift:len]

        mydeck = left_side + shift + last_char

    # print "Shift top: \t" + ''.join(mydeck)
    # print("")

    return ''.join(mydeck)

def swap(text, i, j):
    text[i], text[j] = text[j], text[i]
    return list(''.join(text))

# Convert a CHARACTER to an ASCII INTEGER
def convert_char_to_val(char):
    base = 'a'

    if char == '1':
        return 53
    if char == '2':
        return 54

    if char.islower():
        c = ord(char) - ord(base) + 1
    else:
        c = ((ord(char) - ord(base)) % 52) + 7

    return c

# Convert an ASCII INTEGER value to a CHARACTER
def convert_val_to_char(val):
    base = 'a'
    val %= 53

    if 26 < val <= 52:
        v = chr(ord(base) + val - 59)
    else:
        v = chr(ord(base) + val - 1)

    return v


main()