"""
Задача №31
========================================
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
========================================
Input: 7
Output: 21
"""

def fibbonaci(num: int, prev1 = None, prev2 = None):
    if num == 1:
        return 1
    prev1 = num
    prev2 = num - 1
    return num + fibbonaci(num - 1, prev1, prev2)

print(fibbonaci(3))