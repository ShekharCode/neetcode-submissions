class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        new_lst = sorted(c.items(),reverse = True,key = lambda x : x[1])
        count = 0
        res = []
        for key,value in new_lst:
            if count == k:
                return res
            res.append(key)
            count+=1
        return res