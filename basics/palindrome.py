def is_palindrome(s: int):
    k = str(s)
    l = []
    for i in k:
        l.append(i)
        
    j = []
    f = len(l) - 1 # final index of the array
    while len(l) != len(j):
        j.append(l[f])
        f -= 1 # iterate down from final index to first index then append
        
    if l == j: # compare the two arrays to check if palindrome
        print("true")
    else:
        print("false")

    return 
        
is_palindrome(-121)