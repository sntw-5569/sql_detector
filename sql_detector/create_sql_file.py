import argparse
from datetime import datetime
import json
from unittest.mock import MagicMock, patch
from pathlib import Path
import sys

sys.path.append(str(Path().resolve().parents[1]))
from sql_detector.util import directory_if_creation

OUTPUT_DIR = 'sql_detector/output'


def _write_to_file(file_name: str, content: str):
    with open(f"{OUTPUT_DIR}/{file_name}", 'a', encoding='utf-8') as file:
        file.write(content + '\n')


def _execute_methods(script_path: str, methods: dict, mock_lib: MagicMock):
    try:
        exec(f'import {script_path} as target_file')
    except ModuleNotFoundError as e:
        print(e)
        exit(1)

    current_timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f'sql_{current_timestamp}'
    directory_if_creation(OUTPUT_DIR)
    for method_name, parameter in methods.items():
        result_sql = eval(f'target_file.{method_name}(**{parameter})')
        print(mock_lib.call_args_list)
        args, kwargs = mock_lib.call_args_list[-1]

        _write_to_file(file_name, args[0])

    return file_name


def _method_mock(script_path: str, mock_target_method: str,
                 methods: dict, execute_methods):
    with patch(f'{script_path}.{mock_target_method}') as mock_lib:
        mock_lib.return_value = ('', '')

        return execute_methods(script_path, methods, mock_lib)


def main(config_path: str, mock_target_method: str):
    dir_route = Path().resolve()
    required_modules = ['sql_detector', 'config']

    for dir_name in required_modules:
        if dir_name not in str(dir_route):
            dir_route = dir_route / dir_name
        if not dir_route.exists():
            raise FileNotFoundError(
                'Not found module path. try change current directory.')

    module_dir = dir_route
    try:
        with open(f"{module_dir.resolve()}/{config_path}", 'r') as f:
            config_json = json.load(f)
    except FileNotFoundError as e:
        print(e)
        exit(1)

    script_path = config_json.get('script_path')
    methods = config_json.get('parameters')

    if mock_target_method:
        written_file_name = _method_mock(script_path, mock_target_method,
                                         methods, _execute_methods)
    else:
        written_file_name = _execute_methods(script_path, methods)

    print('create sql success!!')
    return written_file_name


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config',
                        help='Specify config file name', required=True)
    parser.add_argument('-m', '--mock', help='Specify mock target method')
    args = parser.parse_args()

    main(args.config, args.mock)
