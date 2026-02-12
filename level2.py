from level1 import generates_a_matrix_of_data
a=generates_a_matrix_of_data('network_traffic.log')
def counting_requests_by_IP(data):
    ips = [row[1] for row in data]
    return {ip: ips.count(ip) for ip in ips}

# def counting_requests_by_IP2(data):
#     dict_of_count_ip={}
#     for row in data:
#         if row[1] in dict_of_count_ip:
#             dict_of_count_ip[row[1]]+=1
#         else:
#             dict_of_count_ip[row[1]]=1
#     return dict_of_count_ip

def port_to_protocol_mapping(data):
    dict_of_mapped_port={row[3]: row[4] for row in data}
    return dict_of_mapped_port
