import os
import json
import time


from package_comparison import compare_packages
from cli import parse_args
from split_by_arch import split_by_arch
from save_result_packages import save_result_packages


def save_data(data, name_file):
    directory = 'tests/fixtures'
    path = os.path.join(directory, f"{name_file}.json")

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def save_result(directory, data, name_file):
    find_index = directory.rfind('/', 0, -3)
    if find_index != -1:
        path_for_save = f"{directory[:find_index]}{'/result_conditions/'}"

    if not os.path.exists(path_for_save):
        os.makedirs(path_for_save)

    path = os.path.join(path_for_save, f"{name_file}.json")

    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def split_by_directory(path_file):
    with open(path_file, 'r') as file:
        reading_data = json.load(file)

    arch_values = set()
    for package in reading_data["packages"]:
        arch_value = package["arch"]
        arch_values.add(arch_value)


def paths_to_files(file_paths):
    path_1, path_2 = file_paths
    return path_1, path_2


def main():
    time_start_1 = time.time()
    print('Wait - the download is in progress.')
    packages_p10, packages_sisyphus = parse_args()
    save_data(packages_p10, 'p10')
    print('The p10 packages are assembled.')
    save_data(packages_sisyphus, 'sisyphus')
    print('The sisyphus packages are assembled.')

    time_end_1 = divmod(time.time() - time_start_1, 60)
    print(f"Time execution - receiving packages: "
          f"{int(time_end_1[0])}:{time_end_1[1]:.3f}")

    time_start_2 = time.time()
    path_p10 = 'tests/fixtures/p10.json'
    path_sisyphus = 'tests/fixtures/sisyphus.json'

    split_by_directory(path_p10)
    split_by_directory(path_sisyphus)

    print('Directories were created by arch_value.')
    split_by_arch(path_p10)
    split_by_arch(path_sisyphus)
    print('Packages by arch_value were extracted.')

    time_end_2 = divmod(time.time() - time_start_2, 60)
    print(f"Time execution - distribution by arch_value: "
          f"{int(time_end_2[0])}:{time_end_2[1]:.3f}")

    list_path_files = save_result_packages()

    for path in list_path_files:
        time_start_3 = time.time()
        result_pair = paths_to_files(path)
        result = compare_packages(result_pair[0], result_pair[1])

        save_result(result_pair[0], result[0], 'packages_p10_not_in_sisyphus')
        save_result(result_pair[0], result[1], 'packages_sisyphus_not_in_p10')
        save_result(result_pair[0], result[2], 'greater_version_release_sisyphus')

        time_end_3 = divmod(time.time() - time_start_3, 60)
        print(f"Time execution - to one arch_value: "
              f"{int(time_end_3[0])}:{time_end_3[1]:.3f}")
    print('Done - see the result.')


if __name__ == '__main__':
    total_time_end = time.time()
    main()
    total_time_end = divmod(time.time() - total_time_end, 60)
    print(f"Time execution - total: "
          f"{int(total_time_end[0])}:{total_time_end[1]:.3f}")
