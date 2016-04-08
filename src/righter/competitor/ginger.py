import requests
from urllib.parse import quote_plus


TYPE_MAP = {
    3: 'AR',
    1: 'SP',
}


class HTTPError(Exception):
    pass


def check(text):
    """Given a text, query ginger API and return a list of dicts in the same
    format as righter.check"""
    changes = []

    url = 'https://services.gingersoftware.com/Ginger/correct/jsonSecured/GingerTheTextFull'
    params = {
        "text": text,
        "isOnTheFly": "false",
        "securedPage": "true",
        "apiKey": "BrowserStandalone",
        "lang": "US",
        "clientVersion": "0.1.0.562",
        "_": "1460102265093"
    }
    # Ginger usually splits texts on sentences. So, if you have a really big
    # sentence, even ginger plugin will fail. It does make sense to split by
    # sentences because there are sentence-wide analysis that could be made.
    resp = requests.get(url, params=params)
    if not resp.ok:
        raise HTTPError()
    response = resp.json()
    try:
        for correction in response["Corrections"]:
            change = {}
            type_ = TYPE_MAP[correction["Type"]]
            word = text[correction["From"]:correction["To"] + 1]
            if type_ == 'SP' and any(c['Text'].lower() == word for c in correction['Suggestions']):
                type_ = 'C'
            change = {
                'selection': word,
                'start': correction['From'],
                'symbol': type_,
            }
            if correction['Suggestions']:
                change['correction'] = correction['Suggestions'][0]['Text']
            changes.append(change)
    except:
        import pdb; pdb.set_trace()
        raise

    return changes
