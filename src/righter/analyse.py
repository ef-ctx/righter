import argparse
import json



def parse_changes(writing, mistake_type):
    if mistake_type is not None:
        writing["changes"] = [i for i in writing["changes"] if i["symbol"] == mistake_type]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--file-input', help='Input txt file')
    parser.add_argument('-m', '--mistake-type', help='Type of mistake', choices=['AR', 'C', 'SP', 'NSW'])
    parser.add_argument('-t', '--analysis-type', help='Type of analysis', choices=['quantitative', 'qualitative'])
    parser.add_argument('-o', '--file-output', help='Save analysis to output file')
    args = parser.parse_args()

    with open(args.file_input, 'r') as input_file:
        writings_list = []
        for line in input_file:
            writing = json.loads(line.strip())
            parse_changes(writing, args.mistake_type)
            if writing["changes"]:
                print(writing)  
