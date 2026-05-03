class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nlen=len(nums)
        for i in range(nlen):
            for j in range(i+1,nlen):
                if nums[i]+nums[j]==target:
                    return [i,j]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in num_map:
                return [i, num_map[compl]]
            num_map[nums[i]] = i