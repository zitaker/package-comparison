import requests


class ApiClient:
    BASE_URL = 'https://rdb.altlinux.org/api/'

    @classmethod
    def get_branches(cls, branch):
        url = f'{cls.BASE_URL}/export/branch_binary_packages/{branch}'
        response = requests.get(url)
        return response.json()
