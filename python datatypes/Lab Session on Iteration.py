'''Q1. Stair Pattern
Problem Description

Take an integer N as input, print the corresponding stair pattern for N.
For example if N = 4 then stair pattern will be like:
*
**
***
****

Problem Constraints
1 <= N <= 100

Input Format
First and only line of input contains a single integer N.

Output Format
Output the stair pattern corresponding to the given N.

Example Input
Input 1:
 2
Input 2:
 3

Example Output
Output 1:

 *
 **
Output 2:

 *
 **
 ***

Example Explanation
 Print the pattern as described.

'''

def main():
    N = int(input().strip())

    for i in range(1, N + 1):
        print('*' * i)

    return 0

if __name__ == '__main__':
    main()


'''Q2. Is It Prime?
Problem Description
Take an integer A as input, you have to tell whether it is a prime number or not.
A prime number is a natural number greater than 1 which is divisible only by 1 and itself.
Problem Constraints
1 <= A <= 106
Input Format
First and only line of the input contains a single integer A.

Output Format
Print YES if A is a prime, else print NO.

Example Input
Input 1:
 3 
Input 2:
 4 

Example Output
Output 1:
 YES 
Output 2:
 NO 

Example Explanation
Explanation 1:
 3 is a prime number as it is only divisible by 1 and 3.
Explanation 2:
 4 is not a prime number as it is divisible by 2.

'''

A = int(input().strip())

if A <= 1:
    print("NO")
else:
    for i in range(2, int(A**0.5) + 1):
        if A % i == 0:
            print("NO")
            break
    else:
        print("YES")

'''Q3. Print N stars
Problem Description

Given an integer N, print N stars in a single line.

For example if N = 5 then pattern will be like:
*****
Problem Constraints
2 <= N <= 100

Input Format
Single line input contains a single integer N.


Output Format
Output N stars in a single line.


Example Input
Input 1:
 2
Input 2:
 3

Example Output
Output 1:
**
Output 2:
***

Example Explanation
 Print the pattern as described.

'''
def main():
    N = int(input().strip())
    print('*' * N)

if __name__ == '__main__':
    main()

'''Q4. Print a matrix of stars
Problem Description
Given two integers N and M as inputs, print a rectangle of N * M stars.

For example if N = 3, M = 4 then pattern will be like:
****
****
****

Problem Constraints
2 <= N, M <= 100

Input Format
First line of input contains an integers N (no of rows).
Second line of input contains an integer M (no of cols).

Output Format
Output N * M rectangle of stars.

Example Input
Input 1:
 2
 3
Input 2:
 3
 1

Example Output
Output 1:
***
***
Output 2:
*
*
*

Example Explanation

 Print the pattern as described.

'''
# write here

N = int(input().strip())
M = int(input().strip())

for _ in range(N):
    print('*' * M)

'''Q8. Sum of digits
Problem Description

You take an integer N as input. Your task is to calculate and print the sum of the digits of the given number N.

Problem Constraints
0 <= N <= 109

Input Format
The first line contains an integer N.

Output Format
Print an Integer, denoting the sum of the digits of the input integer.

Example Input

Input 1:
5
Input 2:
123
Input 3:
1589

Example Output

Output 1:
5
Output 2:
6
Output 3:
23

Example Explanation

Explanation 1:
5 has only 1 digit hence sum is 5.
Explanation 2:
For the number 123, the digits are 1,2,3. The Sum(123) = 1+2+3 = 6.
Explanation 3:
For the number 1589, the digits are 1,5,8,9. The Sum(1589) = 1+5+8+9 = 23.

'''


def main():
    # Input: Read the integer N
    N = int(input())

    # Initialize the sum of digits
    digit_sum = 0

    # Process each digit of N
    while N > 0:
        digit_sum += N % 10  # Add the last digit to the sum
        N //= 10  # Remove the last digit from N

    # Output: Print the sum of digits
    print(digit_sum)


if __name__ == '__main__':
    main()


'''Q9. Reverse a NumberProblem Description
You are given a number A. Your task is to reverse its digits of A and return the resulting number.
Problem Constraints
0 <= A <= 109

Input Format
The only argument is an Integer A

Output Format
Return a single integer representing the reversed number

Example Input
Input 1:
A = 321
Input 2:
A = 120

Example Output
Output 1:
123
Output 2:
21

Example Explanation
Explanation 1:
A = 321, reversing its digits gives 123.
Explanation 2:
A = 120, reversing its digits gives 021, but leading zeros are removed, so the final output is 21.

Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: A single Integer, For e.g 9
Enter Input Here
'''


class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        # Determine the sign of A
        sign = -1 if A < 0 else 1
        A = abs(A)

        # Reverse the digits of A
        reversed_A = 0
        while A > 0:
            reversed_A = reversed_A * 10 + A % 10
            A //= 10

        # Restore the sign and return the result
        return sign * reversed_A

'''Q1. Numeric Stair Pattern
Problem Description

Take an integer N as input, print the corresponding pattern for N.
For example if N = 4 then pattern will be like:

1
1 2
1 2 3
1 2 3 4

NOTE: There should be no extra spaces after last integer.


Problem Constraints
1 <= N <= 100

Input Format
First and only line of input contains a single integer N.

Output Format
Output the pattern corresponding to the given N.

NOTE:

There should be no extra spaces after last integer and before first integer in any row.
All integers in any row in the pattern are space separated.

Example Input
Input 1:
 2
Input 2:
 3
Example Output
Output 1
1
1 2
Output 2:
1
1 2
1 2 3

Example Explanation
 Print the pattern as described.

'''


def main():
    # Input: Read the integer N
    N = int(input())

    # Generate and print the pattern
    for i in range(1, N + 1):
        print(" ".join(str(j) for j in range(1, i + 1)))


if __name__ == '__main__':
    main()


'''Q2. Inverted Numeric Pyramid
Problem Description

Take an integer N as input, print the corresponding Numeric Inverted Half Pyramid pattern for N.

For example if N = 4 then pattern will be like:

1 2 3 4
1 2 3
1 2
1

Problem Constraints

1 <= N <= 100

Input Format

First and only line of input contains a single integer N.

Output Format
Output the Numeric Inverted Half Pyramid pattern corresponding to the given N.

NOTE: There should be no extra spaces after last integer and before first integer in any . All integers in any row in the pattern are separated by a single space.

Example Input
Input 1:
 2
Input 2:
 3

Example Output
Output 1:

1 2
1
Output 2:
1 2 3
1 2
1

Example Explanation
 Example Input 1
 We have the input of integer as 2. So there will be 2 rows. 
 The first row will have 2 integers separated by a single space (1 2)
 The next row will have 2-1 = 1 integer (1)
 As we do not have any more integers left we stop printing the pattern.

 Example Input 2
 We have the input of integer as 3. So there will be 3 rows. 
 The first row will have 3 integers separated by a single space (1 2 3)
 The next row will have 3-1 = 2 integers separated by a single space (1 2)
 The next row will have 2-1 = 1 integer.(1)
 As we do not have any more integers left we stop printing the pattern.

'''


def main():
    # Input: Read the integer N
    N = int(input())

    # Generate and print the inverted half pyramid pattern
    for i in range(N, 0, -1):
        print(" ".join(str(j) for j in range(1, i + 1)))


if __name__ == '__main__':
    main()


'''Q3. Count the digits
Problem Description
Take T (number of test cases) as input.
For each test case, take integer N as input and Print the count of digits of that number.

Note: No of digits for number 0 is considered as 1.

Problem Constraints

1 <= T <= 1000
0 <= N <= 100000000

Input Format

The first line is the number T which denotes the total number of test cases.
Next T lines contain an integer N for which you have to print the number of digits.
Output Format

For T different Numbers, Print the number of digits in separate lines.
Example Input

Input 1: 
2
0
1

Input 2:
2
100
10101
Example Output

Output 1:
1
1
Output 2:
3
5
Example Explanation

Explanation 1:
0 and 1 both have only one digit.
Explanation 2:
100 has three digits and 10101 has 5 digits.'''


def main():
    # Input: Read the number of test cases
    T = int(input())

    # Process each test case
    for _ in range(T):
        # Input: Read the integer N
        N = int(input())

        # Count the number of digits using string conversion
        digit_count = len(str(N))

        # Output: Print the digit count
        print(digit_count)


if __name__ == '__main__':
    main()

'''Q4. Two Line Star Pattern
Problem Description

Print a pattern consisting of N rows, where each row contains an asterisk (*) at the beginning and end of the line, with N-2 spaces in between.

The Pattern should look like:

*<N-2 Spaces>*

Print the above pattern for a total of N Rows.

Refer Example ouput, for better clarification.

Problem Constraints
2 <= N <= 100

Input Format
First and only line of input contains a single integer N.

Output Format
Output the pattern corresponding to the given N.

Example Input
Input 1:
 2
Input 2:
 4

Example Output
Output 1:
**
**
Output 2:
*  *
*  *
*  *
*  *


Example Explanation

Explanation 1:
 Here N = 2,  So each row should have N - 2 spaces which is 0.
 Thus the N rows(i.e, 2 rows) should be in the form (asterisk)(0 spaces)(asterisk)
Explanation 2:
 Here N = 4,  So each row should have N - 2 spaces which is 2.
 Thus the N rows(i.e, 4 rows) should be in the form (asterisk)(2 spaces)(asterisk)

'''


def main():
    # Input: Read the integer N
    N = int(input())

    # Generate and print the pattern
    for _ in range(N):
        print("*" + " " * (N - 2) + "*")


if __name__ == '__main__':
    main()

'''Q5. HCF - Easy
Problem Description
Write a program to input two integers A & B from user and print their HCF.

Definition Of HCF: The HCF(Highest Common Factor) or the GCD(greatest common divisor) of two positive integers happens to be the largest positive integer that divides the numbers without leaving a remainder.


Problem Constraints

1 <= A,B <= 100000

Input Format
First line will contain 2 integers A and B

Output Format
An integer which is the HCF of A & B.

Example Input
Input 1:
15 105 
Input 2:
24 36 

Example Output
Output 1:
15
Output 2:
12

'''

import math


def main():
    # Input: Read two integers A and B
    A, B = map(int, input().split())

    # Calculate the HCF using math.gcd
    result = math.gcd(A, B)

    # Output: Print the HCF
    print(result)


if __name__ == '__main__':
    main()
