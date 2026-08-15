class Solution:
    def reverse(self, x: int) -> int:
        original = x
        x = abs(x)
        string = str(x)
        l = []
        for i in string:
            l.append(i)
        
        k = []
        while len(l) != 0:
            k.append(l.pop(-1))

        string = ""
        for x in k:
            string += x
        result = int(string)
        if original < 0:
            result *= -1
        if result < -(2**31) or result > (2**31) - 1:
            return 0

        return result
        
        