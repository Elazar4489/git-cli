from level3 import *

total_lines_read=0
total_suspicious_lines=0
count_for_each_suspicion_type= {"EXTERNAL_IP":0,"SENSITIVE_PORT":0,"LARGE_PACKET": 0,"NIGHT_ACTIVITY": 0}



def update_statistics(is_new_line=False, suspicions=None):
    global total_lines_read, total_suspicious_lines, count_for_each_suspicion_type
    if is_new_line:
        total_lines_read += 1
    if suspicions:
        total_suspicious_lines += 1
        for s_type in suspicions:
            count_for_each_suspicion_type[s_type] = count_for_each_suspicion_type.get(s_type, 0) + 1



def generates_a_matrix_of_data(path):
    with open(path, 'r', encoding="utf-8") as log:
        for line in log:
            update_statistics(is_new_line=True)
            line=[w for w in line.split(",")]
            yield list(line)

def filtering_suspicious_lines_with_yield(lines_generator):
    return (line for line in lines_generator if len(running_tests_on_a_line(line)) >=1)


def returning_suspicions_with_row_details(lines_generator):
    for line in lines_generator:
        sus_list = running_tests_on_a_line(line)
        update_statistics(suspicions=sus_list)
        yield (line, sus_list)


def counting_without_loading_into_memory(lines_generator):
    return sum(1 for line in lines_generator)


def chain_generators(path,return_dict=None):
    lines_gen = generates_a_matrix_of_data(path)
    suspicious_gen = filtering_suspicious_lines_with_yield(lines_gen)
    detailed_gen = returning_suspicions_with_row_details(suspicious_gen)
    if return_dict != None:
        return  list(detailed_gen)
    return counting_without_loading_into_memory(detailed_gen)



# d=chain_generators('network_traffic.log',"jj")
# print(d)
# print(total_suspicious_lines)
# print(total_lines_read)
# print(count_for_each_suspicion_type)