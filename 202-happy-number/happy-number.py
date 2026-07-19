class Solution(object):
    def sumofsquaresofdigits(self,n):
        sum = 0
        while n>0:
          digits = n%10
          sum+=digits*digits
          n//=10
        return sum
    def isHappy(self, n):
        slow = n
        fast = n
        while True:
            slow = self.sumofsquaresofdigits(slow)
            fast = self.sumofsquaresofdigits(self.sumofsquaresofdigits(fast))
            if fast==1:
              return True
            if slow == fast:
              return False
        """
        :type n: int
        :rtype: bool
        """
        