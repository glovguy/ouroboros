import re
from git import Git


def all_project_python_files():
    allFiles = []
    for eachFilePath in Git().ls_files().split("\n"):
        if re.match(r'.*\.py$', eachFilePath):
            allFiles.append(eachFilePath)
    return allFiles


def imported_modules(file):
    modules = set()
    for eachLine in file:
        module = imported_module_name(eachLine)
        if module is not None:
            modules.add(module)
    return modules


def imported_module_name(line):
    line = remove_comments(line)
    import_partial_module = re.search(r'^\s*from (.*) import.*', line)
    if import_partial_module is not None:
        return import_partial_module.group(1)
    import_whole_module = re.search(r'^\s*import (.*)', line)
    if import_whole_module:
        return import_whole_module.group(1)
    return None


def remove_comments(line):
    return re.sub(r'#.*', '', line)
