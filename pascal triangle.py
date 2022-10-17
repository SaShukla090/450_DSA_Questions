def nCr(n,r):
    # ans = 0
    u = 1
    d = 1
    if r == 0:
        ans = 1
        return ans
    else:
        for i in range(r):
            u *= n-i
            d *= (i+1)
    ans = u/d
    return int(ans)

def pascal(n):
    for i in range(n):
        for j in range(i+1):
            print(nCr(i,j), end=" ")
        print()

pascal(6)