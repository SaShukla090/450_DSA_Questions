#User function Template for python3
import math
def minSwap (arr, n, k) :
    count = 0
    for i in range(n):
        if arr[i] <= k:
            count += 1
    bad = 0
    for i in range(count):
        if arr[i]>k:
            bad +=1
    ans = bad
    for i in range(1,n - count + 1):
        if arr[i-1]>k:
            bad -=1
        if arr[i+count-1]>k:
            bad +=1
        if bad < ans:
            ans = bad
    return ans



    #Complete the function




#{
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = minSwap(arr, n, k)
    print(ans)






# } Driver Code Ends