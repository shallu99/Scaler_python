
# @param A : integer
# @return an integer
def solve(A):
    count = 0
    for i in range(1,A +1):
        if A % i ==0:
            count +=1
    print(count)
    return count

solve(A= 49)