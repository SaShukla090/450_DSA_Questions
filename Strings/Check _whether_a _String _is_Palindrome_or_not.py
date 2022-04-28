#User function Template for python3
class Solution:
    def isPalindrome(self, S):
        # code here
        N = len(S)
        x = True
        if N == 1:
            return 1
        for i in range((N//2)):
            if S[i] != S[N-i-1]:
                return 0
            else:
                x = True
        return int(x)


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.isPalindrome(S)
        print(answer)

# } Driver Code Ends