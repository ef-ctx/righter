"""
English words & other dictionary-based.
"""
from righter import utils


#EN_GB_WORDS_PATH = "data/british-english-insane.txt"
#EN_US_WORDS_PATH = "data/american-english-insane.txt"
EN_GB_WORDS_PATH = "data/british-english-huge.txt"
EN_US_WORDS_PATH = "data/american-english-huge.txt"
LANGUAGES_PATH = "data/languages.txt"
WORDS_FILEPATHS = [EN_GB_WORDS_PATH, EN_US_WORDS_PATH]
#WORDS_FILEPATHS = ["/usr/share/dict/words"]

NAME_PATH = "data/names.txt"

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


def _build_languages_list():
    all_words = set()
    with open(LANGUAGES_PATH) as words_file:
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


def _build_names_list():
    """
    Builds a set of names
    """
    all_names = set()
    with open(NAME_PATH) as name_file:
        for line in name_file.readlines():
            all_names.add(utils.asciify(line.strip()))
    return all_names


WORDS = _build_word_list()
WORDS_LOWER = {word.lower() for word in WORDS}
ABBREVIATIONS = _build_abbreviations_list()
LANGUAGES = _build_languages_list()
NAMES = _build_names_list()
NAMES_LOWER = {name.lower() for name in NAMES}


def is_name(text):
    return utils.asciify(text.strip()) in NAMES.union({"USA"})


def is_english_abbreviation(text):
    """
    Return True if given string is a valid English abbreviation.
    """
    return text in ABBREVIATIONS


def is_contraction(text):
    """
    Return True if given string is part of a contraction
    """
    return text in ["ll", "ve"]
    

def is_english_word(text, lower=False):
    """
    Return True if given string is a valid English word.
    """
    if lower:
        words = WORDS_LOWER
    else:
        words = WORDS
    return is_english_abbreviation(text) or (text in words) or is_contraction(text)


def is_capital_word(text):
    text = text.lower()
    is_first_person = text in ["i", "i'm", "i'll", "i've", "i'd"]
    is_weekday = text in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    is_month = text in ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    is_language = text.title() in LANGUAGES
    is_country = text in ["china", "brazil", "usa"]
    is_name = text in NAMES_LOWER
    return is_first_person or is_weekday or is_month or is_language or is_country or is_name
