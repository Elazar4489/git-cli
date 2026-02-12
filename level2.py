import level1 as l1


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

def suspicious_detection_for_each_IP(data):
    list_of_ip=[row[1] for row in data]

    aa={"EXTERNAL_IP": l1.extracting_external_IP_addresses(data),
        "SENSITIVE_PORT": list(map(lambda ip: ip[1],l1.filtering_by_sensitive_port(data))),
        "LARGE_PACKET": list(map(lambda ip: ip[1],l1.filter_by_size(data))),
        "NIGHT_ACTIVITY": list(map(lambda ip: ip[1],l1.filter_by_time(data)))}
    dict_with_set={}
    for ip in list_of_ip:
        for key,value in aa.items():
            if ip in value and ip not in dict_with_set:
                dict_with_set[ip]={key}
            elif ip in value:
                dict_with_set[ip].add(key)
    dict_with_set= {k: list(v) for k,v in dict_with_set.items()}
    return dict_with_set

def filtering_the_suspicion_dictionary(data):
    new_dict={k: v for k,v in suspicious_detection_for_each_IP(data).items() if len(v) >=2}
    return new_dict
