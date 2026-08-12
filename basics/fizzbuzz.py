from typing import List


def fizzbuzz(n: int) -> List[str]:
    arr = []
    i = 1
    for i in range(i, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
        elif i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
            i = "Buzz"
        arr.append(i)
    return arr
            
print(fizzbuzz(15))
            