from level1 import generates_a_matrix_of_data as g


a=g('network_traffic.log')
extracting_time_from_timestamp=list(map(lambda s: int(s[0][11:13]),g('network_traffic.log')))

package_size_conversion= list(map(lambda b: int(b[-1])/1024,g('network_traffic.log')))

filter_rows_by_port=list(filter(lambda p:p[-3] == "22" or p[-3]== "23" or p[-3]=="3389",g('network_traffic.log')))

nighttime_activity_filtering=list(filter(lambda n: "00:00:00" < n[0][11:19] < "06:00:00", g('network_traffic.log')))

suspicion_checks = { "EXTERNAL_IP": lambda row: True if not row[1].startswith("192.168") and not row[1].startswith("10.") else False,
                     "SENSITIVE_PORT": lambda row: True if  row[3]== '22' or row[3]== '23' or row[3]== '3389' else False,
                     "LARGE_PACKET":lambda row: True if int(row[-1]) > 5000 else False,
                     "NIGHT_ACTIVITY": lambda row: True if "00:00:00" < row[0][11:19] < "06:00:00" else False}

def running_tests_on_a_line(row):
    return list(filter(lambda k: suspicion_checks[k](row), suspicion_checks))

processing_the_entire_log=list(filter(lambda r: any(r.values()),map(lambda row: {str(row): running_tests_on_a_line(row)},a)))
