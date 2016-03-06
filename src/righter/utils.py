"""
Utilities for text analysis and parsing.
"""
import string


def contains_digit(text):
    """
    Check if text contains any number.
    """
    for char in string.digits:
        if char in text:
            return True
    return False


def remove_punctuation(text):
    """
    Remove all punctiation from text
    """
    for char in string.punctuation:
        text = text.replace(char, ' ')
    return text

