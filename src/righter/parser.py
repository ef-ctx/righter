import json
import sys
import io
import logging
import collections

from lxml import etree

logger = logging.getLogger("righter")


class StateController:

    def __init__(self):
        self.writing = {}
        self.change = {}
        self.inside_writing = False
        self.inside_change = False
        self.writing_failed = False

    def are_changes_correct(self):
        for change in self.writing['changes']:
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
        self.writing["changes"].append(self.change)
        self.writing["text"] += self.change.get("selection", "") or ""

    def set_selection(self, selection):
        if selection:
            self.change["selection"] = selection

    def set_symbol(self, symbol):
        self.change["symbol"] = symbol
    
    def set_correct(self, correct):
        if correct:
            self.change["correct"] = correct

    @property
    def offset(self):
        return len(self.writing["text"])

    def update_text(self, text):
        if text:
            self.writing["text"] += text


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
                if element.tail:
                    controller.update_text(' {}'.format(element.tail))
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
            if element.tail:
                controller.update_text(' {}'.format(element.tail))


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
    for event, element in etree.iterparse(xml_file, events=('start', 'end')):
        if element.tag == 'writing':
            if event == 'start':
                controller.start_writing(element.get('id'), element.get('level'))
            else:
                controller.end_writing()
                if not controller.writing_failed and controller.are_changes_correct():
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


if __name__ == '__main__':
    writings = parse(sys.argv[1])
    stats = collections.defaultdict(lambda: 0)
    total = 0
    total_with_changes = 0
    with open(sys.argv[2], 'w') as output_fp:
        for w in writings:
            print(json.dumps(w), file=output_fp)
            if w['changes']:
                total_with_changes += 1
                for change in w['changes']:
                    stats[change['symbol']] += 1
            total += 1
        for key, value in sorted(stats.items(), key=lambda x: x[1]):
            print(key, value)
    print('Total:', total)
    print('Total with changes:', total_with_changes)
    
 
#    writings = parse(sys.argv[1])
#    sample = [w for w in writings if w['changes'] and 'C' in [change['symbol'] for change in w['changes']]][0]
#    print(sample)
#    print(sample["text"])
#    from pprint import pprint
#    pprint([i for i in sample["changes"] if i["symbol"] == 'C'])
