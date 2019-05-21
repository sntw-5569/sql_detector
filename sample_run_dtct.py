from time import sleep
import sys
from pathlib import Path

PARENT_DIR_PATH = str(Path(Path(str(Path.parent)).resolve()).parents[0])
print(PARENT_DIR_PATH)
sys.path.append(PARENT_DIR_PATH)
from py_git.brc_ctrl import PyGit
from sql_detector import create_sql_file, diff_checker


def before_branch_detection(branch_name: str, py_git: PyGit):
    py_git.change_branch(branch_name)
    create_sql_file.main()


def detect_diff_query(before_branch, after_branch, conf_file, mock_func):
    print({'BEFORE': before_branch, 'AFTER': after_branch})
    print(PARENT_DIR_PATH)
    pygit = PyGit(PARENT_DIR_PATH)

    if not pygit.is_git_repository:
        raise Exception('Not Git Repository.')
    pygit.change_branch(before_branch)
    before_output = create_sql_file.main(conf_file, mock_func)
    pygit.change_branch(after_branch)

    # controlled overwrite file
    sleep(2.5)
    
    after_output = create_sql_file.main(conf_file, mock_func)

    diff_checker.main(before_output, after_output)
    return


if '__main__' in __name__:
    args = sys.argv
    if '-l' in args:
        PyGit.branch_list(is_logging=True)
    elif '-h' in args or len(args) == 1:
        print('\n---- command args ----')
        print('$ python run_dict.py [before_branch_name] [after_branch_name]')
        print('options:\n  -l : branch list preview. \n')
    elif len(args) == 3:
        input_config = input('[-3-]< input Config File. \n')
        patched_mock = input('[-3-]< input patched mock method name for SQL Execute. \n')
        print('------')
        config_path = Path() / input_config
        if config_path.exists:
            print(config_path.resolve())
        else:
            raise Exception(f'Not found input config file: {config_path}')
        print(patched_mock)

        detect_diff_query(
            before_branch=args[1], after_branch=args[2],
            conf_file=config_path.name, mock_func=patched_mock)