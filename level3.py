import level1 as l1

a=l1.generates_a_matrix_of_data('network_traffic.log')
def extracting_time_from_timestamp(data):
    return list(map(lambda s: int(s[0][11:13]),data))

def package_size_conversion(data):
    return list(map(lambda b: int(b[-1])/1024,data))
