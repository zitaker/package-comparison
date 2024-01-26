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


def get_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths


def get_paths_of_list(directory_list):
    pairs = []
    for path in directory_list:
        if os.path.isdir(path):
            files = get_file_paths(path)
            if len(files) == 1:
                continue
            elif len(files) >= 2:
                pairs.append((files[0], files[1]))
    return pairs


def split_into_directory(list_paths):
    result_pairs = []
    for path in list_paths:
        pairs = get_paths_of_list([path])
        if pairs:
            result_pairs.extend(pairs)
    return result_pairs


def save_result_packages():
    path = 'tests/fixtures/'
    list_path = get_paths_directories_arch_value(path)
    list_path_files = split_into_directory(list_path)
    return list_path_files
