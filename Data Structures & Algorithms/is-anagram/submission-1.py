class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)

        for letter in t:
            c[letter]-=1
        for cnt in c.values():
            if cnt !=0:
                return False
        return True


        