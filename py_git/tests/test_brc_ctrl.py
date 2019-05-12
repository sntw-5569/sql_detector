from pathlib import Path
import sys
from unittest import TestCase
sys.path.append(str(Path(Path.cwd()).parents[1]))

from py_git.brc_ctrl import PyGit


class TestBranchControl(TestCase):
    pg = PyGit(str(Path.cwd()))

    def test_change_branch(self):
        self.assertFalse(self.pg.change_branch('unknown', is_logging=False))

    def test_change_base_repository(self):
        self.pg.change_base_repository(str(Path.cwd()))
        self.assertFalse(self.pg.is_git_repository)

    def test_branch_list(self):
        self.assertEqual([], self.pg.branch_list(is_logging=False))
    