import argparse
from datetime import datetime
import inspect
import json
import re

from sql_detector.util import directory_if_creation

CONFIG_DIR = 'config'


def main(target_file_path: str,
         specify_method: str=None,
         output_file_name: str=None):
    try:
        exec(f"import {target_file_path} as target_file")
    except ModuleNotFoundError as e:
        print(e)
        exit(1)

    method_list = eval('dir(target_file)')
    method_list = [l for l in method_list if not l.startswith('_')]

    result = dict()

    if specify_method:
        method_list = [l for l in method_list if re.match(specify_method, l)]

    for method_name in method_list:
        try:
            signature = eval(f'inspect.signature(target_file.{method_name})')
        except Exception as e:
            print(e)
            print(f'Skip {method_name}')
            continue

        result[method_name] = dict()
        parameters = signature.parameters
        for param in parameters.keys():
            param_type = parameters[param].annotation
            if param_type is inspect._empty:
                result[method_name][param] = ''
            else:
                result[method_name][param] = eval(f'{param_type.__name__}()')

    current_timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    config_file_name = output_file_name or f'config_{current_timestamp}'
    directory_if_creation(CONFIG_DIR)
    with open(f"{CONFIG_DIR}/{config_file_name}", 'w', encoding='utf-8') as f:
        json.dump({'script_path': target_file_path, 'parameters': result}, f,
                  ensure_ascii=False,
                  indent=4,
                  sort_keys=True,
                  separators=(',', ': '))

    print('create configure success!!')
    return config_file_name


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        help='Specify file name.(ex: path.to.module)',
                        required=True)
    parser.add_argument('-m', '--method',
                        help='Specify method name (regular expression valid)')
    parser.add_argument('-o', '--output', help='Output file name')

    args = parser.parse_args()
    main(target_file_path=args.file.replace('/', '.'),
         specify_method=args.method,
         output_file_name=args.output)
