import argparse
from difflib import Differ
import sys
from pathlib import Path


def main(file1: str, file2: str):
    dir_route = Path().resolve()
    required_modules = ['sql_detector', 'output']

    for dir_name in required_modules:
        if dir_name not in str(dir_route):
            dir_route = dir_route / dir_name
        if not dir_route.exists():
            raise FileNotFoundError(
                'Not found module path. try change current directory.')
    module_dir = dir_route
    try:
        f1 = open(f"{module_dir.resolve()}/{file1}", 'r', encoding='utf-8')
        f2 = open(f"{module_dir.resolve()}/{file2}", 'r', encoding='utf-8')
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
