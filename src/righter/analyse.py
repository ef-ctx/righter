import argparse
import righter
import collections
import json
from statistics import mean, stdev
import textwrap
from terminaltables import AsciiTable


TEXTWRAP = 40


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


def show_qualitative(baseline, predicted):
    data = []
    
    baseline_dict = map_id_to_field(baseline, "changes")
    predicted_dict = map_id_to_field(predicted, "changes")
    writings_dict = map_id_to_field(baseline, "text")
    level_pred_dict = map_id_to_field(predicted, "level")
    level_base_dict = map_id_to_field(predicted, "level")

    total_items = 0
    precisions = collections.defaultdict(lambda: [])
    recalls = collections.defaultdict(lambda: [])
    precision_list = []
    recall_list = []
    for id_, text in writings_dict.items():
        text = format_text(text)
        baseline = format_changes(baseline_dict[id_])
        predicted = format_changes(predicted_dict.get(id_, []))
        base = flatten2(id_, baseline_dict[id_])
        prediction = flatten2(id_, predicted_dict.get(id_, []))
        prec = "{}".format(precision(base, prediction))
        rec = "{}".format(recall(base, prediction))
        row = [id_, text, baseline, predicted, prec, rec]
        data.append(row)
        precision_list.append(float(prec))
        recall_list.append(float(rec))
        level = int(level_pred_dict.get(id_, level_base_dict.get(id_, 0)))
        precisions[level].append(float(prec))
        recalls[level].append(float(rec))
        total_items += 1
    data = sorted(data, key=lambda row: float(row[-2]), reverse=True)
    headers = ["id", "text", "baseline", "predicted", "precision", "recall"]
    data.insert(0, headers)
    table = AsciiTable(data)
    table.inner_row_border = True
    print(table.table)
    print("total items: ", total_items)
    print("average precision: {} (std: {})".format(mean(precision_list), stdev(precision_list)))
    print("average recall: {} (std: {})".format(mean(recall_list), stdev(recall_list)))
    print("level,precision,recall")
    for level in sorted(precisions.keys()):
        print("{},{},{}".format(level, mean(precisions[level]), mean(recalls[level])))


def show_quantitative(annotated, predicted):
    annotated = flatten(map_id_to_field(annotated, "changes"))
    predicted = flatten(map_id_to_field(predicted, "changes"))
    data = [
        ["precision", "{}".format(precision(annotated, predicted))],
        ["recall", "{}".format(recall(annotated, predicted))]
    ]
    table = AsciiTable(data)
    table.inner_row_border = True
    print(table.table)


def show_mismatches(annotated, predicted, precision=True):
    annotated = flatten(map_id_to_field(annotated, "changes"))
    predicted = flatten(map_id_to_field(predicted, "changes"))
    if precision:
        mismatched = predicted - annotated
    else:
        mismatched = annotated - predicted
    count = collections.defaultdict(lambda: 0)
    for ms in mismatched:
        count[ms[2]] += 1
    count = list(count.items())
    count.sort(key=lambda x: x[1])
    for k, v in count:
        print(k, v)


def flatten(writings):
    """Flatten a dict of writings into a list of tuples. Notice that we are
    ignoring correct key right now. This is deliberated: we still do not
    support correction but only error flaging"""
    return {(key, change['start'], change['selection'].strip(), change['symbol'].strip()) for key, changes in writings.items() for change in changes}


def flatten2(id_, changes):
    return {(id_, change['start'], change['selection'].strip(), change['symbol'].strip()) for change in changes}


def precision(annotations, predictions):
    if not predictions:
        return 1.

    return len(annotations & predictions) / len(predictions)


def recall(annotations, predictions):
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
        print("\nDetailed comparison")
        show_qualitative(annotated, predicted)

    if args.analysis_type in ["all", 'quantitative']:
        print("\nSummary")
        show_quantitative(annotated, predicted)

