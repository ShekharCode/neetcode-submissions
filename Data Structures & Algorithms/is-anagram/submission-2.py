class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = defaultdict(int)
        if len(s)!= len(t):
            return False
        for chr in s:
            dict[chr] = 1+dict.get(chr,0)
        for chr in t:
            dict[chr] = dict.get(chr,0) - 1
        print(dict)
        for key,value in dict.items():
            if value !=0:
                return False
        return True