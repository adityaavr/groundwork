from typing import List


def reverse_string_o_n(s: str):
    l = []
    for i in s:
        l.append(i)
    
    k = []
    while len(l) != 0:
        print("Length of l: ", len(l))
        # using the initial array to iterate by retaining last elem in memory, and cutting it out. 
        # we then use that to make the new array of the reversed string
        k.append(l.pop(-1))
          
    string = ""  
    for x in k:
        string += x
        
    print(string)
    return string

reverse_string_o_n("banana")
