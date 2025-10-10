'''Q1. IsPrime
Problem Description
Given a number A. Return 1 if A is prime and return 0 if not.
Note :
The value of A can cross the range of Integer.

Problem Constraints
1 <= A <= 109

Input Format
The first argument is a single integer A.

Output Format
Return 1 if A is prime else return 0.

Example Input

Input 1:
A = 5
Input 2:

A = 10

Example Output

Output 1:
1
Output 2:

0

Example Explanation
Explanation 1:
5 is a prime number.
Explanation 2:

10 is not a prime number.
'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A<2:
            return 0

        for i in range(2, int(A**0.5 )+1):
            if A %i == 0:
                    return 0
        return 1


'''Q2. Count Factors - 2
Problem Description
Given an integer A, you need to find the count of it's factors.
Factor of a number is the number which divides it perfectly leaving no remainder.

Example : 1, 2, 3, 6 are factors of 6

Problem Constraints
1 <= A <= 109

Input Format
First and only argument is an integer A.


Output Format
Return the count of factors of A.

Example Input
Input 1:
5
Input 2:
10


Example Output
Output 1:
2
Output 2:
4

Example Explanation
Explanation 1:
Factors of 5 are 1 and 5.
Explanation 2:
Factors of 10 are 1, 2, 5 and 10.'''
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count = 0
        for i in range(1, int(A**0.5) + 1):
            if A % i == 0:
                if i == A // i:
                    count += 1
                else:
                    count += 2
        return count

'''Q3.Count of primes
Problem Description

You will be given an integer n. You need to return the count of prime numbers less than or equal to n.

Problem Constraints
0 <= n <= 10^3

Input Format
Single input parameter n in function

Output Format
Return the count of prime numbers less than or equal to n.

Example Input
Input 1:
19
Input 2:
1

Example Output
Output 1:
8
Output 2:
0

Example Explanation
Explanation 1:
Primes <= 19 are 2, 3, 5, 7, 11, 13, 17, 19
Explanation 2:
There are no primes <= 1
'''
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A < 2:
            return 0

        # Sieve of Eratosthenes
        is_prime = [True] * (A + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(A**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, A + 1, i):
                    is_prime[j] = False

        return sum(is_prime)

'''Q4. Find Perfect Numbers
Problem Description

You are given an integer A. You have to tell whether it is a perfect number or not.
Perfect number is a positive integer which is equal to the sum of its proper positive divisors.
A proper divisor of a natural number is the divisor that is strictly less than the number.

Problem Constraints
1 <= A <= 106

Input Format
First and only argument contains a single positive integer A.

Output Format
Return 1 if A is a perfect number and 0 otherwise.

Example Input
Input 1:
A = 4
Input 2:
A = 6

Example Output
Output 1:
0 
Output 2:
1 

Example Explanation
Explanation 1:
For A = 4, the sum of its proper divisors = 1 + 2 = 3, is not equal to 4.
Explanation 2:
For A = 6, the sum of its proper divisors = 1 + 2 + 3 = 6, is equal to 6. '''


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1:
            return 0  # 1 has no proper divisors other than itself

        div_sum = 1  # 1 is always a proper divisor

        # check divisors from 2 to sqrt(A)
        for i in range(2, int(A ** 0.5) + 1):
            if A % i == 0:
                div_sum += i
                if i != A // i:
                    div_sum += A // i

        return 1 if div_sum == A else 0
