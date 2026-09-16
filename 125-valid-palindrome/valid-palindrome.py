class Solution(object):
    def isPalindrome(self, s):
        a =""
        for ch in s:
            if ch.isalnum():
                a+=ch.lower()
        return a == a[::-1]
        """
        :type s: str
        :rtype: bool
        """
        