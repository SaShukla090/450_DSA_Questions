#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        max = arr[0]
        maxSumEndingWith = [None for i in range(N)]
        maxSumEndingWith[0] = arr[0]
        for i in range(1,N):
            S = arr[i] + maxSumEndingWith[i-1]
            maxSumEndingWith[i] = S if  S>arr[i] else arr[i]
            if maxSumEndingWith[i]>max:
                max = maxSumEndingWith[i]
        return max

        ##Your code here

#{
#  Driver Code Starts
#Initial Template for Python 3

# import math


def main():
    T=int(input())
    while(T>0):

        n=int(input())

        arr=[int(x) for x in input().strip().split()]

        ob=Solution()

        print(ob.maxSubArraySum(arr,n))

        T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends