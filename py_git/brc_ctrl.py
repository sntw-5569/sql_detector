from git import Repo
from pathlib import Path


class PyGit():

    Repository = None
    is_git_repository = False

    def __init__(self, dir_name):
        self.change_base_repository(dir_name)

    def _log(self, message, is_logging):
        if is_logging:
            print(message)

    def change_base_repository(self, dir_name):
        try:
            repo = Repo(dir_name)
        except Exception as e:
            self.is_git_repository = False
            self.Repository = None
        else:
            if repo.git:
                self.is_git_repository = True
                self.Repository = repo
            else:
                self.is_git_repository = False
                self.Repository = None

    def change_branch(self, brc_name: str, is_logging=True):
        if not brc_name or not self.Repository:
            return False

        if brc_name not in self.Repository.branches:
            self._log('[-3-]< Not Found Branch.', is_logging)
            return False

        base_br = self.Repository.active_branch.name
        if base_br == brc_name:
            self._log('[-3-]< Target is active branche. Skip switching.', is_logging)
        else:
            switched_br = self.Repository.branches[brc_name]
            try:
                switched_br.checkout()
            except Exception as e:
                self._log(f"'[-3-]< Ummm...Can't switched branch. \n{e}", is_logging)
                return False
            else:
                now_br = self.Repository.active_branch.name
                self._log(f'[-3-]< Switch "{base_br}" ---> "{now_br}".', is_logging)
                
        return True


    def branch_list(self, is_logging=True):
        if not self.Repository:
            return []

        self._log('[-3-]< branches in target directory ---------', is_logging)
        for brc in self.Repository.branches:
            self._log(f'  -  {brc.name}', is_logging)
        self._log('- - - - - - - - - - - - - - - - - - - - - - -', is_logging)
        
        return [b.name for b in self.Repository.branches]


# for debug ----
TestRun = False
target_dir = "C:\\Users\\dt\\source\\repos\\costvisualizer3"
repo = Repo(target_dir)
# --------------

if TestRun:
    pyg = PyGit(target_dir)
    if pyg.is_git_repository:
        pyg = PyGit(target_dir)
        pyg.branch_list()
        # pyg.change_branch('qa')
        pyg.change_branch('merge/pickup-from-qa')
        exit(0)
    else:
        pyg._log('[-3-]< Not Found Git Repository.', True)
        exit(1)