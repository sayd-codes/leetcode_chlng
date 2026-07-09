class Solution(object):
    def validPalindrome(self, s):

        def palindromeCheck(l,r):
            left , right = l,r
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        left,right = 0 ,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return palindromeCheck(left+1,right) or palindromeCheck(left,right-1)
            left+=1
            right-=1
        return True
        """
        :type s: str
        :rtype: bool
        """
        