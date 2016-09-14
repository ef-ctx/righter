import json
import re
import requests_cache
from righter import settings
from urllib.parse import quote_plus

session = requests_cache.CachedSession('whitesmoke', backend=settings.REQUESTS_CACHE_BACKEND)


def _convert_symbol(error_type, correction):
    replacements = [suggestion["replace"] for suggestion in correction["suggestions"] if "replace" in suggestion]
    if error_type == "spelling.1" and any(correction["word"].lower() == replacement.lower() for replacement in replacements):
        return "C"
    elif error_type.startswith("spelling"):
        return "SP"
    else:
        return {
            "grammar.12": "AR",
            "grammar.3": "C",
        }.get(error_type)


def _get_offset(text):
    for i, c in enumerate(text):
        if c != ' ':
            return i
    return len(text)


def check(text):
    text = re.sub(r'\s', ' ', text)
    offset = _get_offset(text)
    payload = json.dumps({
        "user_information": {"GUID": "1"},
        "writer": {"text": text},
        "action": "writer",
    })
    response = session.post('http://companion-api.whitesmoke.com/', data=payload)
    writer = json.loads(response.json()["params"]["writer"])
    changes = []
    for correction in writer["corrections"]:
        grouped_suggestions = {}
        for suggestion in correction["suggestions"]:
            error_type = "{}.{}".format(suggestion['type'], suggestion['explanationCode'])
            symbol = _convert_symbol(error_type, correction)
            if symbol in grouped_suggestions and "replace" in suggestion:
                grouped_suggestions[symbol]["suggestions"].append(suggestion["replace"])
            else:
                grouped_suggestions[symbol] = {
                    "selection": correction["word"],
                    "start": correction["fromPos"] + offset,
                    "originalSymbol": error_type,
                    "symbol": symbol,
                    "suggestions": [],
                }
                if "replace" in suggestion:
                    grouped_suggestions[symbol]["suggestions"].append(suggestion["replace"])
        changes.extend(grouped_suggestions.values())
    return changes
