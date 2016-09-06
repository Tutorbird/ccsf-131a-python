def palindrome(string):
    import re
    word_characters = re.sub('\W','',string.lower())
    word_reverse = word_characters[::-1]

    if word_reverse == word_characters:
        return True
    else:
        return False
