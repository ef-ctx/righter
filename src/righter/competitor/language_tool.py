import language_check

tool = language_check.LanguageTool('en-US')

DEFAULT_SYMBOL_CONVERSION = {
    'EN_A_VS_AN': 'AR',
    'MORFOLOGIK_RULE_EN_US': 'SP',
    'UPPERCASE_SENTENCE_START': 'C',
}

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
        symbol = _convert_symbol(text, match)
        if symbol:
            changes.append({
                "explanation": match.msg,
                "originalSymbol": match.ruleId,
                "selection": _get_selection(text, match),
                "start": match.offset,
                "suggestions": match.replacements,
                "symbol": symbol,
            })
    return changes
