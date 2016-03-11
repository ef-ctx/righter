"""
Identifies common English writing mistakes
"""
import re
import unicodedata
from righter import dictionary
from righter import utils


def findall(sub, string):
    """
    >>> text = "Allowed Hello Hollow"
    >>> tuple(findall('ll', text))
    (1, 10, 16)
    """
    index = 0 - len(sub)
    try:
        while True:
            index = string.index(sub, index + len(sub))
            yield index
    except ValueError:
        pass


def check_spelling(original_text):
    """
    Check if a text has spelling errors.
    Return a list with objects:
        {
            "selection": <wrong-spelled-word>,
            "start": <position-of-the-first-character-in-string>
        }
    """
    text = original_text.lower()
    text = text.replace("’", "'")
    text = utils.remove_punctuation(text)
    words = text.split()
    response = []
    for word in words:
        if not dictionary.is_english_word(word) and\
           not utils.contains_digit(word):
            for pos in findall(word, text):
                item = {
                    "selection": original_text[pos: (pos + len(word))],
                    "start": pos
                }
                if item not in response:
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
        clean_sentence = utils.remove_punctuation(clean_sentence)
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

        # check if a common English word in the middle of the text is
        # wrongly capitalized
        words = clean_sentence.split()
        if words:
            relative_sentence = sentence
            relative_pos = sentence.find(words[0]) + len(words[0])
            relative_sentence = sentence[relative_pos:]
            for word in words[1:]:
                relative_pos += relative_sentence.find(word)
                relative_sentence = sentence[relative_pos + len(word):]
                must_be_capital = dictionary.is_capital_word(word)
                if (word[0].isupper() and not must_be_capital):
                    if dictionary.is_english_word(word.lower()):
                        item = {
                            "selection": word,
                            "start": pos + relative_pos
                        }
                        response.append(item)
                elif (word[0].islower() and must_be_capital):
                    item = {
                        "selection": word,
                        "start": pos + relative_pos
                    }
                    response.append(item)
                relative_pos += (len(word))
                        
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
