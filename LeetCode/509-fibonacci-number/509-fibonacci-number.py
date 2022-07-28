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