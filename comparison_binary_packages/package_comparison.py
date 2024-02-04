import rpm
import json


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


def additional_comparison(new_package, old_package, meaning):
    if new_package[meaning] > old_package[meaning]:
        return 1
    elif new_package[meaning] < old_package[meaning]:
        return -1
    else:
        return 0


def greater_version_release(new_packages, old_packages):
    result = []
    old_packages_index = {}

    for old_package in old_packages:
        old_packages_index[old_package['name']] = old_package

    for new_package in new_packages:
        name = new_package['name']
        if name in old_packages_index:
            old_package = old_packages_index[name]

            package_1 = rpm.hdr()
            package_2 = rpm.hdr()
            package_1['epoch'] = new_package.get('epoch', 0)
            package_1['version'] = new_package['version']
            package_1['release'] = new_package['release']

            package_2['epoch'] = old_package.get('epoch', 0)
            package_2['version'] = old_package['version']
            package_2['release'] = old_package['release']

            comparison = rpm.versionCompare(package_1, package_2)

            if comparison == 0:
                if new_package['disttag'] != old_package['disttag']:
                    comparison = additional_comparison(new_package, old_package, 'disttag')
                elif new_package['buildtime'] != old_package['buildtime']:
                    comparison = additional_comparison(new_package, old_package, 'buildtime')
                elif new_package['source'] != old_package['source']:
                    comparison = additional_comparison(new_package, old_package, 'source')

            if comparison > 0:
                result.append(new_package)

    return result


def compare_packages(path_p10, path_sisyphus):
    packages_p10 = extracting_package(path_p10)
    packages_sisyphus = extracting_package(path_sisyphus)

    packages_p10_not_in_sisyphus = packages(packages_p10, packages_sisyphus)
    packages_sisyphus_not_in_p10 = packages(packages_sisyphus, packages_p10)
    greater_version_release_sisyphus = greater_version_release(packages_p10, packages_sisyphus)

    return (packages_p10_not_in_sisyphus,
            packages_sisyphus_not_in_p10,
            greater_version_release_sisyphus)
