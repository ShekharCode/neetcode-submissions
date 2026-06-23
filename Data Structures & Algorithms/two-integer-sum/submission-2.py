class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = dict()
        for i,num in enumerate(nums):
            k = target - num
            if k in mapping:
                return [mapping[k], i]
            mapping[num] = i
        