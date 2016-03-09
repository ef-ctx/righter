"""
Identifies common English writing mistakes
"""
import re
import unicodedata
from righter import dictionary
from righter import utils


def check_spelling(text):
    """
    Check if a text has spelling errors.
    Return a list with objects:
        {
            "selection": <wrong-spelled-word>,
            "start": <position-of-the-first-character-in-string>
        }
    """
    text = text.lower()
    text = utils.remove_punctuation(text)
    words = text.split()
    response = []
    for word in words:
        if not dictionary.is_english_word(word) and\
           not utils.contains_digit(word):
            item = {
                "selection": word,
                "start": text.find(word)
            }
            response.append(item)
    return response


def check_capitalization(text):
    """
    Check if a text has spelling errors.
    Return a list with objects:
        {
            "selection": <wrong-capitalized-word>,
            "start": <position-of-the-first-character-in-string>
        }
    """
    response = []
    sentences = re.split('[!?.]', text)  # TODO: add \n
    pos = 0
    for sentence in sentences:
        clean_sentence = sentence.strip()
        if not clean_sentence:
            continue
        # Check if first character is capital
        if clean_sentence[0].islower():
            first_word = clean_sentence.split()[0]
            first_word_position = pos + sentence.find(first_word)
            item = {
                "selection": first_word,
                "start": first_word_position
            }
            response.append(item)
        else:
            # check if a common English word in the middle of the text is
            # wrongly capitalized
            words = clean_sentence.split()
            for word in words[1:]:
                if word[0].isupper() and\
                   dictionary.is_english_word(word.lower()):
                    item = {
                        "selection": word,
                        "start": text.find(word)
                    }
                    response.append(item)
        pos += len(sentence) + 1
    return response


def check(text):
    changes = []

    for change in check_capitalization(text):
        change['symbol'] = 'C'
        changes.append(change)

    for change in check_spelling(text):
        change['symbol'] = 'SP'
        changes.append(change)

    return changes
