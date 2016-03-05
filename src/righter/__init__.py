"""
Identifies common English writing mistakes
"""
import string
import unicodedata
from righter import dictionary


def contains_digit(text):
    """
    """
    for c in string.digits:
        if c in text:
            return True
    return False


def remove_punctuation(text):
    """Remove all punctiation from text"""
    for c in string.punctuation:
        text = text.replace(c, ' ')
    return text


def check_spelling(text):
    """
    """
    text = text.lower()
    text = remove_punctuation(text)
    words = text.split()
    response = []
    for word in words:
        if word not in dictionary.WORDS and not contains_digit(word):
            response.append(word)
    return response
