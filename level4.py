from level3 import *

def generates_a_matrix_of_data(path):
    with open(path, 'r', encoding="utf-8") as log:
        for line in log:
            line=[w for w in line.split(",")]
            yield list(line)

def filtering_suspicious_lines_with_yield(lines_generator):
    return (line for line in lines_generator if len(running_tests_on_a_line(line)) >=1)


def returning_suspicions_with_row_details(lines_generator):
    return ((line,running_tests_on_a_line(line))  for line in lines_generator)

def counting_without_loading_into_memory(lines_generator):
    return sum(1 for line in lines_generator)


def chain_generators(path):
    lines_gen = generates_a_matrix_of_data(path)
    suspicious_gen = filtering_suspicious_lines_with_yield(lines_gen)
    detailed_gen = returning_suspicions_with_row_details(suspicious_gen)
    total_count = counting_without_loading_into_memory(detailed_gen)
    return total_count
