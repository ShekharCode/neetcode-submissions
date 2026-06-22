class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1] * len(nums)
        for i in range(len(nums)):
            res = 1
            for j in range(len(nums)):
                if i == j :
                    continue
                res = res*nums[j]
            temp[i] = res
        return temp
        