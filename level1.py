
def generates_a_matrix_of_data(path):
    with open(path, 'r', encoding="utf-8") as log:
        list_of_lines_lists=[w for w in [l.split(",") for l in log.readlines()]]
    return list_of_lines_lists

def extracting_external_IP_addresses(data):
    list_of=[i[1] for i in data if not i[1].startswith("192.168") and not i[1].startswith("10.")]
    return list_of

