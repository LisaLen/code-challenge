'''
Write a function fib() that takes an integer nn and returns the nnth Fibonacci ↴ number.

>>> fib(4)
3
>>> fib(0)
0
>>> fib(1)
1
>>> fib(10)
55

>>> f = Fibonacci()
>>> f.fib(4)
3
>>> f.fib(0)
0
>>> f.fib(1)
1
>>> f.fib(10)
55

'''

def fib(n):

    if n == 0 or n == 1:
        return n
    
    return fib(n-1) + fib(n-2)


# with memoization 
class Fibonacci(object):

    def __init__(self):
        self.memo ={}

    def fib(self, n):

        if n in [0, 1]:
            return n

        if n in self.memo:
            return self.memo[n]

        result = self.fib(n-1) + self.fib(n-2)

        self.memo[n] = result

        return result

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")       