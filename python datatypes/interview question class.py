
'''
Question 2
Real-time Network Stats
Let’s say you're monitoring a system to track internet traffic — how much data your computer or server is sending and receiving over time. Two main parts:

bytes_sent: Data sent out
bytes_recv: Data received
Sometimes, something weird happens — like a huge spike in data usage. This is called an anomaly (something unusual).

Our goal is to:

Detect if a certain time period had suspiciously high network usage — like 5 times higher than usual.
'''
import datetime

NETWORK_DATA = {
    'time_1': {'bytes_sent': 1000, 'bytes_recv': 2000},
    'time_2': {'bytes_sent': 1500, 'bytes_recv': 2500},
    'time_3': {'bytes_sent': 2000, 'bytes_recv': 3000},
    'time_4': {'bytes_sent': 50000, 'bytes_recv': 60000}
}

period_to_check = 'time_4'

# output = True
def detect_network(NETWORK_DATA,period_to_check):
    current_data = NETWORK_DATA[period_to_check]

    total_sent_byte = 0
    total_recv_byte = 0


    for period , data in NETWORK_DATA.items():
         if period != period_to_check:
             total_recv_byte += data['bytes_recv']
             total_sent_byte +=data['bytes_sent']

    avg_total_recv_bye = total_recv_byte/(len(NETWORK_DATA) -1)
    avg_total_sent_bye = total_sent_byte/(len(NETWORK_DATA) -1)

    if current_data['bytes_sent'] >5*avg_total_sent_bye or current_data['bytes_recv'] >5*avg_total_recv_bye:
        return True
    return False
print(detect_network(NETWORK_DATA, period_to_check))



'''
Question 3 
Service Log Rotator
What Are Logs?

When computers or apps run, they constantly write down what they’re doing in a file — just like a diary or notebook.

These records are called logs. Logs help teams understand what happened, when it happened, and if anything went wrong.

Why Rotate or Remove Logs?

Imagine if every activity is recorded and nothing is ever deleted — the system could fill up with old, unnecessary data.

So in DevOps, we regularly rotate logs: Meaning: We remove old or very large logs to save space and keep only recent and useful information.

🎯 What’s the Goal Here?

We want to write a Python function that:

Keeps only the logs that are recent (within a certain number of days from a fixed date).

And are small enough (don’t take too much space).

Problem Statement

Implement a function that filters a list of log entries, retaining only those logs that:

Are within a specified number of days from a fixed reference date (November 15, 2023), AND
Do not exceed a given size in kilobytes (KB).
Each log is represented as a dictionary with the keys "date" and "size_kb".
'''
# Solution
from datetime import datetime
logs = [
    {"date": "2023-11-01", "size_kb": 100},
    {"date": "2023-10-15", "size_kb": 500},
    {"date": "2023-11-10", "size_kb": 300}
]
max_size_kb = 400
days_to_keep = 30

def filter_logs(logs, max_kb, day_keep):
  reference_date = datetime(2023,11,15).date() # finding the reference date
  result = []
  for log in logs:
    log_date = datetime.strptime(log['date'], '%Y-%m-%d').date()
    day_diff = (reference_date - log_date).days
    if day_diff > day_keep or log['size_kb'] > max_kb:
      continue
    result.append(log)
  return result

print(filter_logs(logs, max_size_kb, days_to_keep))


'''
question 4
Most requested URL from Log
Problem Description:

You are given a web server access log. Each line contains an HTTP request. Your task is to parse the log and return the URL (request target) that was requested the most times.

Ignore HTTP method, protocol version, status code, and other fields — only the request target matters.

If multiple URLs have the same highest request count, return the one which attains the highest count first while scanning the file from top to bottom.

Input Format: A plain text access log with one entry per line, where each request is represented in quotes as: METHOD <URL> HTTP/<version>.

Output Format: Return the most frequently requested URL as a string.
'''
import re
# precompile the regex for better TC
regex = re.compile(r'"([A-Z]+)\s+(\S+)\s+HTTP/\d+(?:\.\d+)?"')

def most_used_url(filepath):
  count = {} # freq dictionry
  best_url = ''
  best_count = 0

  # opening the file in read
  with open(filepath, 'r', encoding='utf-8') as f:
    # reading file line by line
    for line in f:
      # searching regex in the line
      m = regex.search(line)
      # if no match found continue
      if not m:
        continue
      # get the group having url
      url = m.group(2)
      # update the frequency
      count[url] = count.get(url,0) +  1
      # check if the frequency is highest
      if best_count < count[url]:
        # update
        best_count = count[url]
        best_url = url
        print(best_url)
  return best_url


most_used_url(r'logfilestopractice/interview_question_class_q4_llogs.txt')

'''
Extract Non-200 HTTP Status Code Logs
You are given the path to a log file.
Each line in the file may contain an HTTP status code such as 200, 404, 500, etc.

Your task is to find and return all log lines that contain a non-200 HTTP status code.

Only the first 3-digit number in each line is considered the status code.
Ignore lines that do not contain any 3-digit number.
HTTP status codes are always 3-digit integers.
Input Format
Log File
Contains multiple lines.
Each line may or may not contain an HTTP status code.
Output Format
Return a list of strings, where each string is a log line whose first status code is not 200.
If no lines match, return an empty list.
Example
File Content
[INFO] 2025-08-08 12:01:03 GET /index.html 200 OK
[WARNING] 2025-08-08 12:01:10 GET /not-found 404 Not Found
[ERROR] 2025-08-08 12:01:15 GET /server-error 500 Internal Server Error
[INFO] 2025-08-08 12:01:20 GET /health 200 OK
[DEBUG] Something unrelated to HTTP
Expected Output
[
  "[WARNING] 2025-08-08 12:01:10 GET /not-found 404 Not Found",
  "[ERROR] 2025-08-08 12:01:15 GET /server-error 500 Internal Server Error"
]
Explanation
Line 1 → Status code = 200 → ignored
Line 2 → Status code = 404 → included
Line 3 → Status code = 500 → included
Line 4 → Status code = 200 → ignored
Line 5 → No status code → ignored
Constraints
The log file can contain up to 10⁵ lines.
Each line length ≤ 200 characters.
Status codes are always 3-digit integers.
The first occurrence of a 3-digit number is always treated as the status code.
Notes
Only the first 3-digit number in each line is evaluated.
Ignore lines with no 3-digit number.'''

import re
from typing import List

def non_200_status_lines(file_path: str) -> List[str]:
    """
    Reads a log file and returns all lines whose first HTTP status code is not 200.

    :param file_path: Path to the input log file
    :return: List of lines with non-200 status codes
    """
    result = []
    status_code_pattern = re.compile(r"\b(\d{3})\b")  # match first 3-digit number

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = status_code_pattern.search(line)
            if not match:
                continue
            status_code = int(match.group(1))
            if status_code != 200:
                # preserve original spacing/tabs, just drop trailing newline
                result.append(line.rstrip("\n"))
                # print(result)
    return result

non_200_status_lines( r'logfilestopractice/Extract Non-200 HTTP Status Code Logs.txt')


'''
Simple Load Balancer
Problem Description

You are given two integers:
requests → the total number of requests to be handled
instances → the number of available server instances

Your task is to distribute the requests among the instances as evenly as possible.
If the requests cannot be evenly divided, the extra requests should be assigned to the first few instances.

Return a list where each element represents the number of requests assigned to a corresponding instance.


Problem Constraints

1 ≤ instances ≤ 109
1 ≤ requests ≤ 105
instances ≤ requests


Input Format

First Argument, requests: int — total number of requests.
Second Argument, instances: int — number of server instances.


Output Format

Return a list of integers of length instances.
Each element represents the number of requests assigned to the corresponding instance.


Example Input

Input 1:
requests = 9
instances = 3
Input 2:
requests = 7
instances = 4


Example Output

Output 1:
[3, 3, 3]
Output 2:
[2, 2, 2, 1]


Example Explanation

Explanation 1:
Since the requests can be divided evenly among the instances, each instance receives the same number of requests as 3.
Explanation 2:
The requests cannot be evenly divided. 

Each instance gets at least 1 request, and the extra requests are given to the first few instances as [2, 2, 2, 1].

'''

from typing import List


def distribute_load(requests: int, instances: int) -> List[int]:
    # Base load for every instance
    base = requests // instances
    # Extra requests to be distributed
    extra = requests % instances

    # First 'extra' instances get (base + 1), rest get base
    result = [base + 1 if i < extra else base for i in range(instances)]
    return result



