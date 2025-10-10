'''Q1. Max Min of an Array
Problem Description
Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109

Input Format
First argument A is an integer array.

Output Format
Return the sum of maximum and minimum element of the array

Example Input
Input 1:
A = [-2, 1, -4, 5, 3]
Input 2:
A = [1, 3, 4, 1]

Example Output
Output 1:
1
Output 2:
5

Example Explanation
Explanation 1:
Maximum Element is 5 and Minimum element is -4. (5 + (-4)) = 1.
Explanation 2:
Maximum Element is 4 and Minimum element is 1. (4 + 1) = 5.'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # find minimum and maximum element in the array
        min_val = min(A)
        max_val = max(A)

        # return their sum
        return min_val + max_val

'''Q2.Array Rotation
Problem Description
Given an integer array A of size N and an integer B, you have to return the same array after rotating it B times towards the right.

Problem Constraints
1 <= N <= 105
1 <= A[i] <=109
1 <= B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return the array A after rotating it B times to the right

Example Input
Input 1:
A = [1, 2, 3, 4]
B = 2
Input 2:
A = [2, 5, 6]
B = 1

Example Output
Output 1:
[3, 4, 1, 2]
Output 2:
[6, 2, 5]


Example Explanation
Explanation 1:
Rotate towards the right 2 times - [1, 2, 3, 4] => [4, 1, 2, 3] => [3, 4, 1, 2]
Explanation 2:
Rotate towards the right 1 time - [2, 5, 6] => [6, 2, 5]
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        N = len(A)
        B = B % N

        if B == 0:
            return A

            # last B elements + first N-B elements
        return A[-B:] + A[:-B]

'''Q3.Reverse in a range
Problem Description
Given an array A of N integers and also given two integers B and C. Reverse the elements of the array A within the given inclusive range [B, C].

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109
0 <= B <= C <= N - 1

Input Format
The first argument A is an array of integer.
The second and third arguments are integers B and C

Output Format
Return the array A after reversing in the given range.

Example Input
Input 1:
A = [1, 2, 3, 4]
B = 2
C = 3
Input 2:
A = [2, 5, 6]
B = 0
C = 2


Example Output
Output 1:
[1, 2, 4, 3]
Output 2:
[6, 5, 2]


Example Explanation
Explanation 1:
We reverse the subarray [3, 4].
Explanation 2:
We reverse the entire array [2, 5, 6].
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        # reverse the part from B to C (inclusive)
        A[B:C+1] = A[B:C+1][::-1]
        return A

'''Q4.Time to equality
Problem Description
Given an integer array A of size N. In one second, you can increase the value of one element by 1.
Find the minimum time in seconds to make all elements of the array equal.

Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 1000

Input Format
First argument is an integer array A.
Output Format
Return an integer denoting the minimum time to make all elements equal.

Example Input
A = [2, 4, 1, 3, 2]

Example Output
8

Example Explanation
We can change the array A = [4, 4, 4, 4, 4]. The time required will be 8 seconds.'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_val = max(A)
        time = 0
        for num in A:
            time += (max_val - num)
        return time

'''Q5.Second Largest
Problem Description
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.

Problem Constraints
1 <= |A| <= 105
0 <= A[i] <= 109

Input Format
The first argument is an integer array A.

Output Format
Return the second largest element. If no such element exist then return -1.

Example Input
Input 1:
 A = [2, 1, 2] 
Input 2:
 A = [2]
Example Output
Output 1:
 1 
Output 2:
 -1 
Example Explanation
Explanation 1:
 First largest element = 2
 Second largest element = 1
Explanation 2:
 There is no second largest element in the array.'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Remove duplicates
        unique_vals = list(set(A))

        # If less than 2 unique values, no second largest exists
        if len(unique_vals) < 2:
            return -1

        # Sort and take second largest
        unique_vals.sort(reverse=True)
        return unique_vals[1]


'''Q6.Linear Search - Multiple Occurences
Problem Description
Given an array A and an integer B, find the number of occurrences of B in A.
Problem Constraints
1 <= B, Ai <= 109
1 <= length(A) <= 105

Input Format
Given an integer array A and an integer B.

Output Format
Return an integer, number of occurrences of B in A.

Example Input
Input 1:
 A = [1, 2, 2], B = 2 
Input 2:
 A = [1, 2, 1], B = 3 

Example Output
Output 1:
 2
Output 2:
 0
Example Explanation

Explanation 1:
Element at index 2, 3 is equal to 2 hence count is 2.
Explanation 2:
There is no element equal to 3 in the array.'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return A.count(B)

'''Q7.Count of elements
Problem Description
Given an array A of N integers. 
Count the number of elements that have at least 1 elements greater than itself.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109

Input Format
First and only argument is an array of integers A.

Output Format
Return the count of elements.
Example Input
Input 1:
A = [3, 1, 2]
Input 2:
A = [5, 5, 3]

Example Output
Output 1:
2
Output 2:
1

Example Explanation
Explanation 1:
The elements that have at least 1 element greater than itself are 1 and 2
Explanation 2:
The elements that have at least 1 element greater than itself is 3
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_val = max(A)
        max_count = A.count(max_val)
        return len(A) - max_count
