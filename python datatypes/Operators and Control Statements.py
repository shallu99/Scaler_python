'''Q1
Write a program to input an integer from user and print 1 if it is odd otherwise print 0.

Problem Constraints

1 <= N <= 1000000



Input Format

One line containing an integer N.



Output Format

Print either 1 or 0 as per the question.



Example Input

Input 1:

5
Input 2:

1000


Example Output

Output 1:

1
Output 2:

0


Example Explanation

Explanation 1:

Clearly, 5 is odd.
Explanation 2:

Clearly, 1000 is even.

'''
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a = int(input())
    x = a/2
    if x%2 ==0:
        print(0)
    if x%2!=0:
        print(1)
    return 0

if __name__ == '__main__':
    main()

'''q2
Write a program to input two numbers(A & B) from user and print the maximum element among A & B.




Problem Constraints


1 <= A <= 1000000

1 <= B <= 1000000




Input Format


First line is a single integer A.
Second line is a single integer B.




Output Format


One line containing the greater integer A or B.




Example Input


Input 1:


5 
6
Input 2:


1000 
10000



Example Output


Output 1:


6
Output 2:


10000



Example Explanation


Explanation 1:


Clearly, among 5 and 6, 6 is maximum.
Explanation 2:


Clearly, among 1000 and 10000, 10000 is maximum.



'''

a = int(input())
b = int(input())
if a>b:
    print(a)
else:
    print(b)
'''q4
Print the result of the following expression:

(3 + 4) // 2 + 6'''
# YOUR CODE GOES HERE
print(9)

'''q5
Set the value of variable a, b and c such that the following condition evaluates to true:

a = -1 # change this
b = -1 # change this
c = -1 # change this

# DO NOT CHANGE THIS
x = a < b + c

print(x) # this should be True
Note: You need to write the code from scratch in the code editor.'''
a =40 # __ change this
b = 45# __ change this
c = 20# __ change this

# DO NOT CHANGE THIS
x = a < b + c

print(x) # this should be True

'''q6
Problem Description

Write a program to input a number(A) from user and print

1 if it is positive,
-1 if it is negative,
0 if it's neither positive nor negative.

Problem Constraints

1 <= A <= 1000000



Input Format
One line containing an integer A.



Output Format
One line each 0/1/-1 as per the question.



Example Input
Input 1:

50
Input 2:

-101
Input 3:

0


Example Output
Output 1:

1
Output 2:

-1
Output 3:

0


Example Explanation
Explanation 1:

Clearly, 50 is positive.
Explanation 2:

Clearly, -101 is negative.
Explanation 3:

Clearly, 0 is neither positive nor negative.

'''

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a = int(input())
    if a >0:
        print(1)
    elif a<0:
        print(-1)
    elif a ==0:
        print(0)
    return 0

if __name__ == '__main__':
    main()


'''q7
You are given 3 integer angles(in degrees) A, B and C of a triangle. You have to tell whether the triangle is valid or not.


A triangle is valid if sum of its angles equals to 180.

NOTE: You have to take the input of 3 sides of triangle from the user.


Problem Constraints

1 <= A, B, C <= 180



Input Format

First line of the input contains an integer A.


Second line of the input contains an integer B.

Third line of the input contains an integer C.




Output Format

Print 1 if the triangle having given sides is valid, else print 0.



Example Input

Input 1:



 60
 60
 60
Input 2:

 30
 40
 50




Example Output

Output 1:



 1 
Output 2:

 0 




Example Explanation

Explanation 1:



 Sum of angles = A + B + C = 60 + 60 + 60 = 180
 Hence, the given triangle is valid.
Explanation 2:

 Sum of angles = A + B + C = 30 + 40 + 50 = 120
 As sum of angles is not equal to 180, the given triangle is not valid.



'''
a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    print(1)
else:
    print(0)

'''q8
Problem Description

Write a program to input two numbers(A & B) from user and print the minimum element among A & B in each line.


Problem Constraints

1 <= A <= 1000000

1 <= B <= 1000000



Input Format


First line is a single integer A.
Second line is a single integer B.




Output Format

One line containing an integer as per the question.



Example Input


Input 1:


5 
6
Input 2:


1000 
10000



Example Output

Output 1:

5
Output 2:

1000


Example Explanation

Explanation 1:

Clearly, among 5 and 6, 5 is minimum.
Explanation 2:

Clearly, among 1000 and 10000, 1000 is minimum.

'''
# YOUR CODE GOES HERE
# YOUR CODE GOES HERE
a = int(input())
b = int(input())
if a<b :
    print(a)

else:
     print(b)


'''q9
You are given the Cost Price C and Selling Price S of a Product. You have to tell whether there is a Profit or Loss. Also, calculate total profit or loss.

NOTE: It is guaranteed that Cost Price and Selling Price are not equal.

NOTE: You have to take input of the Cost Price(C) and Selling Price(S) from the user.



Problem Constraints

1 <= C, S <= 109

C ≠ S





Input Format

First line of the input contains a single integer C.



Second line of the input contains a single integer S.





Output Format

Print two integers in separate lines.



First integer denotes whether there is a profit or loss. If there is a profit, print 1, else print -1.

Second integer is a non-negative integer denoting the absolute value of total profit or loss.





Example Input

Input 1:



 2
 4
Input 2:

 4
 1




Example Output

Output 1:



 1
 2
Output 2:

 -1
 3




Example Explanation

Explanation 1:



 Cost Price = 2
 Selling Price = 4
 As Cost Price < Selling Price, there is a profit.
 Total Profit = Selling Price - Cost Price = 4 - 2 = 2
Explanation 2:

 Cost Price = 4
 Selling Price = 1
 As Cost Price > Selling Price, there is a loss.
 Total Loss = Cost Price - Selling Price = 4 - 1 = 3 



'''
C = int(input())
S = int(input())

if S > C:
    print(1)
    print(S - C)
else:
    print(-1)
    print(C - S)


'''q10
Write a program to input from user an integer(n) representing the rating of a person on a platform.

You have to print the category of that person.

If the rating is greater than or equal to 2100 then that person is "grand master".
If the rating is greater than or equal to 1900 then that person is "candidate master".
If the rating is greater than or equal to 1600 then that person is "expert".
If the rating is greater than or equal to 1400 then that person is "pupil".
If the rating is smaller than 1400 then that person is "newbie".
NOTE: Print all the chars of the category of the person in lowercase if rating is odd otherwise print in UPPERCASE


Problem Constraints

1000 <= n <= 2500



Input Format

One line containing an integern.



Output Format

A string representing the category of the person.



Example Input

Input 1:

1659
Input 2:

2100


Example Output

Output 1:

expert
Output 2:

GRAND MASTER


Example Explanation

Explanation 1:

Clearly, 1659 is odd and is in the range of expert.
Explanation 2:

Clearly, 2100 is even and is in the range of grand master.

'''
# Input from the user
n = int(input())

# Determine category based on rating
if n >= 2100:
    category = "grand master"
elif n >= 1900:
    category = "candidate master"
elif n >= 1600:
    category = "expert"
elif n >= 1400:
    category = "pupil"
else:
    category = "newbie"

# Check if the rating is odd or even and print accordingly
if n % 2 == 0:
    print(category.upper())
else:
    print(category.lower())


'''q11
Write a program to input three numbers(A, B & C) from user and print the maximum element among A, B & C in each line.

Problem Constraints


1 <= A <= 1000000

1 <= B <= 1000000

1 <= C <= 1000000



Input Format


First line is a single integer A.
Second line is a single integer B.
Third line is a single integer C.




Output Format

One line containing an integer as per the question.



Example Input


Input 1:


5 
6 
7
Input 2:


1000 
10000 
100000



Example Output

Output 1:

7
Output 2:

100000


Example Explanation

Explanation 1:

Clearly, among 5, 6 and 7, 7 is maximum.
Explanation 2:

Clearly, among 1000, 10000 and 100000, 100000 is maximum.

'''
def main():
    # Input three numbers from the user
    A = int(input())
    B = int(input())
    C = int(input())

    # Find the maximum number
    maximum = max(A, B, C)

    # Print the maximum number
    print(maximum)

    return 0

if __name__ == '__main__':
    main()
