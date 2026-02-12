from level1 import generates_a_matrix_of_data as g


a=g('network_traffic.log')
extracting_time_from_timestamp=list(map(lambda s: int(s[0][11:13]),g('network_traffic.log')))

package_size_conversion= list(map(lambda b: int(b[-1])/1024,g('network_traffic.log')))

filter_rows_by_port=list(filter(lambda p:p[-3] == "22" or p[-3]== "23" or p[-3]=="3389",g('network_traffic.log')))

nighttime_activity_filtering=list(filter(lambda n: "00:00:00" < n[0][11:19] < "06:00:00", g('network_traffic.log')))
