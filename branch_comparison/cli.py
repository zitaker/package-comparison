import argparse

from api_client import ApiClient


def parse_args():
    parser = argparse.ArgumentParser(
        prog = 'branch_comparison',
        description='Package comparison tool')
    parser.add_argument('branch_p10', help='branch p10')
    parser.add_argument('branch_sisyphus', help='branch sisyphus')
    args = parser.parse_args()

    api_client = ApiClient()
    p10_packages = api_client.get_branches(args.branch_p10)
    sisyphus_packages = api_client.get_branches(args.branch_sisyphus)

    return p10_packages, sisyphus_packages
