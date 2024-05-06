# Your Verkada security camera is part of your Enterprise IT Network. You're trying to debug an issue, so you need to consult your data logs. You're mainly interested in seeing which devices are communicating with each other, so you'd like to find all the IP addresses within the logs.

# You have a hierarchy of directories and some files in some of those directories:

# /root/data/dir1/file1.txt, file2.txt, ... 
# /root/data/dir2/file3.txt, file4, ...
# /root/data/file6.in, file7.out, ...
# ...
# Some of these files contain IP addresses inside the text. An IP address is a string of form x.x.x.x where each x is a number from 0 to 255.

# For example, say we have file1.txt that looks like this:

# hello world 127.0.0.1 
# this is some example 128.99.107.55 
# file with some correct and incorrect 128.128.4.11 ip 0.11.1115.78 addresses
# It contains only 3 IP addresses, namely 127.0.0.1, 128.99.107.55, 128.128.4.11, since 0.11.1115.78 is not a valid IP address (specifically because 1115 is too big).

# Your task is to find all distinct IP addresses from all the files in the /root/data/ directory, and print them in lexicographical order.

# Example

# For the following /root/data directory

# /root/data/dir1/file1.txt

#     hello world 127.0.0.1 
#     this is some example 128.99.107.55 
#     file with some correct and incorrect 128.128.4.11 ip 0.11.1115.78 addressesaddresses
# /root/data/dir1/file2.txt

#     hello from 74.0.65.76 and 8.dd.99.88.907 good
#     this is some example 306.5.76.35 
#     file with some correct and incorrect 15.128.4.65 ip addresses
#     0.0.0.0
# /root/data/dir2/file3.txt

#     127.65.64.1 127.0.64.1 127.0.0.1
#     exaMple 128.57.107.76 128.57.907.70 
#     file with some correct and incorrect 67.128.4.11 ip addresses 7.7.7.8
# /root/data/dir2/file4.txt

#     hello world 127.98.0.1 
#     this is some example 128.96.107.55 
#     file with some correct and incorrect 128.68.4.11 ip addresses
# /root/data/f.inp

#     hello world 127.0.49.1 
#     this is some example 128.99.58.55 8.88.888.88 77.255.255.254
#     7.7.257.25 file with some correct and incorrect 26.56.4.23 ip addresses
# The output should be

# 0.0.0.0
# 127.0.0.1
# 127.0.49.1
# 127.0.64.1
# 127.65.64.1
# 127.98.0.1
# 128.128.4.11
# 128.57.107.76
# 128.68.4.11
# 128.96.107.55
# 128.99.107.55
# 128.99.58.55
# 15.128.4.65
# 26.56.4.23
# 67.128.4.11
# 7.7.7.8
# 74.0.65.76
# 77.255.255.254


# import requests
# import mysql.connector
# import pandas as pd

import os
import re

def extract_ip_addresses(file_path):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = set()
    with open(file_path, 'r') as file:
        for line in file:
            ips = re.findall(ip_pattern, line)
            for ip in ips:
                if is_valid_ip(ip):
                    ip_addresses.add(ip)
    return ip_addresses

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False
    return True

def find_all_ip_addresses(directory):
    ip_addresses = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            ip_addresses.update(extract_ip_addresses(file_path))
    return sorted(ip_addresses)

# Example usage:
directory = "/root/data"
all_ip_addresses = find_all_ip_addresses(directory)
for ip in all_ip_addresses:
    print(ip)
