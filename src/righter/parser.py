import sys

from lxml import etree


class StateController:

    def __init__(self):
        self.writing = {}
        self.change = {}
        self.inside_writing = False
        self.inside_change = False

    def start_writing(self):
        self.writing = {
            "text": "",
            "changes": [],
        }
        self.inside_writing = True

    def end_writing(self):
        self.inside_writing = False

    def start_change(self):
        self.inside_change = True
        self.change = {
            "start": self.offset
        }

    def end_change(self):
        self.inside_change = False
        self.writing["changes"].append(self.change)
        self.writing["text"] += self.change.get("selection", "") or ""

    def set_selection(self, selection):
        self.change["selection"] = selection

    def set_symbol(self, symbol):
        self.change["symbol"] = symbol
    
    def set_correct(self, correct):
        self.change["correct"] = correct

    @property
    def offset(self):
        return len(self.writing["text"])

    def update_text(self, text):
        if text:
            self.writing["text"] += text


def parse(xml_file_name):
    """Given a xml_file_name, returns a list of dicts with two keys:
        - text: original student writing
        - changes: list of dicts with the fields:
            - symbol: error type, according to the list
                x>>y - change from x to y
                AG - agreement
                AR - article
                CO - combine sentences
                C - capitalization
                D - delete
                EX - expression of idiom
                HL - highlight
                I(x) - insert x
                MW - missing word
                NS - new sentence
                NWS - no such word
                PH - phraseology
                PL - plural
                PO - possessive
                PR - preposition
                PS - part of speech
                PU - punctuation
                SI - singular
                SP - spelling
                VT - verb tense
                WC - word choice
                WO - word order
            - selection: excerpt of the original text
            - start: indice where the word is in the text (in unicode characters)
            - correct: if this field exists it is the teacher suggested correction
    """
    controller = StateController()
    writings = []
    with open(xml_file_name, 'rb') as fp:
        for event, element in etree.iterparse(fp, events=('start', 'end')):
            if element.tag == 'writing':
                if event == 'start':
                    controller.start_writing()
                elif event == 'end':
                    controller.end_writing()
                    writings.append(controller.writing)
            elif element.tag == 'text':
                if event == 'start':
                    controller.update_text(element.text)
                elif event == 'end':
                    children = element.getchildren()
            elif element.tag == 'change':
                if event == 'start':
                    controller.start_change()
                elif event == 'end':
                    controller.end_change()
                    controller.update_text(element.tail)
            elif element.tag == 'selection' and event == 'end':
                if element.text:
                    controller.set_selection(element.text)
            elif element.tag == 'symbol' and event == 'end':
                controller.set_symbol(element.text)
            elif element.tag == 'correct' and event == 'end':
                if element.text:
                    controller.set_correct(element.text)
            elif controller.inside_writing and not controller.inside_change:
                if event == 'end':
                    controller.update_text(element.tail)
    return writings


if __name__ == '__main__':
    writings = parse(sys.argv[1])
    print([w for w in writings if w['changes'] and 'SP' in [change['symbol'] for change in w['changes']]][1])
