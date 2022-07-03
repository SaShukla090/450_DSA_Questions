
#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr, n):
        ma=arr[0]
        mn=arr[0]
        ans=arr[0]
        for i in range(1,n):
            if arr[i]<0:
                ma,mn=mn,ma
            ma=max(arr[i],arr[i]*ma)
            mn=min(arr[i],arr[i]*mn)
            ans=max(ma,ans)

        return ans
#{
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends