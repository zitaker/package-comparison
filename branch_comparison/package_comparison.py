def compare_packages(p10_packages, sisyphus_packages):
    result = {
        'packages_p10_not_in_sisyphus': [],
        'packages_sisyphus_not_in_p10': [],
    }

    p10_names = set()
    for package in p10_packages:
        package_name = package['name']
        p10_names.add(package_name)

    sisyphus_names = set()
    for package in sisyphus_packages:
        package_name = package['name']
        sisyphus_names.add(package_name)

    result['packages_p10_not_in_sisyphus'] = []
    for package in p10_packages:
        package_name = package['name']
        if package_name not in sisyphus_names:
            result['packages_p10_not_in_sisyphus'].append(package)

    result['packages_sisyphus_not_in_p10'] = []
    for package in sisyphus_packages:
        package_name = package['name']
        if package_name not in p10_names:
            result['packages_sisyphus_not_in_p10'].append(package)

    return result
