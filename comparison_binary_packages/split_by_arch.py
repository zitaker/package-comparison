import os
import json


def extract_name_from_path(path):
    start_index = path.rfind('/') + 1
    end_index = path.find('.', start_index)
    result = path[start_index:end_index]
    return result


def split_by_arch(file_path):
    with open(file_path, 'r') as file:
        reading_data = json.load(file)

    arch_packages = {}
    for package in reading_data['packages']:
        arch_value = package['arch']

        if arch_value not in arch_packages:
            arch_packages[arch_value] = []

        arch_packages[arch_value].append(package)

    for arch_value, packages in arch_packages.items():
        package_json = {
            "packages": packages
        }

        directory = f'tests/fixtures/{arch_value}/'
        os.makedirs(directory, exist_ok=True)

        name = extract_name_from_path(file_path)
        package_file_path = f'{directory}{name}_{arch_value}.json'

        with open(package_file_path, 'w') as package_file:
            json.dump(package_json, package_file, indent=4)
