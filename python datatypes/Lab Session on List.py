'''Q1. Row Sum
Problem Description
You are given a 2D matrix A of integers.
Your task is to compute the sum of elements in each row and return a 1D array where each element represents the sum of a corresponding row in the matrix.

Problem Constraints
1 <= A.size() <= 103
1 <= A[i].size() <= 103
1 <= A[i][j] <= 103

Input Format
First argument A is a 2D array of integers.(2D matrix).

Output Format
Return an array containing row-wise sums of original matrix.

Example Input
Input 1:
[1,2,3,4]
[5,6,7,8]
[9,2,3,4]

Example Output
Output 1:
[10,26,18]

Example Explanation
Explanation 1
Row 1 = 1+2+3+4 = 10
Row 2 = 5+6+7+8 = 26
Row 3 = 9+2+3+4 = 18

Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: Multi Dimensional Array with Integers, For e.g [[2,3,6,7],[2,3,4,5]]
Enter Input Here
'''
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        # Handle empty matrix (not strictly needed given constraints but useful for robustness)
        if not A:
            return []
        # Use Python's built-in sum() for each row
        return [sum(row) for row in A]


'''Q2. Matrix Transpose
Problem Description

Given a 2D integer array A, return the transpose of A.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Problem Constraints
1 <= A.size() <= 1000
1 <= A[i].size() <= 1000
1 <= A[i][j] <= 1000


Input Format
First argument is a 2D matrix of integers.

Output Format
You have to return the Transpose of this 2D matrix.

Example Input
Input 1:

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
Input 2:
A = [[1, 2],[1, 2],[1, 2]]


Example Output
Output 1:
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
Output 2:
[[1, 1, 1], [2, 2, 2]]

Example Explanation

Explanation 1:

Clearly after converting rows to column and columns to rows of [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
 we will get [[1, 4, 7], [2, 5, 8], [3, 6, 9]].
Explanation 2:

After transposing the matrix, A becomes [[1, 1, 1], [2, 2, 2]]


Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: Multi Dimensional Array with Integers, For e.g [[2,3,6,7],[2,3,4,5]]
Enter Input Here
'''
#!/usr/bin/env python3
import sys
import threading
from typing import List, Any

class Solution:
    def solve(self, A: List[List[int]]) -> List[List[int]]:
        """
        Returns the transpose of A (i.e. swaps rows and columns).
        E.g. A shape (n × m) becomes result shape (m × n).
        """
        if not A or not A[0]:
            return []
        # zip(*A) groups the i-th elements from each row into columns
        # map(list, ...) converts each tuple into a list
        return [list(col) for col in zip(*A)]

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(map(int, data))
    # First two numbers are dimensions n rows, m cols (if provided)
    # If the judge doesn't give them, you'll just parse row-by-row
    first = next(it)
    second = next(it)

    # Heuristic: if the "first" is list length, use those dims
    # Otherwise treat both as data.
    # Replace this with your problem's exact input spec.

    try:
        n, m = int(first), int(second)
    except ValueError:
        # Fallback: assume matrix follows row-by-row after those two numbers
        # (Common in many hackathons)
        arr = [first, second] + list(it)
        # Suppose original shape is k by k (square)
        k = int(len(arr) ** 0.5)
        n = m = k
        nums = arr
    else:
        nums = list(it)

    # Build A as a list of lists
    A = []
    idx = 0
    for _ in range(n):
        row = nums[idx:idx + m]
        idx += m
        A.append(row)

    sol = Solution()
    T = sol.solve(A)

    # Print each row like the judge's expected format:
    # e.g. [1 2 3 ] with a trailing space before the closing bracket
    for row in T:
        print('[', ' '.join(str(x) for x in row), ' ]')

if __name__ == "__main__":
    # Some platforms require this wrapping to avoid stack limits
    threading.Thread(target=main).start()


'''Q3. Print matrix row by row
Problem Description

Given a matrix of N rows and M columns, print it row by row. Firstly print 0th row, then 1st row, 2nd row and so on.


Problem Constraints

1 <= N <= 100
1 <= M <= 100
1 <= mat[i][j] <= 10000


Input Format
Two values denoting N and M,
Next N lines contain M space separated integers representing the matrix Mat

Output Format
N lines denoting each row.
Note: Ensure there is a space character (' ') at the end of the line.

Example Input
3 4
10 20 30 40
50 60 70 80
90 100 110 120

Example Output
10 20 30 40
50 60 70 80
90 100 110 120

Example Explanation
0th row -> 10 20 30 40
1st row -> 50 60 70 80
2nd row -> 90 100 110 120
'''
def main():
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return 0

    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # Read matrix row by row
    mat = []
    for _ in range(n):
        mat.append([int(next(it)) for _ in range(m)])

    # Output each row with a space after the last element, then a newline
    out = sys.stdout.write
    for row in mat:
        for x in row:
            out(str(x) + " ")  # prints each element followed by a space
        out("\n")

    return 0

if __name__ == "__main__":
    main()

'''Q4. Print matrix column by column
Problem Description

Given a matrix of N rows and M columns, print it column by column. Firstly print 0th column, then 1st column, 2nd column and so on.

Note: Make sure to receive the matrix input row by row.


Problem Constraints

1 <= N <= 100
1 <= M <= 100
1 <= mat[i][j] <= 10000

Input Format
Two values denoting N and M,
Next N lines contain M space separated integers representing the matrix Mat

Output Format
M lines denoting each column
Note: Ensure there is a space character (' ') at the end of the line.


Example Input
3 4
10 20 30 40
50 60 70 80
90 100 110 120

Example Output
10 50 90
20 60 100
30 70 110
40 80 120

Example Explanation

0th column -> 10 50 90
1st column -> 20 60 100
2nd column -> 30 70 80
3rd column -> 40 80 120

'''
#!/usr/bin/env python3
def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return 0

    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # Parse the matrix row‑by‑row
    mat = [[int(next(it)) for _ in range(m)] for _ in range(n)]

    out = sys.stdout.write
    # Iterate columns (0th → 1st → ... → (m‑1)th)
    for col in range(m):
        # Iterate all rows for the current column
        for row in range(n):
            out(str(mat[row][col]) + " ")
        out("\n")
    return 0

if __name__ == "__main__":
    main()


'''Q5. Wave Print (Row Wise)
Problem Description

Given an N x N matrix, print the elements of the matrix in a wave form row-wise. For the first row, traverse from left to right, for the second row, traverse from right to left, and continue this alternating pattern for the remaining rows.

Problem Constraints
1 <= N <= 103
0 <= Mat[i][j] <= 109

Input Format
First line is an integer N
Next N lines contain N space separated integers representing the matrix Mat


Output Format
A single line containing N*N integers of matrix Mat in wave form (row wise)
Note: Ensure there is a space character (' ') at the end of the line.

Example Input
Input 1:

3
4 1 2
7 4 4 
3 7 4
Input 2:

2
1 2
3 4

Example Output
Output 1:
4 1 2 4 4 7 3 7 4
Output 2:
1 2 4 3

Example Explanation
For Input 1:
We will first iterate the 1st row from left to right and print the elements, 
then we will iterate the 2nd row from right to left and print the elements,
then we will iterate the 3rd row from left to right and print the elements.
This looks like a wave.
For Input 2:
We will first iterate the 1st row from left to right and print the elements, 
then we will iterate the 2nd row from right to left and print the elements.
This looks like a wave.
'''


def main():
    # DO NOT CHANGE THE CODE BELOW.
    global ii
    n = inp[ii: ii + 1][0]
    ii += 1
    mat = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = inp[ii: ii + 1][0]
            ii += 1
    # DO NOT CHANGE THE CODE ABOVE

    # YOUR CODE GOES BELOW HERE.
    # USE THE GIVEN MATRIX mat FOR ALL THE OPERATIONS.

    # Ensure a newline after finishing (judge tolerance)
    import sys
    out = sys.stdout.write

    # Traverse each row in wave form
    for i in range(n):
        if i % 2 == 0:
            # Even row → left to right
            for j in range(n):
                out(str(mat[i][j]) + " ")
        else:
            # Odd row → right to left
            for j in range(n - 1, -1, -1):
                out(str(mat[i][j]) + " ")

    # Optionally, print a newline (most judges ignore trailing newline)
    out("\n")

    return 0


if __name__ == '__main__':
    main()


'''Q1. Are Matrices Same ?
Problem Description

You are given two matrices A and B of equal dimensions and you have to check whether two matrices are equal or not.

NOTE: Both matrices are equal if A[i][j] == B[i][j] for all i and j.


Problem Constraints

1 <= A.size(), B.size() <= 1000
1 <= A[i].size(), B[i].size() <= 1000
1 <= A[i][j], B[i][j] <= 1000
A.size() == B.size()
A[i].size() == B[i].size()


Input Format

First argument is 2-D array of integers representing matrix A.

Second argument is 2-D array of integers representing matrix B.
'''
class Solution:
    def solve(self, A, B):
        # Matrices must have the same number of rows
        if len(A) != len(B):
            return 0

        n = len(A)
        # Early exit if there are no rows
        if n == 0:
            return 1

        m = len(A[0])
        for i in range(n):
            # Check each row length for complete rectangular structure
            if len(A[i]) != len(B[i]):
                return 0
            for j in range(m):
                if A[i][j] != B[i][j]:
                    return 0

        return 1

'''Q2. Add the matrices

Problem Description

You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.
Note: Matrices are of same size means the number of rows and number of columns of both matrices are equal.

The Following will give you an idea of matrix addition:



Problem Constraints

1 <= A.size(), B.size() <= 1000 1 <= A[i].size(), B[i].size() <= 1000 1 <= A[i][j], B[i][j] <= 1000
Input Format

The first argument is the 2D integer array A The second argument is the 2D integer array B
Output Format

You have to return a vector of vector of integers after doing required operations.
Example Input

Input 1:
A = [[1, 2, 3],   
     [4, 5, 6],   
     [7, 8, 9]]  

B = [[9, 8, 7],   
     [6, 5, 4],   
     [3, 2, 1]]
 
Input 2:
A = [[1, 2, 3],   
     [4, 1, 2],   
     [7, 8, 9]]  

B = [[9, 9, 7],   
     [1, 2, 4],   
     [4, 6, 3]]
 
Example Output

Output 1:
[[10, 10, 10],   
 [10, 10, 10],   
 [10, 10, 10]]
Output 2:
[[10, 11, 10],   
 [5,   3,  6],   
 [11, 14, 12]]
Example Explanation

Explanation 1:
A + B = [[1+9, 2+8, 3+7],  
         [4+6, 5+5, 6+4],  
         [7+3, 8+2, 9+1]]   
      = [[10, 10, 10],   
         [10, 10, 10],   
         [10, 10, 10]].
Explanation 2:
A + B = [[1+9, 2+9, 3+7],  
         [4+1, 1+2, 2+4],  
         [7+4, 8+6, 9+3]]   
      = [[10, 11, 10],   
         [5,   3,  6],   
         [11, 14, 12]].
Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: Multi Dimensional Array with Integers, For e.g [[2,3,6,7],[2,3,4,5]]
Enter Input Here
Arg 2: Multi Dimensional Array with Integers, For e.g [[2,3,6,7],[2,3,4,5]]
'''


class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        # Quick dimension sanity check (optional, per problem they match)
        if len(A) != len(B) or any(len(A[i]) != len(B[i]) for i in range(len(A))):
            raise ValueError("Matrices are not the same size")

        # Using nested loops for clarity and minimal overhead
        n = len(A)
        if n == 0:
            return []
        m = len(A[0])
        C = [[0] * m for _ in range(n)]

        for i in range(n):
            Ai, Bi, Ci = A[i], B[i], C[i]
            # Summing each element at position j
            for j in range(m):
                Ci[j] = Ai[j] + Bi[j]

        return C

'''Q3. Largest in each Row of 2D Array
Problem Description
Given a 2D array A of N rows and M columns. Find value of largest element in each row.

Problem Constraints

1 <= N, M <= 1000
1 <= Ai <= 109

Input Format
The first argument A is a 2D array of integers

Output Format

Return an array of length N, in which every index i contains the maximun value of the ith row in the 2D matrix.

Example Input
Input 1:
A = [[1, 2], [1, 3]]
Input 2:
A = [[1, 2, 3]]

Example Output
Output 1:
 [2, 3]
Output 2:
 [3]

Example Explanation
Explanation 1:
In the first row 2 is maximum value.
In the second row 3 is maximum value.
Explanation 2:
In the first and only row 3 is maximum value.

Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: Multi Dimensional Array with Integers, For e.g [[2,3,6,7],[2,3,4,5]]
Enter Input Here
'''
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        # If A is empty, return an empty list
        if not A:
            return []

        # Compute the max of each row using Python’s built-in max() — very efficient in C
        return [max(row) for row in A]


'''Q4. Sum of Columns of 2D Array
Problem Description
Given a 2D integer array C[][] of A rows and B columns. Return an integer array of size B that represents the sums of the columns of the 2D array C.

Problem Constraints
1 <= A,B <= 103
1 <= C[i][j] <= 103

Input Format
The first argument is a single integer A.
The second argument is a single integer B.
The third argument is a 2D integer array C.


Output Format
Return an integer array of size B that represents the sums of the columns of the 2D array C.

Example Input
Input 1:
A = 3
B = 2
C = [[4, 1], [1, 3], [6, 2]]
Input 2:
A = 2
B = 2
C = [[1, 1], [4, 1]]


Example Output
Output 1:
[11, 6]
Output 2:
[5, 2]

Example Explanation
Explanation 1:
 Column 1 : 4 + 1 + 6 = 11
Column 2 : 1 + 3 + 2 = 6
Explanation 2:

Column 1 : 4 + 1 = 5
Column 2 : 1 + 1 = 2


Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: A single Integer, For e.g 9
Enter Input Here
Arg 2: A single Integer, For e.g 9
Enter Input Here
Arg 3: Multi Dimensional Array with Integers, For e.g [[2,3,6,7],[2,3,4,5]]
Enter Input Here
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        # Sanity check on dimensions (usually guaranteed by constraints)
        if len(C) != A or any(len(row) != B for row in C):
            raise ValueError(f"Invalid matrix size: expected {A}×{B}, got {len(C)}×{len(C[0])}")

        # Initialize column sums to zeros
        col_sums = [0] * B

        # Accumulate sum for each column
        for i in range(A):
            row = C[i]
            for j in range(B):
                col_sums[j] += row[j]

        return col_sums


'''Q6. Wave Print (Column Wise)
Problem Description


Write a program to input an integer N and a N*N matrix Mat from user and print the matrix in wave form (column wise)

See example for clarifications regarding wave print.

Note: Ensure there is a space character (' ') at the end of the line.

Problem Constraints
1 <= N <= 103
0 <= Mat[i][j] <= 109

Input Format

First line is an integer N
Next N lines contain N space separated integers representing the matrix Mat

Output Format
A single line containing N*N integers of matrix Mat in wave form (column wise)

Example Input
Input 1:
3
4 1 2 
7 4 4 
3 7 4 
Input 2:
2
1 2
3 4

Example Output
Output 1:
4 7 3 7 4 1 2 4 4 
Output 2:
1 3 4 2

Example Explanation
For Input 1:
We will first iterate the 1st column from top to bottom and print the elements, 
then we will iterate the 2nd column from botton to top and print the elements,
then we will iterate the 3rd column from top to bottom and print the elements.
For Input 2:
We will first iterate the 1st column from top to bottom and print the elements, 
then we will iterate the 2nd column from bottom to top and print the elements.

'''

def main():
    # Input the size of the matrix
    N = int(input())

    # Initialize the matrix
    mat = []

    # Input the matrix elements
    for i in range(N):
        row = list(map(int, input().split()))
        mat.append(row)

    # Traverse the matrix in wave form column-wise
    for j in range(N):
        if j % 2 == 0:
            # Traverse the column from top to bottom
            for i in range(N):
                print(mat[i][j], end=" ")
        else:
            # Traverse the column from bottom to top
            for i in range(N-1, -1, -1):
                print(mat[i][j], end=" ")

    # Print a newline at the end
    print()

if __name__ == '__main__':
    main()
