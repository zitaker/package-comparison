import json

from package_comparison import compare_packages
from cli import parse_args


def save_data(data):
    path = 'tests/fixtures/lists_binary_packages.json'
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def main():
    print('wait - the download is in progress')
    p10_packages, sisyphus_packages = parse_args()
    result = compare_packages(p10_packages['packages'], sisyphus_packages['packages'])
    save_data(result)
    print('check the result')


if __name__ == '__main__':
    main()
