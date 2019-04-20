class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_indice = [(v,k) for k, v in enumerate(nums)]
        num_indice.sort()
        i = 0
        j = len(num_indice) -1
        while i < j:
            a = num_indice[i][0]
            b = num_indice[j][0]
            if a + b < target:
                i= i+1
            elif a + b > target:
                j = j-1
            else:
                break
        return [num_indice[i][1],num_indice[j][1]]