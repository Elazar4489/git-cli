from level3 import *

def generates_a_matrix_of_data(path):
    with open(path, 'r', encoding="utf-8") as log:
        for line in log:
            line=[w for w in line.split(",")]
            yield list(line)

def filtering_suspicious_lines_with_yield(path):
    k=[line for line in generates_a_matrix_of_data(path) if len(running_tests_on_a_line(line)) >=1]
    return k

def returning_suspicions_with_row_details(path):
    k = [(line,running_tests_on_a_line(line))  for line in generates_a_matrix_of_data(path) if len(running_tests_on_a_line(line)) >= 1]
    return k

def counting_without_loading_into_memory(path):
    counter=sum(1 for line in generates_a_matrix_of_data(path) if len(running_tests_on_a_line(line)) >=1)
    return counter
