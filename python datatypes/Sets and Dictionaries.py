'''Q4. Frequency of Characters
Problem Description:

Given an input string, write a program to count the frequency of each character in the string. Map the characters and their respective frequency into a dictionary and return that dictionary.

Note: In the back-end, we are just checking the items in the dictionary, not the order therefore True will be printed if the returned dictionary has the same items as expected otherwise False will be printed.

Input Format:

The first and the only arguement to the function is a string.
Output Format:

Returned output must be in a dictionary format. The keys must be the unique characters in the string, and the values should
be the frequency of those characters in the given string.
Sample Input:

ABC
Sample Output:

{'A': 1, 'B': 1, 'C': 1}
Output Explanation:

In the string 'ABC', there are three unique characters: 'A', 'B', and 'C'.
They occur once in the string and hence their count values are 1.'''

def dict_freq(str1):
    '''str1 is a string
       Ouput -> A dictionary is expected to be returned'''
    dict1 = {}
    for n in str1:
        if n in dict1:
            dict1[n] += 1
        else:
            dict1[n] = 1
    return dict1
    # YOUR CODE GOES HERE


'''Q7. Distributed Log Aggregator
Problem Description

In a distributed system, logs are generated across various services such as Database, Authentication, Billing, etc. Each service maintains its own set of logs, where each log entry contains a timestamp, a log level, and a descriptive message.

Your task is to merge all log entries from these different services into a single chronologically ordered list, based on their timestamps, and print them, in the below format.

Each line must follow exactly this format:

YYYY-MM-DD HH:MM:SS [LEVEL] message

Input Format
You are given a dictionary named logs where:
Each key is a string representing the name of the log source (e.g., "Database_logs", "Auth_logs").
Each value is a list of dictionaries, where each dictionary represents a single log entry.

Each log dictionary has the following keys:
"timestamp": A string in the format "YYYY-MM-DD HH:MM:SS"
"level": One of "INFO", "WARNING", or "ERROR"
"message": A string representing the log description

Output Format
Print all log entries sorted by timestamp in ascending order.
Each line must follow exactly this format:
YYYY-MM-DD HH:MM:SS [LEVEL] message

Example Input

Input 1:
logs = {
  "Database_logs": [
    { "timestamp": "2024-07-18 10:15:00", "level": "ERROR", "message": "Database connection failed" },
    { "timestamp": "2024-07-18 14:42:00", "level": "INFO", "message": "Backup Started" }
  ],
  "Authentication_logs": [
    { "timestamp": "2024-07-18 14:00:00", "level": "ERROR", "message": "External Authentication Service Down" },
    { "timestamp": "2024-07-18 10:24:00", "level": "WARNING", "message": "Suspicious login attempt detected" },
    { "timestamp": "2024-07-18 14:47:00", "level": "WARNING", "message": "Multiple attempts detected" }
  ]
}

Example Output
Output 1:
2024-07-18 10:15:00 [ERROR] Database connection failed
2024-07-18 10:24:00 [WARNING] Suspicious login attempt detected
2024-07-18 14:00:00 [ERROR] External Authencation Service Down
2024-07-18 14:42:00 [INFO] Backup Started
2024-07-18 14:47:00 [WARNING] Multiple attempts detected

Example Explanation
Explanation 1:
All log entries sorted by timestamp in ascending order.  

'''

from typing import List, Dict


def merge_logs(logs: Dict[str, List[Dict[str, str]]]):
    all_logs = []

    for server_logs in logs.values():  # key is used, so using the values only
        for log in server_logs:
            all_logs.append(log)

    all_logs = sorted(all_logs, key=lambda x: x['timestamp'])

    for log in all_logs:
        print(f"{log['timestamp']} [{log['level']}] {log['message']}")


'''Q8. Dynamic Port Allocato
Problem Description

You are developing a new application that requires allocating a certain number of free network ports within a specific range, defined by a starting port (start_range) and an ending port (end_range), both inclusive.
Some ports in this range are already in use(used_ports) and cannot be assigned.
Your task is to find the first n available ports within the given range and print them in ascending order, one port per line.
It is guaranteed that there will be enough free ports available in the specified range to meet the requirement.
Problem Constraints

1 ≤ n ≤ 10^5
0 ≤ start_range ≤ end_range ≤ 10^6
used_ports are unique
Input Format

n → Number of free ports required to be allocated.
used_ports → List of ports that are already in use and cannot be allocated.
start_range → Starting port number of the allocation range (inclusive).
end_range → Ending port number of the allocation range (inclusive).
Output Format

Print the first n available ports, each on a separate line, in ascending order.
Example Input

Input 1:
n = 3
used_ports = [8000, 8001, 8004, 8007]
start_range = 8000
end_range = 8008
Example Output

Output 1:
8002
8003
8005
Example Explanation

Explanation 1:
Available ports are 8002, 8003, 8005, 8006, 8008\.    
We have to pick the first n available ports, i.e., 8002, 8003 and 8005'''

from typing import List

def allocate_ports(n: int, used_ports: List[int], start_range: int, end_range: int) -> None:
    """
    Prints the first n available network ports within the inclusive range [start_range, end_range],
    skipping ports in used_ports. Each available port is printed on its own line, in ascending order.
    """
    used_set = set(used_ports)
    count = 0
    for port in range(start_range, end_range + 1):
        if port not in used_set:
            print(port)
            count += 1
            if count == n:
                break


'''Q3. Sum of Values
Problem Description:

Given a dictionary, find the sum of values of every key in the dictionary.

Input Format:

The input contains two lines.
The first line has space-separated string values which are the keys of the dictionary.
The second line has space-separated integer numbers which are the values of the dictionary.
Output Format:

Print the sum of the values of the items as an integer.
Sample Input:

x y z
25 25 50
Sample Output:

100
Output Explanation:

The dictionary has three key-value pairs having values 25, 25, and 50. Hence their sum, 25+25+50 = 100 should be printed.'''

def returnSum(dict):
    sum = 0
    # dict.values() will have all the values of dictionary
    for i in dict.values():
          sum = sum + i
    print(sum)



'''Q4. Adding Common Keys
Problem Description:

Given two dictionaries, write a program for creating a dictionary in such a way that it consists of all the keys that are common in both dictionaries. The values corresponding to the keys in this new dictionary are the sum of the values of those keys in the two dictionaries.

Input Format:

The input contains four lines.
The first line is space-separated string values which are the keys of the first dictionary.
The second line is space-separated integer numbers which are values of the first dictionary.
The third line is space-separated string values which are the keys of the second dictionary.
The second line is space-separated integer numbers which are values of the second dictionary.
Output Format:

Print the resultant dictionary containing added values for common keys.
Sample Input:

a b c
1 2 3
c d e
4 5 6
Sample Output:

{'c': 7}
Output Explanation:

Given the two dictionaries, {'a': 1, 'b': 2, 'c': 3} and {'c': 4, 'd':5. 'e', 6}, key 'c' is common having values 3 and 4. 
Therefore, their sum 7 with the key 'c' should be added in to the resultant dictionary.'''

def commonKey(d1, d2):
  dict3 = {}
  # iterating over d2 keys
  for key in d2:
      if key in d1:
          dict3[key] = d2[key] + d1[key]
      else:
          pass

  print(dict3)


'''Q5. Length of unique words
Problem Description:

Given two sentences, write a program to return the sum of the total number of unique words from each sentence.

Input Format:

The first line indicates the number of test cases.There will be two lines of inputs for each test cases as following:
The two lines consist of two sentences in string format.
Output Format:

The number of unique words from the sentences in integer format.
Sample Input:

1
in data analysis we use data and process it further to create better interpreted data
more and more data will be passively collected
Sample Output:

20
Sample explanation:

{'use', 'process', 'create', 'better', 'analysis', 'in', 'it', 'further', 'and', 'we', 'data', 'interpreted', 'to'} 
represent the 13 unique words from sentence1 and {'collected', 'more', 'be', 'and', 'data', 'passively', 'will'} 
represent the 7 unique words from sentence2. Therefore 13 + 7 = 20 is returned.
Note:

If a word is present in both sentences it should be counted separately for both sentences.'''


def set_operation(sent1,sent2):
  sen_1_words = sent1.split()
  sen_2_words = sent2.split()
  # In set we will have only distinct words
  a = set(sen_1_words)
  b = set(sen_2_words)
  return (len(a) + len(b))