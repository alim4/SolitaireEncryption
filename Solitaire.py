__author__ = 'anthonylim'


# Anthony Lim
# alim4@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 3
#
# Solitaire encryption

def main():
    deck = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12"
    result = []

    print deck
    print shuffle(deck)

    print("")
    # print convert_char_to_val('z')
    # print convert_char_to_val('c')
    # print convert_val_to_char(convert_char_to_val('Y') + convert_char_to_val('c'))
    # print convert_val_to_char(1)

    flag = get_input()
    while flag != 'e' and flag != 'd':
        flag = get_input()

    message = raw_input("What is your message? ")
    #deck = raw_input("What is the initial deck? ")
    print deck

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

def shuffle(deck):
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
            mydeck = swap(mydeck, joker_i2, next_i2)

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

    # Shift top
    print convert_char_to_val(mydeck[-1])

    if mydeck[-1] != '1' and mydeck[-1] != '2':
        num_to_shift = convert_char_to_val(mydeck[-1])
        len = mydeck.__len__() - 1
        last_char = list(mydeck[-1])
        shift = mydeck[0:num_to_shift]
        left_side = mydeck[num_to_shift:len]

        mydeck = left_side + shift + last_char

    return ''.join(mydeck)

def swap(text, i, j):
    text[i], text[j] = text[j], text[i]
    return list(''.join(text))

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