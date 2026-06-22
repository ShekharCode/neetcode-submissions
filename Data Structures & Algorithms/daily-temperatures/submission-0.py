class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #O(n2)
        res = 0
        ans = []
        for i in range(len(temperatures)):
            res = 0
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res = j-i
                    break
            ans.append(res)
            
        return ans
        