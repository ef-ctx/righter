import regex

from righter.competitor.wikipedia_typos import typos
from bs4 import BeautifulSoup


def _load_regexes():
    regexes = []
    soup = BeautifulSoup(typos, 'html.parser')
    for typo in soup.findAll("typo"):
        regexes.append(regex.compile(typo.attrs["find"]))
    return regexes


regexes = _load_regexes()


def check(text):
    changes = []
    for re in regexes:
        for match in re.finditer(text):
            start = match.start()
            if all(start != change['start'] for change in changes):
                changes.append({
                    'start': start,
                    'selection': text[start:match.end()]
                })
    return changes
