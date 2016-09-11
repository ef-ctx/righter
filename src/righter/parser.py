import collections
import io
import json
import logging
import string
import sys

from lxml import etree

logger = logging.getLogger("righter")


class StateController:

    def __init__(self):
        self.writing = {}
        self.change = {}
        self.inside_writing = False
        self.inside_change = False
        self.writing_failed = False

    def _is_change_valid(self, change):
        if not change.get('symbol'):
            return False
        if change['symbol'] in ('SP', 'C', 'NSW'):
            required_keys = {'symbol', 'selection', 'start'}
            if required_keys - set(change.keys()):
                return False
        return True

    def start_writing(self, writing_id, level):
        self.writing_failed = False
        self.writing = {
            "id": writing_id,
            "level": level,
            "text": "",
            "changes": [],
        }
        self.inside_writing = True

    def set_nationality(self, nationality):
        self.writing['nationality'] = nationality

    def set_topic(self, topic):
        self.writing['topic'] = topic

    def set_grade(self, grade):
        self.writing["grade"] = grade

    def end_writing(self):
        self.inside_writing = False

    def start_change(self):
        self.inside_change = True
        self.change = {
            "start": self.offset
        }

    def end_change(self):
        self.inside_change = False
        self.update_text(self.change.get("selection"))
        # ignore changes without symbols (they are impossible to analyse
        # anyway)
        if self._is_change_valid(self.change):
            self.writing["changes"].append(self.change)

    def set_selection(self, selection):
        if selection:
            self.change["selection"] = selection

    def set_symbol(self, symbol):
        if symbol == 'NSW':
            symbol = 'SP'
        self.change["symbol"] = symbol
    
    def set_correct(self, correct):
        if correct:
            self.change["correct"] = correct

    @property
    def offset(self):
        return len(self.writing["text"])

    def _needs_space(self, a, b):
        if not a or not b:
            return False

        if any(map(a.endswith, string.punctuation)) and not any(map(b.startswith, string.whitespace)):
            return True
        elif not any(map(a.endswith, string.whitespace)):
            return not any(map(b.startswith, string.whitespace + string.punctuation))

        return False

    def update_text(self, text):
        if text:
            if self._needs_space(self.writing["text"], text):
                separator = ' '
            else:
                separator = ''
            self.writing["text"] += separator + text


def _parse_text(controller, blob):
    """Parses blob, extracted from text CDATA using XML Parser."""
    stream = io.BytesIO(blob.encode('utf8'))
    for event, element in etree.iterparse(stream, events=('start', 'end')):
        if element.tag == 'text' and event == 'start':
            controller.update_text(element.text)
        elif element.tag == 'change':
            if event == 'start':
                controller.start_change()
            else:
                controller.end_change()
                controller.update_text(element.tail)
        elif element.tag == 'selection' and event == 'end':
            controller.set_selection(element.text)
        elif element.tag == 'symbol' and event == 'end':
            controller.set_symbol(element.text)
        elif element.tag == 'correct' and event == 'end':
            controller.set_correct(element.text)
        elif element.tag == 'br' and event == 'end':
            if element.tail:
                controller.update_text('\n{}'.format(element.tail))
            else:
                controller.update_text('\n')
        elif not controller.inside_change and event == 'end':
            controller.update_text(element.tail)


def parse(xml_file):
    """Given a xml file-like object, returns a list of dicts with two keys:
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
                NSW - no such word
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
    for event, element in etree.iterparse(xml_file, events=('start', 'end')):
        if element.tag == 'writing':
            if event == 'start':
                controller.start_writing(element.get('id'), element.get('level'))
            else:
                controller.end_writing()
                if not controller.writing_failed:
                    yield controller.writing
                # keep etree from keeping the entire tree in memory
                element.clear()
        elif element.tag == 'learner' and event == 'end':
            if element.get('nationality'):
                controller.set_nationality(element.get('nationality'))
        elif element.tag == 'topic' and event == 'end':
            if element.get('id'):
                controller.set_topic(element.get('id'))
        elif element.tag == 'grade' and event == 'end':
            if element.text:
                try:
                    controller.set_grade(int(element.text))
                except ValueError:
                    pass
        elif element.tag == 'text' and event == 'end':
            try:
                _parse_text(controller, '<text>{}</text>'.format(element.text))
            except etree.XMLSyntaxError:
                logger.warn("Text for writing <%s> is invalid XML", controller.writing.get('id'))
                controller.writing_failed = True
