import re
import requests_cache
from urllib.parse import quote_plus

TYPE_MAP = {
    3: 'AR',
    1: 'SP',
}

session = requests_cache.CachedSession('ginger')


class SentenceTooBigError(Exception):
    pass


def split_sentences(text):
    """Splits text into sentences, whilist keeping all original punctuation.
    Thus this is the expected output:

        I have an elephant! Its name is Bob. -> ["I have an elephant!", "Its name is Bob."]
    """
    tokens = re.split(r'([.!?]+)', text)
    # If the last token is '' it means the last sentence ends in punctuation.
    # So we remove the uneeded empty string in the end. Otherwise, we add an
    # empty string so the for ... in zip(...) works later on.
    if tokens[-1] == '':
        tokens.pop()
    else:
        tokens.append('')
    sentences = []
    for sentence, punct in zip(tokens[::2], tokens[1::2]):
        sentences.append(sentence + punct)
    return sentences


def merge_sentences(sentences, max_size=600):
    """Merges phrases together up to max_size. If a sentence is too big
    SentenceTooBigError is raised"""
    result = []
    current = ''
    for sent in sentences:
        if len(sent) > max_size:
            raise SentenceTooBigError()
        new_sent = current + sent
        if len(new_sent) > max_size:
            result.append(current)
            current = sent
        else:
            current += sent
    result.append(current)
    return result


def _get_type(correction, text):
    word = _get_word(correction, text)
    type_ = TYPE_MAP.get(correction["Type"], "undefined")
    if type_ == 'SP' and any(c['Text'].lower() == word for c in correction['Suggestions']):
        type_ = 'C'
    return type_


def _get_word(correction, text):
    return text[correction["From"]:correction["To"] + 1]


def _get_suggestions(correction):
    if correction['Suggestions']:
        return [suggestion['Text'] for suggestion in correction['Suggestions']]
    return []


def check(text):
    """Given a text, query ginger API and return a list of dicts in the same
    format as righter.check"""
    url = 'https://services.gingersoftware.com/Ginger/correct/jsonSecured/GingerTheTextFull'
    # Ginger splits texts on sentences. So, if you have a really big
    # sentence, even ginger plugin will fail. It does make sense to split by
    # sentences because there are sentence-wide analysis that could be made.
    #
    # The largest sentence ginger can handle is 600 characters.
    offset = 0
    params = {
        "isOnTheFly": "false",
        "securedPage": "true",
        "apiKey": "BrowserStandalone",
        "lang": "US",
        "clientVersion": "0.1.0.562",
        "_": "1460102265093"
    }
    changes = []
    for sentence in merge_sentences(split_sentences(text)):
        params["text"] = sentence
        resp = session.get(url, params=params)
        resp.raise_for_status()
        response = resp.json()
        for correction in response["Corrections"]:
            change = {
                'selection': _get_word(correction, sentence),
                'start': correction['From'] + offset,
                'symbol': _get_type(correction, sentence),
                'originalSymbol': correction["Type"],
            }
            change['suggestions'] = _get_suggestions(correction)
            if change['suggestions']:
                change['correction'] = change['suggestions'][0]
            changes.append(change)
        offset += len(sentence)

    return changes
