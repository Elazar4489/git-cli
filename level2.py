import level1 as l1
a=l1.generates_a_matrix_of_data('network_traffic.log')
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

def filter_by_time(data):
    return [row for row in data if "00:00:00" < row[0][11:19] < "06:00:00"]

def suspicious_detection_for_each_IP(data):
    listush=[row[1] for row in data]

    aa={"EXTERNAL_IP": l1.extracting_external_IP_addresses(data),
        "SENSITIVE_PORT": list(map(lambda ip: ip[1],l1.filtering_by_sensitive_port(data))),
        "LARGE_PACKET": list(map(lambda ip: ip[1],l1.filter_by_size(data))),
        "NIGHT_ACTIVITY": list(map(lambda ip: ip[1],filter_by_time(data)))}
    g={}
    for ip in listush:
        for key,value in aa.items():
            if ip in value and ip not in g:
                g[ip]={key}
            elif ip in value:
                g[ip].add(key)
    yy= {k: list(v) for k,v in g.items()}
    return yy
