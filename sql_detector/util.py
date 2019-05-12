import os


def directory_if_creation(directory_name: str):
    if os.path.exists(directory_name):
        return
    os.mkdir(directory_name)
