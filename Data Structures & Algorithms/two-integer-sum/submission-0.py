class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hashmap = {}
        for i  in range(len(nums)) :
            diff  = target-nums[i]
            if diff in Hashmap:
                return [Hashmap[diff],i]
            Hashmap[nums[i]] = i 