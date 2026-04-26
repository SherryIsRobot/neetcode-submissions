class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        if len(s) != len(t):
            return false

        countS, countT = {}, {}

        for i in s:
            countS[i] = 1 + countS.get(i, 0)
            countT[i] = 1 + countT.get(i, 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
    
        return True
    
sol = Solution()
print(sol.isAnagram("racecar", "carrace"))