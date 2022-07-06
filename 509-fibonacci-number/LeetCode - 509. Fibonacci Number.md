# LeetCode - 509. Fibonacci Number

## 접근

얘는... 딱히 설명할 필요가 없을듯

기본적인 피보나치 수열 문제!

```python
class Solution:
    def fib(self, n: int) -> int:
        num1 = 1
        num2 = 1
        temp = 0
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        for _ in range(n-2):
            temp = num1 + num2
            num1 = num2
            num2 = temp

        return num2
```

