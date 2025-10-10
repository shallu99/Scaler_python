'''Q1. Column Sum
Problem Description
You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.

Problem Constraints
1 <= A.size() <= 103
1 <= A[i].size() <= 103
1 <= A[i][j] <= 103
Input Format
First argument is a 2D array of integers.(2D matrix).

Output Format
Return an array containing column-wise sums of original matrix.

Example Input
Input 1:
[1,2,3,4]
[5,6,7,8]
[9,2,3,4]

Example Output
Output 1:
{15,10,13,16}

Example Explanation
Explanation 1
Column 1 = 1+5+9 = 15
Column 2 = 2+6+2 = 10
Column 3 = 3+7+3 = 13
Column 4 = 4+8+4 = 16'''
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        result = []
        for j in range(len(A[0])):
            sum = 0
            for i in range(len(A)):
                sum += A[i][j]
            result.append(sum)
        return result


'''Q2. Row Sum
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
Row 3 = 9+2+3+4 = 18'''

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        for i in range(0,len(A)):
            temp = 0
            # Finding sum of elements of ith row
            for j in range(0,len(A[0])):
                temp += A[i][j]
            ans.append(temp)
        return ans

'''Q3. Row to Column Zero
Problem Description
You are given a 2D integer matrix A, make all the elements in a row or column zero if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.

Problem Constraint
1 <= A.size() <= 103
1 <= A[i].size() <= 103
0 <= A[i][j] <= 103

Input Format
First argument is a 2D integer matrix A.

Output Format
Return a 2D matrix after doing required operations.

Example Input
Input 1:
[1,2,3,4]
[5,6,7,0]
[9,2,0,4]

Example Output
Output 1:
[1,2,0,0]
[0,0,0,0]
[0,0,0,0]

Example Explanation
Explanation 1:
A[2][4] = A[3][3] = 0, so make 2nd row, 3rd row, 3rd column and 4th column zero.'''


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])

        zero_rows = set()
        zero_cols = set()

        # Step 1: Find positions of zeros
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Step 2: Update rows
        for r in zero_rows:
            for j in range(cols):
                A[r][j] = 0

        # Step 3: Update columns
        for c in zero_cols:
            for i in range(rows):
                A[i][c] = 0

        return A
'''Q4. Main Diagonal Sum
Problem Description
You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.
Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.

Problem Constraints
1 <= N <= 103
-1000 <= A[i][j] <= 1000

Input Format
There are 1 lines in the input. First 2 integers R, C are the number of rows and columns. Then R * C integers follow corresponding to the rowwise numbers in the 2D array A.

Output Format
Return an integer denoting the sum of main diagonal elements.

Example Input
Input 1:
3 3 1 -2 -3 -4 5 -6 -7 -8 9
Input 2:
2 2 3 2 2 3

Example Output
Output 1:
 15 
Output 2:
 6 

Example Explanation
Explanation 1:
The size of matrix is 3.
So, considering the indexing from 0.
Main diagonal elements will be A[0][0], A[1][1] and A[2][2]
A[1][1] + A[2][2] + A[3][3] = 1 + 5 + 9 = 15
Explanation 2:
The size of matrix is 2.
So, considering the indexing from 0.
Main diagonal elements will be A[0][0] and A[1][1].
A[1][1] + A[2][2] = 3 + 3 = 6'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        diag_sum = 0
        for i in range(n):
            diag_sum += A[i][i]
        return diag_sum
'''Q5
Minor Diagonal Sum
Problem Description
You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.
Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).

Problem Constraints
1 <= N <= 103
-1000 <= A[i][j] <= 1000

Input Format
First and only argument is a 2D integer matrix A.

Output Format
Return an integer denoting the sum of minor diagonal elements.

Example Input
Input 1:
 A = [[1, -2, -3],
      [-4, 5, -6],
      [-7, -8, 9]]
Input 2:
 A = [[3, 2],
      [2, 3]]

Example Output
Output 1:
 -5 
Output 2:
 4 

Example Explanation
Explanation 1:
 A[1][3] + A[2][2] + A[3][1] = (-3) + 5 + (-7) = -5
Explanation 2:
 A[1][2] + A[2][1] = 2 + 2 = 4'''
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        diag_sum = 0
        for i in range(n):
            diag_sum += A[i][n - 1 - i]   # pick from anti-diagonal
        return diag_sum

'''Q6.Matrix Scalar Product
Problem Description
You are given a matrix A and and an integer B, you have to perform scalar multiplication of matrix A with an integer B.

Problem Constraints
1 <= A.size() <= 1000
1 <= A[i].size() <= 1000
1 <= A[i][j] <= 1000
1 <= B <= 1000

Input Format
First argument is 2D array of integers A representing matrix.
Second argument is an integer B.

Output Format
You have to return a 2D array of integers after doing required operations.


Example Input
Input 1:
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = 2 
Input 2:
A = [[1]]
B = 5 
Example Output
Output 1:
[[2, 4, 6], 
[8, 10, 12], 
[14, 16, 18]]
Output 2:
[[5]]

Example Explanation
Explanation 1:
==> ( [[1, 2, 3],[4, 5, 6],[7, 8, 9]] ) * 2

==> [[2*1, 2*2, 2*3],
     [2*4, 2*5, 2*6],
     [2*7, 2*8, 2*9]]
     
==> [[2,   4,  6], 
     [8,  10, 12], 
     [14, 16, 18]]
Explanation 2:
==> ( [[1]] ) * 5
==> [[5*1]]
==> [[5]]'''
