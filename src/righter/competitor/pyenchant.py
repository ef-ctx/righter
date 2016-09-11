import enchant
from enchant.checker import SpellChecker


def check(original_text):
    """
    Check spelling using whichever broker was set initially.
    """
    response = []
    checker = SpellChecker("en_US")
    checker.set_text(original_text)
    for error in checker:
        suggestions = error.suggest()
        item = {
            "selection": error.word,
            "start": error.wordpos,
            "suggestions": suggestions,
        }
        if suggestions and suggestions[0].lower() == error.word.lower():
            item["symbol"] = "C"
        else:
            item["symbol"] = "SP"
        response.append(item)
    return response


def check_hunspell(original_text):
    """cd ..
    Set pyenchant broker to Hunspell (default)
    """
    # although the name "myspell", this is Hunspell
    broker = enchant.Broker()
    broker.set_ordering("en_US","myspell")
    return check(original_text)


def check_aspell(original_text):
    """
    Set pyenchant broker to Aspell
    """
    broker = enchant.Broker()
    broker.set_ordering("en_US","aspell")
    return check(original_text)


if __name__ == "__main__":
    text = "the book is on an tabel. and it came too europe last monday.\nJulia has lots of friend, she is happy yesterday."
    print(check_hunspell(text))
