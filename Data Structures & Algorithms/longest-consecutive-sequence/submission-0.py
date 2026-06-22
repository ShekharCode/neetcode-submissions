class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 0
        
        for i in range(len(nums)):
            current_num = nums[i]
            current_streak = 1
            
            # Check for the next consecutive numbers
            while current_num+1 in nums:
                current_num+=1
                current_streak+=1
            
            longest = max(longest, current_streak)
        
        return longest


        