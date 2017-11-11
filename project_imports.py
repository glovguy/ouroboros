import re
from git import Git


def all_project_python_files():
    allFiles = []
    for eachFilePath in Git().ls_files().split("\n"):
        if re.match(r'.*\.py$', eachFilePath):
            allFiles.append(eachFilePath)
    return allFiles

