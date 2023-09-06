#Fibonacci Number
class Solution:
    def fib(self, n: int) -> int:
        solution=Solution()
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return solution.fib(n-1)+solution.fib(n-2)
