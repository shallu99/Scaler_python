

'''Q1. Replace Character
Problem Description

You are given a character string A and two integer ASCII codes B and C.

You have to find and replace all the occurrences of the character having ASCII code equal to B with character having ASCII code equal to C and return the resultant string.


Problem Constraints
1 <= N <= 105
A[i] ∈ ['a'-'z']
97 <= B, C <= 122

Input Format
First argument is a character string A.
Second argument is an integer B.
Third argument is an integer C.
Output Format
Return the resultant string after replacing the character(s).
Example Input
Input 1:
 A = "aabbccbb"
 B = 98
 C = 100
Input 2:
 A = "abc"
 B = 100
 C = 97

Example Output
Output 1:
 aaddccdd
Output 2:
 abc

Example Explanation
Explanation 1:
 Character having ASCII code equal to 98 = 'b'
 Character having ASCII code equal to 100 = 'd'
 Character 'b' occurs at positions 3, 4, 7 and 8 in "aabbaabb".
 After replacing the characters, string becomes "aaddaadd".
Explanation 2:
 Character having ASCII code equal to 100 = 'd'
 Character 'd' is not present in "abc".
 The resultant string is same as string A.

Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: A single String, For e.g 'anagram'
Enter Input Here
Arg 2: A single Integer, For e.g 9
Enter Input Here
Arg 3: A single Integer, For e.g 9
Enter Input Here

'''
class Solution:
    # @param A : string
    # @param B : integer
    # @param C : integer
    # @return a strings
    def solve(self, A, B, C):
        char_to_replace = chr(B)
        replacement_char = chr(C)
        return A.replace(char_to_replace, replacement_char)


'''Q2. Low to High - II
Problem Description

You are given lowercase string (S) and you have to return a string that is the uppercase form of S.

Problem Constraints
1 <= S.size() <= 1000

Input Format
First and only argument containing a lowercase string S.

Output Format
You have to return uppercase form of input string.

Example Input
Input 1:
interviewbit
Input 2:
scaler

Example Output
Output 1:
INTERVIEWBIT
Output 2:
SCALER

Example Explanation
Explanation 1:

Clearly, uppercase of interviewbit is INTERVIEWBIT.
Explanation 2:

Clearly, uppercase of scaler is SCALER.

Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: A single String, For e.g 'anagram'
Enter Input Here
'''
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        return A.upper()

if __name__ == "__main__":
    for inp in A:
        print(solve(A))


'''Q3. Reverse the word - II
Problem Description
You are given lowercase string (A) and you have to return after reversing that.

Problem Constraints
1 <= S.size() <= 1000

Input Format
First and only argument containing a lowercase string S.

Output Format
You have to return string which is reverse form of input string.

Example Input
Input 1:
interviewbit
Input 2:
scaler

Example Output
Output 1:
tibweivretni
Output 2:
relacs

Example Explanation
Explanation 1:
Clearly, reverse of interviewbit is tibweivretni.
Explanation 2:
Clearly, reverse of scaler is relacs.

Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: A single String, For e.g 'anagram'
Enter Input Here
'''

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        return A[::-1]


'''Q6. Divide the tuple
Problem Description:

Write a program to divide a given tuple into two tuples that contain even and odd indexed elements of the original tuple. Print both these tuples in the given output format.

Note: The input tuple follows 1-based indexing. This means the element at index 0 is treated as having index as 1.

For example, (9,2,3). The 1-based index of 2 is 2.

Input Format:

The input contains a tuple as an argument to the function.
Output Format:

Print two tuples one for odd indexed elements and another for even indexed elements in the following format:
Odd: (....)
Even: (....)
Sample Input:

1
(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
Sample Output:

Odd: (10, 5, 10, 10, 5, 8)
Even: (8, 2, 15, 8, 8, 2)'''


def odd_even_split_tuple(tup):
    '''
    input: tup - indicates the input tuple
    output: print two tuples one for even-indexed and one for odd-indexed elements in the given output format
    '''
    # Based on 1-based indexing:
    odd_tuple = tuple(tup[i] for i in range(len(tup)) if (i + 1) % 2 != 0)
    even_tuple = tuple(tup[i] for i in range(len(tup)) if (i + 1) % 2 == 0)

    print("Odd:", odd_tuple)
    print("Even:", even_tuple)


'''Q7. String Manipulation
Problem Description:

Given a string, complete the function modify() that returns the string after performing string modifications according to the following conditions:

1) If the length of the given string is less than 3, leave it unchanged.

2) Otherwise add 'ing' at the end of the given string.

3) If the given string already ends with 'ing' then add 'ly' instead.

Input Format:

First-line will have the number of test cases. For each testcase there will be a single line of input consisting of a string.
Output Format:

Resultant string in string format
Sample Input 1:

1
Am
Sample Output 1:

Am
Sample explanation:

The length of "Am" is lesser than 3 therefore it is returned as it is.
Sample Input 2:

1
Sow
Sample Output 2:

Sowing
Sample explanation:

The length of "Sow" is equal to 3 therefore it is returned after adding 'ing' at the end.

Sample Input 3:

1
string
Sample Output 3:

stringly
Sample explanation:

The length of "string" is greater than 3 and it has 'ing' at the end therefore it is returned after adding "ly" at the end.'''


def modify(s):
    '''Input: s is the string
       Output: return the resultant string with described modifications'''

    if len(s) < 3:
        return s
    elif s.endswith("ing"):
        return s + "ly"
    else:
        return s + "ing"


'''Q8. Extract the error message
Problem Description

You are given a list of strings, where each string represents a log entry from a system.
Your task is to find and print all log entries that contain the word "ERROR".

What is a Log Entry?
A log entry is like a diary note written by a computer.
It records what the computer (or application/server) did at a specific time — such as:

Starting up or shutting down
Displaying errors
User logins/logouts
Performing any important activity
Example Log Entry
2025-08-02 10:30:45 [INFO] Server started successfully
Meaning:
“At 10:30 AM on August 2nd, 2025, the server started without any issue.”


Input Format

The first line contains a single integer N — the number of log entries.

The next N lines each contain a single log entry in the format:

"YYYY-MM-DD HH:MM:SS LEVEL Message"


Output Format

Print only the lines (in order) that contain the log level ERROR.


Example Input

logs = [
    "2024-07-18 10:00:01 INFO Server started",
    "2024-07-18 10:01:17 ERROR Failed to connect to database",
    "2024-07-18 10:02:45 WARNING High memory usage",
    "2024-07-18 10:04:10 ERROR Disk full",
    "2024-07-18 10:06:30 INFO Backup complete"
]


Example Output

2024-07-18 10:01:17 ERROR Failed to connect to database
2024-07-18 10:04:10 ERROR Disk full


Example Explanation

Two lines contain the word ERROR:
    2024-07-18 10:01:17 ERROR Failed to connect to database
    2024-07-18 10:04:10 ERROR Disk full

'''

def extract_error_logs(logs):
    for log in logs:
        if "ERROR" in log:
            print(log)


'''Q9. Print the longest log entry
Problem Description

Given a list of strings where each string represents a line of text, find and print the longest string from the list.
What is a Log Entry?
A log entry is like a diary note written by a computer.
It records what the computer (or application/server) did at a specific time — such as:

Starting up or shutting down
Displaying errors
User logins/logouts
Performing any important activity
Example Log Entry
2025-08-02 10:30:45 [INFO] Server started successfully
Meaning:
“At 10:30 AM on August 2nd, 2025, the server started without any issue.”

Input Format
The only Argument is an array of Strings.

Output Format
Print a single line: the longest string from the list.

Example Input
Input 1:
lines = [
    "DevOps is awesome.",
    "Error: Disk not found.",
    "Server started successfully at 10:05 AM.",
    "OK"
]
Example Output
Output 1:
Server started successfully at 10:05 AM.

'''
def find_longest_line(lines):
    if not lines:
        return  # If the list is empty, do nothing

    longest_line = max(lines, key=len)
    print(longest_line)


'''Q1. First Occurrence
Problem Description

You are given a character string A, having length N and an integer ASCII code B.
You have to tell the leftmost occurrence of the character having ASCII code equal to B, in A or report that it does not exist.

Problem Constraints
1 <= N <= 105
A[i] ∈ ['a'-'z']
97 <= B <= 122

Input Format
First argument is a character string A.
Second argument is an integer B.

Output Format
If there exists an occurrence, return the leftmost index(0 - based), else return -1.

Example Input
Input 1:
 A = "aabbcc"
 B = 98 
Input 2:
 A = "abc"
 B = 100

Example Output
Output 1:
 2 
Output 2:
 -1 


Example Explanation
Explanation 1:

 Character having ASCII code equal to 98 = 'b' 
 Leftmost index of character 'b' in "aabbcc" is 2.
Explanation 2:
 Character having ASCII code equal to 100 = 'd'
 Character 'd' is not present in "abc".

Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: A single String, For e.g 'anagram'
Enter Input Here
Arg 2: A single Integer, For e.g 9
Enter Input Here
'''
class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        target_char = chr(B)  # Convert ASCII code to character
        for i in range(len(A)):
            if A[i] == target_char:
                return i  # Return 0-based index of first occurrence
        return -1  # Character not found

'''Q2. Vowels vs Consonants - II
Problem Description

You are given lowercase string (A) and you have to tell the count of vowels and consonants in it.

Problem Constraints
1 <= A.size() <= 1000

Input Format
First and only argument containing a lowercase string A.

Output Format
You have to return an array of two elements representing count of vowels and consonants in the input string respectively.

Example Input
Input 1:
interviewbit
Input 2:
scaler

Example Output
Output 1:
[5 7]
Output 2:
[2 4]

Example Explanation
Explanation 1:
Clearly, interviewbit has 4 vowels and 7 consonants.
Explanation 2:
Clearly, scaler has 2 vowels and 4 consonants.

Expected Output
Provide sample input and click run to see the correct output for the provided input. 
Use this to improve your problem understanding and test edge cases'''


class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        vowels = set('aeiou')
        vowel_count = 0
        consonant_count = 0

        for char in A:
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

        return [vowel_count, consonant_count]


'''Q7. Characters Swap
Problem Description:

Write a program to return a single string from two given strings, separated by a space. Swap the first two characters of the first string (s1) with the first two characters of the second one (s2).

Input Format:

The first line of input contains an integer t denoting the number of test cases.
The next 2t lines contain strings s1 and s2.
The two arguments to the function are the strings s1 and s2.
Output Format:

Resultant string.
Sample Input:

1
abc
xyz
Sample Output:

xyc abz
Sample explanation:

The first two characters of string abc are ab which are swapped with xy of xyz and both the strings are joined by space.'''
def swap(s1, s2):
    string = s2[:2] + s1[2:] + ' ' + s1[:2] + s2[2:]
    return string


'''Q8. Palindrome or not
Problem Description:

Write a program to check whether the given string is a palindrome or not. Return True if it is palindrome else return False.

Note: A string is said to be a palindrome if the reverse of the string is the same as the string itself.

Input Format:

First line will have the number of test cases. For each testcase there will be single line of input consisting of a string.
Output Format:

True if palindrome else False
Sample Input 1:

1
level
Sample Output 1:

True
Sample explanation:

'level' when reversed returns 'level' only which are same therefore True is returned.
Sample Input 2:

1
Scaler
Sample Output 2:

False
Sample explanation:

'Scaler' when reversed returns 'relacS' which is not equal to original string therefore False is returned.'''
def isPalindrome(s):
    # s[::-1] will be the reverse of s
    return s == s[::-1]


''''Q9. No. of Alphabets & Digits
Problem Description:

Write a program that takes a sentence as a parameter and returns the number of alphabets and digits separately.

Input Format:

First line will have the number of test cases. For each testcase there will be one line of input consisting
of string/sentence in string format.
Output Format:

Count of alphabets and digits in the given string.
Sample Input:

1
John.Smith1990@gmail.com
Sample Output:

Number of alphabets:  17
Number of Digits:  4
Sample explanation:

The four digits are 1,9,9, and 0. The 17 alphabets are J,o,h,n,S,m,i,t,h,g,m,a,i,l,c,o and m.'''


def alphandig_count(s):
    count_digit = 0
    count_alpha = 0
    # count_digit will have count of digits
    # count_alpha will have count of alphabets
    for i in s:
        if i.isdigit():
            count_digit = count_digit+1
        elif i.isalpha():
            count_alpha = count_alpha+1
    return count_alpha, count_digit