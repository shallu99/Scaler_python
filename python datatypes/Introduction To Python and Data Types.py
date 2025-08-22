'''
question 1
Problem Description

Given two numbers A and B. Concatenate the two numbers and print it.


Problem Constraints

1 <= A, B <= 104


Input Format

There are two input lines
The first line has a single integer A.
The second line has a single integer B.


Output Format

Print in a single line the concatenated number.


Example Input

Input 1:-
4
5
Input 2:-
16
2


Example Output

Output 1:-
45
Output 2:-
162


Example Explanation

Explanation 1:-
Concatenation of 4 and 5 is 45.
Explanation 2:-
Concatenation of 16 and 2 is 162.

'''

n = int(input())
m = int(input())
# Print N and M one by one without any space
print(str(n)+""+str(m))


'''
question 2

Given the value of a single bill and the number of bills you received, print the total value of the bills.

Note: The value of all the bills are same


Problem Constraints

1 <= N <= 100
1 <= M <= 100


Input Format

The first line of the input is an integer N denoting the value of a single bill.
The second line of the input is an integer M denoting the number of bills.


Output Format

Print in a single line denoting the total value of bills.


Example Input

Input:-
12
10


Example Output

Output:-
120


Example Explanation

Note: The problem constraints mean that when we test your code, the test cases used in the backend can have input values only within those constraints. You need not implement them in your code. You need to make sure your code will work for all such input values!

'''

a = int(input())
b =int(input())
print(a*b)


'''question 3
Problem Description

Given total bills amount and amount of a single bill. Print number of bills.

Note : The total amount is equally splitted in all bills. The number of bills should be an integer value.

Input Format

The first line contains a real number N denoting the total budget.
The second line contains an integer M denoting the value of a single bill.
Output Format

Print in a single line denoting the total number of bills that can fit in the total budget.
Problem Constraints

1 <= N <= 10000
1 <= M <= 100
Example Input

Input:-
126.3
5
Example Output

Output:-
25
Note: The problem constraints mean that when we test your code, the test cases used in the backend can have input values only within those constraints. You need not implement them in your code. You need to make sure your code will work for all such input values!

'''
N = float(input())
M = float(input())
c = (int(N) / int(M))
print(int(c))

'''question 4
Your friend Rahul plans to visit exotic countries all around the world. Sadly,
 Rahul's math skills aren't good enough. Take the amount of money Rahul has before the currency exchange and the amount of money that is spent from his savings as input, print the amount of money that remains in his savings.

Input Format

The first line contains an integer N denoting the total savings, the amount of money before exchange.
The second line contains an integer M denoting the exchanging amount, denoting the amount of money that is spent 
from the savings.
Output Format

Print a single line denoting the amount of money that is left in his savings.
Problem Constraints

1 <= N <= 1000
1 <= M <= N
Example Input

Input:-
116
12
Example Output

Output:-
104
Note: The problem constraints mean that when we test your code, the test cases used in the backend 
can have input values only within those constraints. You need not implement them in your code. 
You must ensure your code will work for all such input values!'''

N = int(input())
M = int(input())
print(N -M)
