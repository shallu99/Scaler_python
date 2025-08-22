'''Q1. Celsius to Fahrenheit
Problem Description:

Given the temperature of a day in Degrees Celsius, convert this given temperature from Celsius to Fahrenheit. Complete the function to do so. Round the output up to 2 decimal places

Note:

To round up the values -
Python : Use round(ans,2) to round up ans to two decimals
Java : Use Math.round(val*100)/100d to round upto two decimals
The formula to convert Celsius to Fahrenheit is: F = (9/5 * C) + 32
You need not take input in this problem, you need to only implement the function provided.
Input Format:

First and the only line has input in float format representing the temperature.
Output Format:

Fahrenheit value in float format
Sample Input:

36.8
Sample Output:

98.24
'''


def celsius_farhen(Celsius):
    ans = 0
    # YOUR CODE GOES HERE
    c = Celsius
    ans = (9 / 5 * c) + 32

    return round(ans, 2)


celsius_farhen(36.8)

'''Q2. Print Sum of squares
Problem Description:

Given an integer n, write a program to return the sum of squares of first n natural numbers in integer format.

Note1:

The formula for the sum of squares of first n natural numbers is: n(n+1)(2n+1)/6

Note2:

You need not take input in this problem, only implement the function provided.

Problem Constraints:

1 <= N <= 100
Input Format:

The first line indicates the number of test cases.
For each testcase there will be a single line of input with an integer representing n for that testcase.
Output Format:

Sum of squares of n natural numbers in integer format
Sample Input:

1
6
Sample Output:

91
Sample explanation:

According to the formula sum of first 6 natural numbers is 6*(6+1)(12+1)/6=91'''


def sum_squares(n):
    ans = None
    ''' input:Given Integer n
         output: Return ans as sum of squares in integer format.'''

    # YOUR CODE GOES HERE
    ans = int(n * (n + 1) * (2 * n + 1) // 6)

    return ans


sum_squares(n=2)


'''Q4. Find the Area of Circle
Problem Description:

Write a function to calculate and return the area of a circle by using the radius of the circle given as a parameter.
Notes:

Round up the area to 2 decimal places. You can use the round() function.
Use pi as 3.14159.
You need not take input in this problem, you need to only implement the function provided.
Input Format:

The first line indicates the number of the test cases. 
For each test case there will be one line of input in integer format representing radius.
Output Format:

Area in float format rounded upto 2 decimal places for each testcase.
Sample Input:

1  
5
Sample Output:

78.54

Sample explanation:

The area for circle with radius 5cm is 3.14159 x (5 x 5) = 78.53975 cm2

After rounding by 2 dig'''
def circle_area(r):
    ans=None
    '''input: r = A numerical value as radius
       output: Return the area of circle as ans upto 2 decimal places'''
    # YOUR CODE GOES HERE
    ans = 3.14159 * r**2
    ans = round(ans,2)
    return ans

circle_area(r = 45)

'''Q1. Simple Interest
'''
def simple_int(time, pa, ir):
    ''' time = number of days
        pa = principal amount
        ir = annual interest rate in percent
        Returns the total amount (principal + interest), rounded to 2 decimals.
    '''
    # Compute total amount using simple interest formula for days
    ans = pa * (1 + (time / 365) * (ir / 100))
    return round(ans, 2)


'''Q2. Sequence [1-N] & [N-1]
Problem Description:

Write a program to print all Natural numbers from 1 to N and from N to 1 inclusive, where N is given as an argument.

Note1: First print from 1 to N then in new line print again from N to 1

Note2: You need not take input in this problem, you need to only implement the function provided.

Note3: There is 1 line gap between two output lines and a space between numbers in same line.

Problem Constraints:

1 <= N <= 1000
Input Format:

The first line indicates the number of test cases t
The next t lines will have different values of N according to testcases
Output Format:

For each testcase there will be two lines of output:  
The first line is N space-separated integers from 1 to N.
The next line is N space-separated integers from N to 1.
Sample Input:

1
5
Sample Output:

1 2 3 4 5
5 4 3 2 1'''

def sequence(n):
    # Loop from 1 to n
    for i in range(1,n+1):
        if i != n:
            print(i, end=" ")
        else:
            print(i)
    # Loop from 0 to n-1 and print n-j
    for j in range(0,n):
         if j != n-1:
            print(n-j, end=" ")
         else:
            print(n-j)




'''Q3. Road tax
Problem Description:

Write a program that takes the cost price of a vehicle as an argument and returns the road tax, 
that the vehicle owner has to pay according to the following criteria:

Cost price (in Rs)    		Tax
> 1,00,000            		20%
> 75,000 and <= 1,00,000	15%
> 50,000 and <= 75,000		10%
<= 50,000			        5%

Note1: Return the tax up to one decimal place. You can use round(tax,1)

Note2: You need not take input in this problem, you need to only implement the function provided.

Input Format:

The first line indicates the number of test cases. For each testcase there will be a single line of input representing the cost price.
Output Format:

Return tax in float format.
Sample Input 1:

1
25000
Sample Output 2:

1250.0
Sample Explanation 1

The given cost price of vehicle is 25000 which is less than 50,000. 
Hence the tax applicable is 5%. So if we calculate 5% of 25,000, it evaluates to 1250.0.
Sample Input 2:

1
60000
Sample Output 2:

6000.0
Sample Explanation 2

The given cost price of vehicle is 60,000 which is greater than 50,000 but less than 75,000. 
Hence the tax applicable is 10%. So if we calculate 10% of 60,000, it '''

def road_tax(price):
    tax = None
    # use if else to check price range
    if price > 100000:
        tax = 20/100*price
    elif price >75000 and price <=100000:
        tax = 15/100*price
    elif price >50000 and price <=75000:
        tax = 10/100*price
    else:
        tax = 5/100*price
    tax=round(tax,1)
    return tax