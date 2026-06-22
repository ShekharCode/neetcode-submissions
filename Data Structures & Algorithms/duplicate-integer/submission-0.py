class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = defaultdict(int)
        for num in nums:
            if num in c:
                return True
            c[num]+=1
        return False
        
         