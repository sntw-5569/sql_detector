import argparse
from difflib import Differ
import sys


def main(file1: str, file2: str):
    try:
        f1 = open(f"output/{file1}", 'r', encoding='utf-8')
        f2 = open(f"output/{file2}", 'r', encoding='utf-8')
    except FileNotFoundError as e:
        print(e)
        exit(1)

    with f1, f2:
        text1 = f1.read()
        text2 = f2.read()
        diff = Differ()
        result = list(diff.compare(
            text1.splitlines(keepends=True),
            text2.splitlines(keepends=True)
        ))

    sys.stdout.writelines(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f1', '--file1', help='Specify check file name', required=True)
    parser.add_argument('-f2', '--file2', help='Specify check file name', required=True)
    args = parser.parse_args()

    main(args.file1, args.file2)
