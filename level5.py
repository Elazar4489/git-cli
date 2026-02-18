import level4 as f

def analyze_log(path):
    d=f.chain_generators(path,"jj")
    tyu={i[0][1]:i[1] for i in d}
    return tyu

def generate_report(path):
    suspicious_dict=analyze_log(path)
    IPs_report= (f"{"="*60}\n{" "*10}דוח תעבורה חשודה{" "*10}\n{"="*60}\n\n{" "*10}סטטיסטיקות כלליות{" "*10}\n\n"
           f"שורות שנקראו: {f.total_lines_read} -\n שורות חשודות: {f.total_suspicious_lines} -\n"
           f"{"\n".join([f"- {k}: {v}" for k,v in f.count_for_each_suspicion_type.items()])}\n\n"
           f"{" "*10}IPs עם רמת סיכון גבוהה (3+ חשדות)\n\n"
           f"{"\n".join([f"- {k}: {", ".join(v)}" for k,v in suspicious_dict.items() if len(v) >= 3])}\n\n"
           f"{" "*10}IPs חשודים נוספים\n\n"
           f"{"\n".join([f"- {k}: {", ".join(v)}" for k,v in suspicious_dict.items() if len(v) < 3])}")
    return IPs_report

