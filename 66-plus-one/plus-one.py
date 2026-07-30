class Solution(object):
    def plusOne(self, digits):
    
        num =0
        for digit in digits:
            num = num * 10 + digit
        num += 1

        
        result = []

        while num > 0:
            result.append(num % 10)
            num //= 10

        result.reverse()

        return result
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        