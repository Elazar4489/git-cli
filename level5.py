from level4 import *


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
