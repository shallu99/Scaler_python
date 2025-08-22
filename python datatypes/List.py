'''Q1. Sum the Array
Problem Description

Write a program to print sum of elements of the input array A of size N.

Note: User is supposed to write a program from scratch to add the elements of the input array and print the result.

Problem Constraints

1 <= N <= 1000
1 <= A <= 1000

Input Format
- The first integer N denotes the number of integers in the array.
- The next N integers denotes the element of the array A.

Output Format
A single integer containing sum of elements from the input array.

Example Input
Input 1:
5 1 2 3 4 5
Input 2:
4 10 50 40 80

Example Output
Output 1:
15
Output 2:
180

Example Explanation
Input-1:
N = 5 , A = [1, 2, 3, 4, 5]
here the first integer is the size of A and the remaining elements are [1, 2, 3, 4, 5]
which all sum to 15
Input-2:
N = 4 , A = [10, 50, 40, 80]
here the first integer is the size of A and the remaining elements are [10, 50, 40, 80]
which all sum to 180

'''
def calculate_sum(input_list):
    """
    Takes a list of numbers (integers or floats) and returns their sum.
    """
    total = 0
    for x in input_list:
        total += x
    return total



def calculate_sum(input_list):
    return sum(input_list)



'''Q2. Second Largest
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
 There is no second largest element in the array.


Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: An Integer Array, For e.g [1,2,3]
Enter Input Here

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) < 2:
            return -1

        first = second = float('-inf')
        for num in A:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num

        return second if second != float('-inf') else -1


'''Q3. Remove that
Problem Description

Write a program to input N numbers array, A from the user and an integer X and print the array by deleting element at specified position X.

Note: The first element is located at position 1, the second element is located at position 2, and so on.

Problem Constraints
2 <= N <= 100
1 <= A[i] <= 1000
1 <= X <= N

Input Format
First line is N which means number of elements.
Second line contains N space separated integers.
Third line is X position which has to be deleted.

Output Format
N-1 space separated integers of the input array after deleting the element at required position.

Example Input

Input 1:
5
2 3 1 4 2
3
Input 2:
2
4 5
2

Example Output
Output 1:
2 3 4 2
Output 2:
4

Example Explanation

Explanation 1:
Clearly after removing the element at position 3 (2 3 1 4 2), the remaining array is 2 3 4 2.
Explanation 2:
After removing the element at position 2 (4 5), the remaining array is 4.

'''
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    a = list(map(int,input().split()))
    x = int(input())
    # looping from x to n-1 and making current element equal to the next one
    for i in range(x,n):
        a[i-1]=a[i]
    n -= 1;
    for i in range(0,n):
        print(a[i],end=' ')
    return 0

if __name__ == '__main__':
    main()



'''Q4. Print in Reverse
Problem Description

Write a program to print the input array A of size N in reverse order where you have to take integer N and further N elements as input from user.
Problem Constraints

1 <= N <= 1000  
1 <= A <= 1000
Input Format

A single line representing **N** followed by N integers of the array **A**
Output Format

A single line containing N space separated integers representing elements of the input array in reverse order.  
**Note** - Keep a space character (' ') at the end of the line.
Example Input

Input 1:
5 1 2 3 4 5
Input 2:
4 10 50 40 80

Example Output
Output 1:
5 4 3 2 1 
Output 2:
80 40 50 10 
Note:

This question requires you to read multiple numbers from input. The first number represents N, which indicates how many more numbers follow. The remaining numbers are converted to integers using the map() function.
Since this concept will be covered later in the module, 
we encourage you to do some independent research and write your code accordingly.
You may also refer to the following article for further guidance: link'''


# Your Code Goes Here
def main():
    data = list(map(int, input().strip().split()))
    if not data:
        return
    N = data[0]
    arr = data[1:1 + N]
    # reverse the list
    rev = arr[::-1]
    # print with trailing space
    print(' '.join(str(x) for x in rev), end=' ')


if __name__ == "__main__":
    main()


'''Q9. Shopping list items
Problem Description:

Write a program that will keep track of items for a shopping list. 
The program should keep asking for new items as input until “end” is entered, print the full shopping list at the end.

Input Format:

Input is taken from the user for different elements until end is input.
Output Format:

The list of all elements of the shopping list
Sample Input:

Fruits
Notebooks
Perfume
Shoes
end
Sample Output:

['Fruits', 'Notebooks', 'Perfume', 'Shoes']
Sample explanation:

Fruits, Notebooks, Perfume, and Shoes strings
are only added to the shopping list because after Shoes end is input therefore it shouldn't be included in the output list.'''


def shopping_list(items):
    ''' input: take items as inputs (strings) from the user
        output: print the shopping list '''

    shoplist = []
    for item in items:
        if item.lower() == 'end':
            break
        shoplist.append(item)

    print(shoplist)


# Sample usage
shopping_list(['Perfume', 'Stickers', 'Eggs', 'Bread', 'Vegetables', 'Watermelon', 'Soaps', 'Notebook', 'end'])


'''Q2. First Multiple
Problem Description

Write a program for a given integer x and a list ls to return the first multiple of x that occurs in the list,
and if there isn’t any multiple of x in the list then return -1.

Note: The list with elements and the integer x is already passed as an argument to the function. User don't need to take any input. Just perform the task on the passed arguments and return the required result.

Problem Constraints

1 <= len(ls) <= 103
1 <= ls[i] <= 105
1 <= x <= 105


Input Format
First line of input is number of test cases t.
The remaining lines contain the test cases.
For each test case-
First line of input is the integer x.
Second line of input contains the elements of ls, separated by spaces.


Output Format
Return the first multiple of x from the list in integer format, else return -1.

Example Input

Input 1:
ls = [2, 1, 2, 4, 3, 5]
x  = 4
Input 2:
ls = [7, 5, 3, 17]
x  = 2


Example Output
Output 1:
4
Output 2:
-1

Example Explanation
Explanation 1:
In the list, the first element that is a multiple of 4 is 4.
Explanation 2:
There is no multiple of 2, So return -1

'''
def first_multiple(ls, x):
    '''Returns the first multiple of x in ls, or -1 if none exists.'''
    for num in ls:
        if num % x == 0:
            return num
    return -1

'''Q3. Consecutive Duplicate
Problem Description

Write a function to check if the given array A has consecutive duplicate elements or not.
Return True if there are consecutive duplicate elements in the list else return False.
Here by consecutive duplicates, we mean duplicates that are present at consecutive indices in the array

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109

Input Format
An integer array A as the function argument.

Output Format
Return True or False

Example Input
Input 1:
1
4
1 2 3 3
Input 2:
1
2
1 2

Example Output
Output 1:
True
Output 2:
False

Example Explanation

Explanation 1:
As there are 3 3 in the list i.e. at indices 2 and 3, there True is returned.
Explanation 2:
There are no consecutive duplicate elements in the list.

'''


def duplicate(ls, n):
    ''' input: ls - List of elements and n - length of list
        output: Return True if there are consecutive duplicates, else False'''

    for i in range(n - 1):
        if ls[i] == ls[i + 1]:
            return True
    return False

'''Q6. Difference of even and odd
Problem Description

Write a program to find the difference between the sum of all even elements and the sum of all odd elements from the given array, A.
Note: The array of elements will be passed as an argument to the function. You don't need to take any input of array.

Problem Constraints

1 <= len(A) <= 105
1 <= A[i] <= 105

Input Format
The only argument is the array of integers, A.

Output Format
The difference of the even and odd elements sum in integer format.

Example Input
Input 1:
1
56 63 87 24 32 13 15 19 44 52
Input 2:
1
2 8 4 6

Example Output
Output 1:
11
Output 2:
20

Example Explanation

Explanation 1:
The sum of even elements is: 56 + 24 + 32 + 44 + 52 = 208. 
The sum of odd elements is: 63 + 87 + 13 + 15 + 19 = 197. 
Difference between even elements and odd elements sum is 208 - 197 = 11.
Explanation 2:
The sum of even elements is: 2 + 8 + 4 + 6 = 20. 
There is no odd elements. 
Difference between even elements and odd elements sum is 20 - 0 = 20.

'''


def even_odd(A):
    sum_even = 0
    sum_odd = 0

    for num in A:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    diff = sum_even - sum_odd
    return diff

'''Q7. Divisible by 5 and 7
Problem Description

Write a program that returns the list of elements that are present in the given list and are divisible by 5 and 7.


Problem Constraints

1 <= A.size() <= 105
1 <= A[i] <= 105


Input Format

The only argument is an Integer Array A.


Output Format

Return an Integer Array, denoting the elements that are divisible by 5 and 7 from the given list.

Example Inpu
Input 1:
A = [5, 7, 70, 50, 35]
Input 2:
A = [105, 57]

Example Output

Output 1:
[70, 35]
Output 2:
[105]

Example Explanation

Explanation 1:
Only 35 and 70 are divisible by 5 and 7 from the list [5, 7, 70, 50, 35]

Therefore the list consisting of only these two elements is returned.
Explanation 2:
105 is divisible by (5 and 7).

'''

def divisible(A):
    '''Returns a list of elements from A that are divisible by both 5 and 7.'''
    return [num for num in A if num % 5 == 0 and num % 7 == 0]


'''Q8. Product of elements

Problem Description:

Write a program that returns the product of all elements present in the array.

Note: The list with elements is already passed as an argument to the function. User don't need to take any input. Just perform the task on the passed arguments and return the required result.

Constraints:

1 <= |A| <= 100
1 <= A <= 100
Note: It is guaranteed that the resultant product will be <= 1015
Input Format:

An integer array **A** as the function argument.
Output Format:

Product of elements in integer format
Sample Input:

A = [7, 9, 2, 51]
Sample Output:

6426
Sample explanation:

The product of all the elements is 7 * 9 * 2 * 51 = 6426 is returned'''

def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result



