import json

from packaging import version


def extracting_package(path_file):
    with open(path_file, 'r') as file:
        reading_data = json.load(file)

    package = reading_data.get('packages', [])
    return package


def packages(in_package, no_in_package):
    result = []
    for package in in_package:
        if package not in no_in_package:
            result.append(package)
    return result


def greater_version_release(new_packages, old_packages):
    result = []
    for package_sisyphus in new_packages:
        package_name_sisyphus = package_sisyphus['name']
        matching_package_p10 = None
        for package_p10 in old_packages:
            if (
                package_p10['name'] == package_name_sisyphus and
                version.parse(package_p10['version']) <
                version.parse(package_sisyphus['version'])
            ):
                matching_package_p10 = package_p10
                break

        if matching_package_p10 is not None:
            result.append(package_sisyphus)
    return result


def compare_packages(path_p10, path_sisyphus):
    packages_p10 = extracting_package(path_p10)
    packages_sisyphus = extracting_package(path_sisyphus)

    packages_p10_not_in_sisyphus = packages(packages_p10, packages_sisyphus)
    packages_sisyphus_not_in_p10 = packages(packages_sisyphus, packages_p10)
    greater_version_release_sisyphus = greater_version_release(packages_sisyphus, packages_p10)

    return (packages_p10_not_in_sisyphus,
            packages_sisyphus_not_in_p10,
            greater_version_release_sisyphus)
