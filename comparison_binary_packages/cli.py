import argparse

from api_client import ApiClient


def parse_args():
    parser = argparse.ArgumentParser(
        prog = 'comparison_binary_packages',
        description='Package comparison')
    parser.add_argument('branch_p10', help='branch p10')
    parser.add_argument('branch_sisyphus', help='branch sisyphus')
    args = parser.parse_args()

    api_client = ApiClient()
    packages_p10 = api_client.get_branches(args.branch_p10)
    packages_sisyphus = api_client.get_branches(args.branch_sisyphus)
    return packages_p10, packages_sisyphus
