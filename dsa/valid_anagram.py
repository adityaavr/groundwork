def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for i in s:
            letters[i] = letters.get(i, 0) + 1
        
        if len(s) == len(t):
            for j in t:
                if j not in letters or t.count(j) != letters[j]:
                    return False
            return True
            
        return False