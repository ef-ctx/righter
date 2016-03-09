import argparse
import json
import textwrap
from terminaltables import AsciiTable


TEXTWRAP = 80


def filter_changes(writing, mistake_type):
    if mistake_type is not None:
        writing["changes"] = [i for i in writing["changes"] if i["symbol"] == mistake_type]


def read_writings(file_name, mistake_type):
    writings = []
    with open(file_name, 'r') as fp:
        for line in fp:
            writing = json.loads(line.strip())
            filter_changes(writing, mistake_type)
            if writing.get("changes"):
                writings.append(writing)
    return writings


def map_id_to_field(writings, field):
    writings_dict = {}
    for writing in writings:
        writings_dict[writing['id']] = writing[field]
    return writings_dict


def format_changes(original_changes):
    changes = []
    for i in original_changes:
        xubi = "{} ({})".format(i["selection"], i["start"])
        changes.append(xubi)
    return "\n".join(changes)


def format_text(text):
    chunks = textwrap.wrap(text, TEXTWRAP)
    return "\n".join(chunks)


def show_comparison(baseline, predicted):
    data = []
    headers = ["id", "text", "baseline", "predicted"]
    data.append(headers)
    
    baseline_dict = map_id_to_field(baseline, "changes")
    predicted_dict = map_id_to_field(predicted, "changes")
    writings_dict = map_id_to_field(baseline, "text")

    for id_, text in writings_dict.items():
        text = format_text(text)
        baseline = format_changes(baseline_dict[id_])
        predicted = format_changes(predicted_dict[id_])
        row = [id_, text, baseline, predicted]
        data.append(row)
    table = AsciiTable(data)
    table.inner_row_border = True
    print(table.table)


def flatten(writings):
    """Flatten a dict of writings into a list of tuples. Notice that we are
    ignoring correct key right now. This is deliberated: we still do not
    support correction but only error flaging"""
    return {(key, change['start'], change['selection'], change['symbol']) for key, changes in writings.items() for change in changes}


def precision(annotated, predicted):
    annotations = flatten(annotated)
    predictions = flatten(predicted)

    if not predictions:
        return 1.

    return len(annotations & predictions) / len(predictions)


def recall(annotated, predicted):
    annotations = flatten(annotated)
    predictions = flatten(predicted)

    if not annotations:
        return 1.

    return len(annotations & predictions) / len(annotations)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--annotated-file', help='Annotated input file', required=True)
    parser.add_argument('-p', '--predicted-file', help='Predicted input file', required=True)
    parser.add_argument('-m', '--mistake-type', help='Type of mistake', choices=['AR', 'C', 'SP', 'NSW'])
    parser.add_argument('-t', '--analysis-type', help='Type of analysis', default='all', choices=['all', 'quantitative', 'qualitative'])
    parser.add_argument('-o', '--file-output', help='Save analysis to output file')
    args = parser.parse_args()

    annotated = read_writings(args.annotated_file, args.mistake_type)
    predicted = read_writings(args.predicted_file, args.mistake_type)
    if args.analysis_type in ["all", "qualitative"]:
        show_comparison(annotated, predicted)

    if args.analysis_type in ["all", 'quantitative']:
        annotated = map_id_to_field(annotated, "changes")
        predicted = map_id_to_field(predicted, "changes")
        print('Precision:', precision(annotated, predicted))
        print('Recall:', recall(annotated, predicted))

