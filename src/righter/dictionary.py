"""
English words & other dictionary-based.
"""
from righter import utils


EN_GB_WORDS_PATH = "data/british-english-insane.txt"
EN_US_WORDS_PATH = "data/american-english-insane.txt"
WORDS_FILEPATHS = [EN_GB_WORDS_PATH, EN_US_WORDS_PATH]

ABBREV_PATH = "data/abbreviations.txt"


def _build_word_list():
    """
    Builds a set of valid English words.
    """
    all_words = set()
    for filepath in WORDS_FILEPATHS:
        with open(filepath) as words_file:
            some_words = [word.strip() for word in words_file.readlines()]
            all_words |= set(some_words)
    return all_words


def _build_abbreviations_list():
    """
    Builds a set of valid English abbreviations.
    """
    all_abbrevs = set()
    with open(ABBREV_PATH) as abbrev_file:
        for line in abbrev_file.readlines():
            abbrevs = line.split("-")[0]
            some_abbrevs = []
            for abbrev in abbrevs.split("/"):
                abbrev = utils.remove_punctuation(abbrev.strip())
                abbrev = abbrev.replace(" ", "")
                some_abbrevs.append(abbrev)
            all_abbrevs |= set(some_abbrevs)
    return all_abbrevs


WORDS = _build_word_list()
ABBREVIATIONS = _build_abbreviations_list()


def is_english_abbreviation(text):
    """
    Return True if given string is a valid English abbreviation.
    """
    return text in ABBREVIATIONS


def is_english_word(text):
    """
    Return True if given string is a valid English word.
    """
    return is_english_abbreviation(text) or (text in WORDS)
