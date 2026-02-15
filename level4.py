

def generates_a_matrix_of_data(path):
    with open(path, 'r', encoding="utf-8") as log:
        for line in log:
            line=[w for w in line.split(",")]
            yield list(line)


a=generates_a_matrix_of_data('network_traffic.log')

