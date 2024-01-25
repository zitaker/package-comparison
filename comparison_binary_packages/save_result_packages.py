import os


def get_paths_directories_arch_value(path):
    all_elements = os.listdir(path)

    list_directories = []
    for element in all_elements:
        if os.path.isdir(os.path.join(path, element)):
            list_directories.append(element)

    list_paths = []
    for elem in list_directories:
        list_paths.append(os.path.join(path, elem))

    return list_paths


def save_result_packages():
    path = 'tests/fixtures/'
    list_path = get_paths_directories_arch_value(path)
    print(list_path)
