class Solution(object):
    def reverseWords(self, s):
        alphabet = s.split()
        alphabet.reverse()
        return " ".join(alphabet)
        """
        :type s: str
        :rtype: str
        """
        