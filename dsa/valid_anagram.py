def isAnagram(s: str, t: str) -> bool:
        letters = {}
        # counting how many times each letter shows up in s
        # get(i, 0) gives back the current count, or 0 if its the first time seeing it
        # this way no KeyError when the letter isnt in the dict yet
        for i in s:
            letters[i] = letters.get(i, 0) + 1
        
        # if the lengths dont match it can never be an anagram
        if len(s) == len(t):
            for j in t:
                # letter in t that s never had, or the counts dont match -> not an anagram
                # one mismatch is enough to say false straight away
                if j not in letters or t.count(j) != letters[j]:
                    return False
            # every letter survived the check so its an anagram
            return True
            
        return False