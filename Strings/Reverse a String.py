class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(len(s)//2):
            s[i], s[n-1-i] = s[n-1-i], s[i]

        """
        Do not return anything, modify s in-place instead.
        """
        