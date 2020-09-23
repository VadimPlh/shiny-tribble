import pydriller as pd
import json

def get_changes():
    changed_lines = dict()
    for commit in pd.RepositoryMining('~/shiny-tribble', order="reverse").traverse_commits():
        for m in commit.modifications:
            if m.filename not in changed_lines:
                changed_lines[m.filename] = set()
            for line, _ in m.diff_parsed["added"]:
                changed_lines[m.filename].add(line)
            for line, _ in m.diff_parsed["deleted"]:
                changed_lines[m.filename].add(line)
        return changed_lines


tests = set()
changes = get_changes()
with open("./coverage/mapping") as f:
    test_mapping = json.load(f)
    for file in changes:
        if file in test_mapping:
            for changes_line_number in changes[file]:
                str_line = str(changes_line_number)
                if str_line in test_mapping[file]:
                    set_test = set(test_mapping[file][str_line])
                    tests = tests.union(set_test)
print(tests)