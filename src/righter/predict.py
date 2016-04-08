import json
import argparse

import righter
from righter.competitor import ginger

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', help='File with one json per line containing the key text', required=True)
    parser.add_argument('-o', '--file-output', help='Save analysis to output file', required=True)
    parser.add_argument('-a', '--algorithm', help='Name of the algorithm to use')
    args = parser.parse_args()

    if args.algorithm is None:
        check = righter.check
    elif args.algorithm == 'ginger':
        check = ginger.check

    with open(args.input_file, 'r') as input_fp:
        with open(args.file_output, 'w') as output_fp:
            for line in input_fp:
                writing = json.loads(line.strip())
                writing['changes'] = check(writing['text'])
                print(json.dumps(writing), file=output_fp)
