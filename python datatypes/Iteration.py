'''q1
Write a program that takes a positive integer N as input from the user and prints all natural numbers from 1 to N, with each number followed by a space (including the last number).

Problem Constraints

1 <= N <= 1000000

Input Format
A single line representing N

Output Format
N space separated integers from 1 to N, with each number followed by a space, including the last number.

Example Input
Input 1:
5
Input 2:
10
Example Output
Output 1:
1 2 3 4 5
Output 2:

1 2 3 4 5 6 7 8 9 10
'''
def main():
    # write your code and logic here
  # Read input
    N = int(input())

    # Print numbers from 1 to N, each followed by a space
    for i in range(1, N + 1):
        print(i, end=' ')
if __name__ == "__main__":
    main()

'''q2
Problem Description

Write a program to print all Natural numbers from N to 1 where you have to take N as input from user

Problem Constraints
1 <= N <= 10000000

Input Format
A single line representing N

Output Format
N space separated integers from N to 1.

Example Input
Input 1:
5
Input 2:
10

Example Output
Output 1:
5 4 3 2 1 
Output 2:
10 9 8 7 6 5 4 3 2 1 

'''

# write code here
def main():
    # Read input
    N = int(input())

    # Print numbers from N to 1, each followed by a space
    for i in range(N, 0, -1):
        print(i, end=' ')

if __name__ == "__main__":
    main()

'''q3
Write a program to print all odd numbers from 1 to N where you have to take N as input from user. Here N is inclusive.

Note:
Each number should be followed by a space, including the last number.

Problem Constraints
1 <= N <= 2000000

Input Format
A single line representing N

Output Format
All odd numbers from 1 to N, each number followed by a space, including the last number.

Example Input
Input 1:
5
Input 2:
10

Example Output
Output 1:
1 3 5 
Output 2:
1 3 5 7 9 
'''

# write code here
def main():
    # Read input
    N = int(input())

    # Print all odd numbers from 1 to N
    for i in range(1, N + 1, 2):
        print(i, end=' ')

if __name__ == "__main__":
    main()
'''q4
Take an input of a number A from the user. Print all perfect squares less than or equal to A.
Note - Perfect squares are integers whose square root is an integer. (For Example: 16 is perfect square as √16 = 4, or 42 = 16)

Problem Constraints
1 <= A <= 104

Input Format
A single line consisting of a integer A.

Output Format
Print perfect squares less than or equal to A in a single line in a space-separated manner.


Example Input
Input 1:
20
Input 2:
100
Example Output
Output 1:
1 4 9 16
Output 2:
1 4 9 16 25 36 49 64 81 100'''

# write code here
import math

def main():
    # Read input
    A = int(input())

    # Print all perfect squares less than or equal to A
    i = 1
    while i * i <= A:
        print(i * i, end=' ')
        i += 1

if __name__ == "__main__":
    main()

'''q5
Given an integer input N, print all multiples of 4 less than or equal to N.

Problem Constraints
1 <= N <= 10000

Input Format
Single line containing an integer N.

Output Format
Space separated integers representing multiples of 4 less than or equal to N.

Example Input
22

Example Output
4 8 12 16 20

Example Explanation
1 * 4 = 4
2 * 4 = 8
3 * 4 = 12
4 * 4 = 16
5 * 4 = 20
All are multiples of 4 less than 22

'''
n = int(input())

for i in range(1, n + 1):
    if i % 4 == 0:
        print(i, end=" ")

'''q6
Take an integer A as input. You have to print the sum of all odd numbers in the range [1, A].

Problem Constraints
1 <= A <= 1000

Input Format
First and only line contains a single positive integer A.

Output Format
Print the required sum in a single line.

Example Input
Input 1:

 1 
Input 2:
 4 

Example Output
Output 1:
 1 
Output 2:
 4 
 
Example Explanation
Explanation 1:
 For A = 1, 1 is the only odd number which lies in the range [1, 1].
Explanation 2:

 For A = 4, Odd numbers 1 and 3 lie in the range [1, 4]. 
 Sum = 1 + 3 = 4. 
'''


# write your code here
A = int(input())

total_sum = 0
for i in range(1, A + 1):
    if i % 2 != 0:  # Check if i is odd
        total_sum += i

print(total_sum)


'''q7
Take a number A as input, print its multiplication table having the first 10 multiples.

Problem Constraints
1 <= A <= 1000

Input Format
First line contains a single integer A.

Output Format
Print 10 lines, ith line containing ith multiple.

Example Input
Input 1:
 2 
Input 2:
 3 

Example Output
Output 1:
 2 * 1 = 2 
 2 * 2 = 4 
 2 * 3 = 6 
 2 * 4 = 8 
 2 * 5 = 10 
 2 * 6 = 12 
 2 * 7 = 14 
 2 * 8 = 16 
 2 * 9 = 18 
 2 * 10 = 20 
Output 2:

 3 * 1 = 3 
 3 * 2 = 6 
 3 * 3 = 9 
 3 * 4 = 12 
 3 * 5 = 15 
 3 * 6 = 18 
 3 * 7 = 21 
 3 * 8 = 24 
 3 * 9 = 27 
 3 * 10 = 30 

Example Explanation
Explanantion 1:

 For A = 2, First 10 multiples of 2 are 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 
Explanation 2:

 For A = 3, First 10 multiples of 3 are 3, 6, 9, 12, 15, 18, 21, 24, 27, 30 

'''


def main():
    A = int(input())

    for i in range(1, 11):
        print(f"{A} * {i} = {A * i}")


if __name__ == '__main__':
    main()

'''q8
You are given an integer A as input and you need to determine whether it is a palindrome or not.
A palindrome integer is one whose digits, when reversed, result in the same number.
For example, 121 is a palindrome because its reverse is also 121, but 123 is not a palindrome because its reverse is 321.

Note: The given integer will not have any leading zeros.

Problem Constraints
1 <= A <= 106

Input Format
First and the only line contains a single integer A.

Output Format
Print Yes if it is palindromic, else print No.

Example Input
Input 1:
 120 
Input 2:
 1001 
Input 3:
 131 

Example Output
Output 1:
 No 
Output 2:
 Yes 
Output 3:
 Yes 

Example Explanation
Explanation 1:
 For A = 120, reverse(A) = reverse(120) = 021 = 21 (removing leading zeroes). 120 is not equal to 21 
Explanation 2:

 For A = 1001, reverse(A) = reverse(1001) = 1001, which is same as A.
Explanation 3:

 For A = 131, reverse(A) = reverse(131) = 131, which is same as A. 

'''
def main():
    A = input().strip()  # Read input as a string

    # Reverse the string
    rev = A[::-1]

    # Compare original and reversed strings
    if A == rev:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()


'''q9
You are given two integers A and B. You have to find the value of AB.
NOTE: The value of AB will always be less than or equal to 109.

Problem Constraints
1 <= A, B <= 1000


Input Format
First line of the input contains a single integer A.
Second line of the input contains a single integer B.

Output Format
Print a single integer in single line.

Example Input
Input 1:
 2
 3 
Input 2:
 1
 10 
Example Output
Output 1:
 8 
Output 2:
 1 

Example Explanation
Explanation 1:

 For A = 2 and B = 3, the value of 23 = 2 * 2 * 2 = 8. 
Explanation 2:

 For A = 1 and B = 10, the value of 110 = 1.

'''


# write code here
def main():
    A = int(input())
    B = int(input())

    result = A ** B
    print(result)


if __name__ == '__main__':
    main()

'''a10
You have been provided with a bank account that has an initial balance of N amount. You are now required to perform two operations on this account, namely, ADD and SUBTRACT.

ADD operation: This operation increases the account balance by a certain amount and you are expected to print the updated balance after each ADD operation.
SUBTRACT operation: This operation decreases the account balance by a certain amount and you are again expected to print the updated balance after each SUBTRACT operation.
However, if the amount you are trying to subtract (i.e., debit) from the account balance is greater than the current balance, you should print "Insufficient Funds" (without quotes) instead of the updated balance. In this case, the operation should be skipped, and the account balance should remain unchanged.


Note :
Initial Amount N and Amount that is given are larger numbers.
Problem Constraints

1 <= N, X <= 1011
1 <= Number of operations <= 105

Input Format

The initial balance in the bank account is provided as a single integer N.
The number of operations to be performed on the bank account is provided as a single integer M.
Each of the next M lines contains two space-separated integers Type and Amount(X).
The value of Type can either be 1 or 2. If Type is 1, then the ADD operation needs to be performed, and if Type is 2, 
then the SUBTRACT operation needs to be performed.
The value of Amount(X) represents the amount of money to be added or subtracted from the account.

Output Format

Print Amount in the bank balance after each operation on a new line.

Example Input

1000
3
1 500
2 1400
2 500

Example Output

1500
100
Insufficient Funds

Example Explanation
Initially bank balance is 1000. 
First operation, ADD 500, bank balance becomes 1500, print it.
Second operation, SUBTRACT 1400, bank balance becomes 100, print it.
Third operation, SUBTRACT 500, print "Insufficient Funds".

'''

def main():
    N = int(input())  # Initial balance
    M = int(input())  # Number of operations

    balance = N

    for _ in range(M):
        Type, X = map(int, input().split())
        if Type == 1:
            # ADD operation
            balance += X
            print(balance)
        elif Type == 2:
            # SUBTRACT operation
            if X > balance:
                print("Insufficient Funds")
            else:
                balance -= X
                print(balance)

if __name__ == '__main__':
    main()


'''11
You are given a positive integer A. You have to print the sum of all even numbers in the range [1, A].

Problem Constraints
1 <= A <= 1000

Input Format
First and only line contains a single positive integer A.

Output Format
Print the required sum in a single line.

Example Input
Input 1:
 1 
Input 2:
 4 

Example Output
Output 1:
 0 
Output 2:
 6 

Example Explanation
Explanation 1:
 For A = 1, there are no even number which lies in the range [1, 1].
Explanation 2:

 For A = 4, Even numbers 2 and 4 lie in the range [1, 4]. 
 Sum = 2 + 4 = 6. 
'''

def main():
    A = int(input())
    total = 0

    for i in range(1, A + 1):
        if i % 2 == 0:
            total += i

    print(total)

if __name__ == '__main__':
    main()
