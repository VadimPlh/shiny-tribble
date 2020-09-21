import json
import os


def get_coverage_from(coverage_path, mapping):
    coverage_files = os.listdir(coverage_path)
    for file_path in coverage_files:
        with open("{}/{}".format(coverage_path, file_path)) as f:
            json_data = json.load(f)
            for coverage_file in json_data["files"]:
                if coverage_file not in mapping:
                    mapping[coverage_file] = dict()
                for covered_line in json_data["files"][coverage_file]["executed_lines"]:
                    if covered_line not in mapping[coverage_file]:
                        mapping[coverage_file][covered_line] = []
                    mapping[coverage_file][covered_line].append(file_path)


line_to_test = dict()
get_coverage_from("./coverage/", line_to_test)
with open("./coverage/mapping", 'w') as file:
    json.dump(line_to_test, file)
