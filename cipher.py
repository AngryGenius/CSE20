# assignment: programming assignment 4
# author: Reed Warren
# date: 11/30/2020
# file: cipher.py is a program that encodes and decodes text.
# input: File text
# output: Either encoded data or decoded text.

# read text from a file and return text as a string
def readfile():
    reading = input('Please enter a file for reading:\n')
    f1 = open(f'{reading}', "r+")
    message = to_string(f1.read())
    f1.close()
    return message


# write a string (message) to a file
def writefile(message):
    writing = input('Please enter a file for writing:\n\n')
    f1 = open(f'{writing}', "w+")
    f1.write(to_string(message))
    f1.close()


# make a list (tuple) of letters in the English alphabet
def make_alphabet():
    alphabet = ()
    for i in range(26):
        char = i + 65
        alphabet += (chr(char),)
    # print (alphabet)
    return alphabet


# encode text letter by letter using a Caesar cipher
# return a list of encoded symbols
def encode(plaintext):
    plaintext = plaintext.upper()
    shift = 3
    ciphertext = []
    alphabet = make_alphabet()
    length = len(alphabet)
    for char in plaintext:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % length]
                ciphertext.append(letter)
                found = True
                break
        if not found:
            ciphertext.append(char)
    return ciphertext


# decode text letter by letter using a Caesar cipher
# return a list of decoded symbols
# check how the function encode() is implemented
# your implementation of the function decode() can be very similar
# to the implementation of the function encode()
def decode(ciphertext):
    ciphertext = ciphertext.upper()
    shift = -3
    plaintext = []
    alphabet = make_alphabet()
    length = len(alphabet)
    for char in ciphertext:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % length]
                plaintext.append(letter)
                found = True
                break
        if not found:
            plaintext.append(char)
    return plaintext


# convert a list into a string
# for example, the list ["A", "B", "C"] to the string "ABC" or
# the list ["H", "O", "W", " ", "A", "R", "E", " ", "Y", "O", "U", "?"] to the string "HOW ARE YOU?"
def to_string(text):
    s = ""
    for i in text:
        s += str(i)
    return s


# main program
done = False
while not done:
    operation = str(input("Would you like to encode or decode the message?\n" +
                          "Type E to encode, D to decode, or Q to quit:\n"))

    if operation == 'Q' or operation == 'q':
        done = True
    elif operation == 'E' or operation == 'e':
        try:
            read = readfile()
        except:
            print('invalid file!')
            continue
        ded_txt = to_string(encode(read))
        writefile(ded_txt)
        print('Plaintext:\n' + read)
        print('Ciphertext:\n' + ded_txt)
    elif operation == 'D' or operation == 'd':
        try:
            read = readfile()
        except:
            print('invalid file!')
            continue
        ded_txt = to_string(decode(read))
        writefile(ded_txt)
        print('Ciphertext:\n' + read)
        print('Plaintext:\n' + ded_txt)
    else:
        print('Not a valid operation!')
print('Goodbye!')
