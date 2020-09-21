import subprocess
import os
import shutil


def get_test_files(dir_with_tests):
    test_files = []
    files_and_dirs = os.listdir(dir_with_tests)
    for i in files_and_dirs:
        if i.startswith("test_"):
            test_files.append(i)
    return test_files


def generate_coverage_file(src_path, test_file_path, test_name, coverage_dir_path):
    print(test_file_path)
    run_pytest_for_file = "coverage run -m --source={}  pytest {}".format(src_path, test_file_path)
    subprocess.call(run_pytest_for_file, shell=True)
    get_coverage = "coverage json --include={}/* --pretty-print -o {}/{}.coverage".format(src_path, coverage_dir_path, test_name)
    subprocess.call(get_coverage, shell=True)


def get_coverage(src_path, dir_with_tests):
    coverage_dir_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "coverage")
    if os.path.exists(coverage_dir_path):
        shutil.rmtree(coverage_dir_path)

    os.mkdir(coverage_dir_path)

    test_files = get_test_files(dir_with_tests)
    for test_file in test_files:
        generate_coverage_file(src_path, "{}/{}".format(dir_with_tests, test_file), test_file, coverage_dir_path)

get_coverage("../simple", "./..") ## TODO: edit this paths