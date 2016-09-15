import argparse
import righter
import collections
import json
from statistics import mean, stdev
import textwrap
from terminaltables import AsciiTable


TEXTWRAP = 40


def filter_changes(writing, mistake_types):
    writing["changes"] = [i for i in writing["changes"] if i.get('symbol') and i["symbol"] in mistake_types]


def read_writings(file_name, mistake_types):
    writings = []
    with open(file_name, 'r') as fp:
        for line in fp:
            try:
                writing = json.loads(line.strip())
            except:
                print(line)
                raise
            if mistake_types:
                filter_changes(writing, mistake_types)
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
        xubi = "{} ({})".format(i.get("selection", ""), i["start"])
        changes.append(xubi)
    return "\n".join(changes)


def format_text(text):
    chunks = textwrap.wrap(text, TEXTWRAP)
    return "\n".join(chunks)


def show_qualitative(baseline, predicted, ignore_types=False):
    data = []
    
    baseline_dict = map_id_to_field(baseline, "changes")
    predicted_dict = map_id_to_field(predicted, "changes")
    writings_dict = map_id_to_field(baseline, "text")
    level_pred_dict = map_id_to_field(predicted, "level")
    level_base_dict = map_id_to_field(baseline, "level")

    nat_pred_dict = map_id_to_field(predicted, "nationality")
    nat_base_dict = map_id_to_field(baseline, "nationality")

    total_items = 0
    precisions = collections.defaultdict(lambda: [])
    recalls = collections.defaultdict(lambda: [])
    precisions_per_nat = collections.defaultdict(lambda: [])
    recalls_per_nat = collections.defaultdict(lambda: [])
    precision_list = []
    recall_list = []
    for id_, text in writings_dict.items():
        if id_ in predicted_dict:
            text = format_text(text)
            baseline = format_changes(baseline_dict[id_])
            predicted = format_changes(predicted_dict.get(id_, []))
            base = flatten2(id_, baseline_dict[id_], ignore_types)
            prediction = flatten2(id_, predicted_dict.get(id_, []), ignore_types)
            prec = "{}".format(precision(base, prediction))
            rec = "{}".format(recall(base, prediction))
            row = [id_, text, baseline, predicted, prec, rec]
            data.append(row)
            precision_list.append(float(prec))
            recall_list.append(float(rec))
            level = int(level_pred_dict.get(id_, level_base_dict.get(id_, 0)))
            precisions[level].append(float(prec))
            recalls[level].append(float(rec))
            nat = nat_pred_dict.get(id_, nat_base_dict.get(id_, ''))
            precisions_per_nat[nat].append(float(prec))
            recalls_per_nat[nat].append(float(rec))
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
    #print("level,precision,recall")
    #for level in sorted(precisions.keys()):
    #    print("{},{},{}".format(level, mean(precisions[level]), mean(recalls[level])))

    #nats = []
    #for nat in precisions_per_nat.keys():
    #    if len(precisions_per_nat[nat]) > 100:
    #        prec = mean(precisions_per_nat[nat])
    #        rec = mean(recalls_per_nat[nat])
    #        f1 = 2 * ((prec * rec) / (prec + rec))
    #        nats.append((f1, nat))

    #print("nat,f1")
    #for f1, nat in sorted(nats, reverse=True):
    #    print("{},{}".format(nat, f1))


def show_quantitative(annotated, predicted, ignore_types=False):
    annotated = map_id_to_field(annotated, "changes")
    predicted = map_id_to_field(predicted, "changes")
    for id_ in list(annotated.keys()):
        if id_ not in predicted:
            del annotated[id_]
    annotated = flatten(annotated, ignore_types)
    predicted = flatten(predicted, ignore_types)
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


def flatten(writings, ignore_types=False):
    """Flatten a dict of writings into a list of tuples. Notice that we are
    ignoring correct key right now. This is deliberated: we still do not
    support correction but only error flaging"""
    if ignore_types:
        return {(key, change['start']) for key, changes in writings.items() for change in changes}
    else:
        return {(key, change['start'], change.get('selection', "").strip(), change['symbol'].strip()) for key, changes in writings.items() for change in changes if change.get('symbol')}


def flatten2(id_, changes, ignore_types):
    if ignore_types:
        return {(id_, change['start']) for change in changes}
    else:
        return {(id_, change['start'], change.get('selection', "").strip(), change['symbol'].strip()) for change in changes if 'symbol' in change}


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
    parser.add_argument('-m', '--mistake-types', help='Types of mistake to analyse', nargs='+')
    parser.add_argument('-t', '--analysis-type', help='Type of analysis', default='all', choices=['all', 'quantitative', 'qualitative'])
    parser.add_argument('-o', '--file-output', help='Save analysis to output file')
    args = parser.parse_args()
    if not args.mistake_types:
        ignore_types = True
    else:
        ignore_types = False

    annotated = read_writings(args.annotated_file, args.mistake_types)
    predicted = read_writings(args.predicted_file, args.mistake_types)
    if args.analysis_type in ["all", "qualitative"]:
        print("\nDetailed comparison")
        show_qualitative(annotated, predicted, ignore_types=ignore_types)

    if args.analysis_type in ["all", 'quantitative']:
        print("\nSummary")
        show_quantitative(annotated, predicted, ignore_types=ignore_types)

