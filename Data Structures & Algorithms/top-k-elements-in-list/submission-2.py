class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = []
        sorted_list = sorted(c.items(),key = lambda x:x[1],reverse = True)
        for key,value in sorted_list:
            if k >0:
                res.append(key)
            k-=1
        return res


            

        