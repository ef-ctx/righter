"""
Identifies common English writing mistakes
"""
import unicodedata
from righter import dictionary
from righter import utils


def check_spelling(text):
    """
    Check if a text has spelling errors.
    Return a list with objects:
        {
            "selection": <wrong-spelled-word>,
            "start": <first-character-position-in-string>
        }
    """
    text = text.lower()
    text = utils.remove_punctuation(text)
    words = text.split()
    response = []
    for word in words:
        if not dictionary.is_english_word(word) and not utils.contains_digit(word):
            item = {
                "selection": word,
                "start": text.find(word)
            }
            response.append(item)
    return response
