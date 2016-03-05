"""
English words & other dictionary-based.
"""
EN_GB_WORDS_PATH = "data/british-english-insane.txt"
EN_US_WORDS_PATH = "data/american-english-insane.txt"

FILEPATHS = [EN_GB_WORDS_PATH, EN_US_WORDS_PATH]


def _build_word_list():
    """
    Builds a list of valid English words.
    """
    all_words = set()
    for filepath in FILEPATHS:
        with open(filepath) as words_file:
            some_words = [word.strip() for word in words_file.readlines()]
            all_words |= set(some_words)
    return all_words


WORDS = _build_word_list()
