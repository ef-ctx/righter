import language_check

tool = language_check.LanguageTool('en-US')

DEFAULT_SYMBOL_CONVERSION = {
    'EN_A_VS_AN': 'AR',
    'MORFOLOGIK_RULE_EN_US': 'SP',
    'UPPERCASE_SENTENCE_START': 'C',
}

# Mistakes that are not mapped on our annotated data
IGNORE_RULES = [
    "EN_UNPAIRED_BRACKETS"
]


def _get_selection(text, match):
    start = match.offset
    end = match.offset + match.errorlength
    return text[start:end]


def _convert_symbol(text, match):
    symbol = DEFAULT_SYMBOL_CONVERSION.get(match.ruleId)
    if symbol == 'SP':
        error = _get_selection(text, match)
        if any(error.lower() == replacement.lower() for replacement in match.replacements):
            return 'C'
    return symbol


def check(text):
    changes = []
    for match in tool.check(text):
        if match.ruleId not in IGNORE_RULES:
            symbol = _convert_symbol(text, match)
            change = {
                "explanation": match.msg,
                "originalSymbol": match.ruleId,
                "selection": _get_selection(text, match),
                "start": match.offset,
                "suggestions": match.replacements,
            }
            if symbol:
                change["symbol"] = symbol
            changes.append(change)
    return changes
