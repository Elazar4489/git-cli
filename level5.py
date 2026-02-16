import level4 as f

def analyze_log(path):
    d=f.chain_generators('network_traffic.log',"jj")
    tyu={i[0][1]:i[1] for i in d}
    return tyu

