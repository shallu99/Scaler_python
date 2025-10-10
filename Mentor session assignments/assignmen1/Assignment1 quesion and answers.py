'''
Q1. Find Top 10 IPs by Frequency
'''
import  re
from collections import Counter
def countofIP(file_path):
    ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    with open(file_path) as file:
        content =file.read()
        ips = re.findall(ip_pattern, content)
        count = Counter(ips)
        top10 =count.most_common(10)
    for ip, count in top10 :
        print(f"{ip} -> {count} times")
    return top10

countofIP(file_path="sample_apache_logs.txt")

