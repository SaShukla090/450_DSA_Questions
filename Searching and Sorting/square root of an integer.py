#User function Template for python3

class Solution:
    def countSquares(self, N):
        # low = 1
        # high = 1
        # while(high*high < N):
        #     low = high
        #     high *=2

        # while(low<=high):
        #     mid = low + (high - low)/2

        #     if (mid * mid < N):
        #         low = mid  + 1
        #     else:
        #         high = mid -1
        # return int(high) if high*high<=N else int(high -1)
        count = 0
        s = math.sqrt(N)
        if s%1 == 0:
            return int(s)-1
        else:
            return int(s)
        # code here

#{
#  Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        N=int(input())

        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends