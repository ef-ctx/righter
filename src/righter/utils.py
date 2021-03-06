"""
Utilities for text analysis and parsing.
"""
import string
import unicodedata


def contains_digit(text):
    """
    Check if text contains any number.
    """
    for char in string.digits:
        if char in text:
            return True
    return False


def remove_punctuation(text, ignore=None):
    """
    Remove all punctiation from text
    """
    punctuation = string.punctuation
    if ignore:
        punctuation = punctuation.replace(ignore, "")
    for char in punctuation:
        text = text.replace(char, ' ')
    return text


def asciify(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').encode('ascii', 'ignore').decode('ascii')
