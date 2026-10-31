class Solution(object):
    def replaceElements(self, arr):
        n = len(arr)
        max_elm = -1
        for i in range (n-1,-1,-1):
            temp = arr[i]
            arr[i] = max_elm
            max_elm = max(max_elm,temp)
        return arr
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        