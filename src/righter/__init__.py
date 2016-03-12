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
    text = utils.asciify(original_text)
    text = utils.remove_punctuation(text)
    words = text.split()
    response = []
    for word in words:
        if not dictionary.is_english_word(word.lower(), lower=True) and\
           not utils.contains_digit(word) and\
           not dictionary.is_name(word):
            for pos in findall(word, text):
                item = {
                    "selection": original_text[pos: (pos + len(word))],
                    "start": pos
                }
                if item not in response:
                    response.append(item)
    return response


def preceded_by_breakline(sentence, pos):
    while pos > 0:
        previous_pos = pos - 1
        if sentence[previous_pos] == "\n":
            return True
        elif sentence[previous_pos] == " ":
            pos = previous_pos
        else:
            return False
    return False


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
    sentences = re.split('[!?.]+', text)  # TODO: add \n
    pos = 0
    for sentence in sentences:
        clean_sentence = sentence.strip()
        clean_sentence = utils.remove_punctuation(clean_sentence, ignore="'")
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
                if (word == word.capitalize() and not must_be_capital):
                    if dictionary.is_english_word(word.lower()) and\
                       not preceded_by_breakline(sentence, relative_pos):
                        item = {
                            "selection": word,
                            "start": pos + relative_pos
                        }
                        response.append(item)
                elif (word != word.capitalize() and must_be_capital):
                    item = {
                        "selection": word,
                        "start": pos + relative_pos
                    }
                    response.append(item)
                relative_pos += (len(word))
                        
            pos += len(sentence) + 1
    return response


def check_article(text):
    mistakes_list = []
    a_before_vowel = r"(\b[aA]\b) [aeiouAEIOU][a-zA-Z]+"
    mistake = re.search(a_before_vowel, text)
    if mistake:
        pos = mistake.start()
        word = text[pos:].split()[0]
        item = {
            "selection": word,
            "start": pos
        }
        mistakes_list.append(item)

    an_before_consonant = r"(\b[aA]n\b) [bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ][a-zA-Z]+"   
    mistake = re.search(an_before_consonant, text)
    if mistake:
        pos = mistake.start()
        word = text[pos:].split()[0]
        item = {
            "selection": word,
            "start": pos
        }
        mistakes_list.append(item)
    return mistakes_list


def check(text):
    changes = []

    for change in check_capitalization(text):
        change['symbol'] = 'C'
        changes.append(change)

    for change in check_spelling(text):
        change['symbol'] = 'SP'
        changes.append(change)

    for change in check_article(text):
        change['symbol'] = 'AR'
        changes.append(change)

    return changes
