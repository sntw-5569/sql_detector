import sys
from pathlib import Path

PARENT_DIR_PATH = str(Path(Path(str(Path.parent)).resolve()).parents[0])
print(PARENT_DIR_PATH)
sys.path.append(PARENT_DIR_PATH)
from py_git.brc_ctrl import PyGit


def before_branch_detection():
    pass


def detect_diff_query(before_branch, after_branch):
    print({'BEFORE': before_branch, 'AFTER': after_branch})
    pass


if '__main__' in __name__:
  args = sys.argv
  if '-l' in args:
    PyGit.branch_list(is_logging=True)
  elif '-h' in args or len(args) == 1:
    print('\n---- command args ----')
    print('$ python run_dict.py [before_branch_name] [after_branch_name]')
    print('options:\n  -l : branch list preview. \n')
  elif len(args) > 3:
    detect_diff_query(before_branch=args[1], after_branch=args[2])