#User function Template for python3


def find(arr,n,x):
    s = 0
    e = n-1

    while (True):
        mid = (e-s)//2
        if arr[mid] == x:
            index = mid
            break
        elif arr[mid] < x:
            s = mid

        elif arr[mid] > x:
            e = mid
    first = last = index
    i = 1
    while True:
        if arr[index - i] == x:
            first -= 1
        if arr[index + i] == x:
            last += 1

        if arr[index - i] !=x and arr[index+1] != x:
            break
        i += 1
    return first, last


    # code here




#{
#  Driver Code Starts
# t=int(input())
# for _ in range(0,t):
#     l=list(map(int,input().split()))
#     n=l[0]
#     x=l[1]
#     arr=list(map(int,input().split()))
#     ans=find(arr,n,x)
#     print(*ans)
# # } Driver Code Ends

arr = []