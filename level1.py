
def getting_the_path_to_the_log_file(path):
    with open(path, 'r', encoding="utf-8") as log:
        list_of_lines_lists=[w for w in [l.split(",") for l in log.readlines()]]
    return list_of_lines_lists
