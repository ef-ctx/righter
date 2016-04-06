import requests


TYPE_MAP = {
    3: 'AR',
    1: 'SP',
}


def check(text):
    """Given a text, query ginger API and return a list of dicts in the same
    format as righter.check"""
    changes = []

    url = 'https://services.gingersoftware.com/Ginger/correct/jsonSecured/GingerTheTextFull?apiKey=GingerWebSite&lang=US&clientVersion=2.0&text={}&_=1459928621895'
    response = requests.get(url.format(text)).json()
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

    return changes
