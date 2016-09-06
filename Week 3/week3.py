#!/usr/local/bin/python3
# Name: Nestor Alvarez
# File: week3.py
# Desc: Exercises

# Create a list of lc letters the hard way with with a list comprehension, chr(), range(),
# and a knowledge of the numbers of the ASCII lowercase letters.

#Dictionaries
lowercase_letters = [chr(i) for i in range(97, 123)]

alphabet_dict = {}
ALPHABET_RANGE = 26

for i in range(0, ALPHABET_RANGE):
    alphabet_dict[lowercase_letters[i]] = lowercase_letters[i].upper()

print(list(alphabet_dict.values()))
print(sorted(alphabet_dict.keys()))
print(sorted(alphabet_dict.values()))
print(alphabet_dict)

i = 0
sorted_alphabet = sorted(alphabet_dict.keys())
sorted_alphabet.reverse()

while i < ALPHABET_RANGE:
    print("{}:{}".format(sorted_alphabet[i], alphabet_dict[sorted_alphabet[i]]))
    i = i + 1
else:
    pass

i = 0


#Control Flow
sorted_alphabet.reverse()
while i < ALPHABET_RANGE:
    if i % 2 == 0:
        print(alphabet_dict[sorted_alphabet[i]])
        i = i + 1
    else:
        i = i + 1
else:
    pass

i = 0
while i < ALPHABET_RANGE:
    if i % 11 == 0:
        print("{:>3} {:^20} {:>11}".format(ord(sorted_alphabet[i]), sorted_alphabet[i], sorted_alphabet[i]*11, sep = '\t'))
        i = i + 1
    elif i % 7 == 0:
        print("{:>3} {:^20} {:>11}".format(ord(sorted_alphabet[i]), sorted_alphabet[i], sorted_alphabet[i]*7, sep = '\t'))
        i = i + 1
    elif i % 5 == 0:
        print("{:>3} {:^20} {:>11}".format(ord(sorted_alphabet[i]), sorted_alphabet[i], sorted_alphabet[i]*5, sep = '\t'))
        i = i + 1
    elif i % 3 == 0:
        print("{:>3} {:^20} {:>11}".format(ord(sorted_alphabet[i]), sorted_alphabet[i], sorted_alphabet[i]*3, sep = '\t'))
        i = i + 1
    else:
        print("{:>3} {:^20} {:>11}".format(ord(sorted_alphabet[i]), sorted_alphabet[i], sorted_alphabet[i], sep = '\t'))
        i = i + 1
else:
    pass

#Palindrome
def palindrome(string):
    import re
    word_characters = re.sub('\W','',string.lower())
    word_reverse = word_characters[::-1]

    if word_reverse == word_characters:
        return True
    else:
        return False
    
#Count_Words

def count_words(string):
    import re
    tmp = {}
    words = re.split('\W+',string.lower())

    for i in words:
        if i not in tmp:
            tmp[i] = 1
        else:
            tmp[i] = tmp[i] + 1
                

    return tmp

