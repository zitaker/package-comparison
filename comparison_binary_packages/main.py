import os
import json

from package_comparison import compare_packages
from cli import parse_args


def save_data(data, name_file):
    directory = 'tests/fixtures'
    path = os.path.join(directory, f"{name_file}.json")

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def main():
    print('wait - the download is in progress.')
    packages_p10, packages_sisyphus = parse_args()
    save_data(packages_p10, 'p10')
    print('The p10 packages are assembled.')
    save_data(packages_sisyphus, 'sisyphus')
    print('The sisyphus packages are assembled.')
    print('-----------------')

    path_p10 = 'tests/fixtures/p10.json'
    path_sisyphus = 'tests/fixtures/sisyphus.json'
    result = compare_packages(path_p10, path_sisyphus)
    print('-----------------')

    save_data(result[0], 'packages_p10_not_in_sisyphus')
    print('Done - all packages that are in p10 but not in sisyphus.')
    save_data(result[1], 'packages_sisyphus_not_in_p10')
    print('Done - all packages that are in sisyphus but are not in p10.')
    save_data(result[2], 'greater_version_release_sisyphus')
    print('Done - all packages with more version-release in sisyphus than in p10.')


if __name__ == '__main__':
    main()
