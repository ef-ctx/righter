import argparse
import json

def filter_changes(changes, mistake_type):
    if mistake_type is not None:
        return [c for c in changes if c["symbol"] == mistake_type]
    else:
        return changes


def read_writings(file_name, mistake_type):
    writings = {}
    with open(file_name, 'r') as fp:
        for line in fp:
            writing = json.loads(line.strip())
            changes = filter_changes(writing['changes'], mistake_type)
            if changes:
                writings[writing['id']] = changes
    return writings


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
    parser.add_argument('-t', '--analysis-type', help='Type of analysis', choices=['quantitative', 'qualitative'])
    parser.add_argument('-o', '--file-output', help='Save analysis to output file')
    args = parser.parse_args()

    annotated = read_writings(args.annotated_file, args.mistake_type)
    predicted = read_writings(args.predicted_file, args.mistake_type)

    if args.analysis_type == 'quantitative':
        print('Precision:', precision(annotated, predicted))
        print('Recall:', recall(annotated, predicted))
    else:
        for key, changes in annotated.items():
            print(key, changes)
