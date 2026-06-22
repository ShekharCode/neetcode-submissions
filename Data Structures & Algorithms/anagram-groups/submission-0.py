class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dict = [0] * len(strs)
        
        for i in range(len(strs)):
            if dict[i] == 0:  # Only process if not already grouped
                current_group = [strs[i]]
                dict[i] = 1
                for j in range(i + 1, len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]) and dict[j] == 0:
                        current_group.append(strs[j])
                        dict[j] = 1
                res.append(current_group)
        
        return res
        