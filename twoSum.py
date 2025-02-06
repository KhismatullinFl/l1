class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                k=len(nums)-1-j
                if(nums[i]+nums[k]==target):
                    return [i,k]
        return []