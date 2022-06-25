#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n):
        ssum1 = 0
        ssum2 = n*(n+1)*(2*n+1)/6
        sum1 = 0
        sum2 = n*(n+1)/2

        for i in range(n):
            ssum1 = ssum1 + arr[i]*arr[i]
            sum1 = sum1 + arr[i]

        A = (ssum2 - ssum1)/(sum2 - sum1)
        B = sum2 - sum1

        missing = (A+B)/2
        repeating = (A-B)/2

        return [int(repeating),int(missing)]

        # code here

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends