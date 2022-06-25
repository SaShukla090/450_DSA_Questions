#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):

        # dictt = {}
        # for i in A:
        #     if i in dictt:
        #         dictt[i] += 1
        #     else:
        #         dictt[i] = 1

        # for k, v in dictt.items():
        #     if v>(N//2):
        #         return k
        # return -1

        majorityCandidate = self.findCandidate(A,N)
        majorityElement = self.isMajority(A,majorityCandidate)

        return majorityElement


    def findCandidate(self, A, N):
        maj_index = 0
        count = 1
        for i in range(N):
            if A[maj_index] == A[i]:
                count +=1
            else:
                count -=1

            if count == 0:
                maj_index = i
                count = 1
        return A[maj_index]

    def isMajority(self, A, cand):
        # if cand == True:
        #     return -1


        count = 0
        for i in range(len(A)):
            if A[i] == cand:
                count += 1
        if count > (len(A)/2):
            return cand
        else:
            return -1


        #Your code here

#{
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T=int(input())
    while(T>0):

        N=int(input())

        A=[int(x) for x in input().strip().split()]


        obj = Solution()
        print(obj.majorityElement(A,N))

        T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends