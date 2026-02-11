
def generates_a_matrix_of_data(path):
    with open(path, 'r', encoding="utf-8") as log:
        matrix_of_data=[w for w in [l.split(",") for l in log.readlines()]]
    return matrix_of_data

def extracting_external_IP_addresses(data):
    list_of_external_IP=[i[1] for i in data if not i[1].startswith("192.168") and not i[1].startswith("10.")]
    return list_of_external_IP

def filtering_by_sensitive_port(data):
    list_of_sensitive_port = [i for i in data if  i[3]== '22' or i[3]== '23' or i[3]== '3389']
    return list_of_sensitive_port
