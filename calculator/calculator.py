"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""
    stack = []
    for i in range(-1, -len(s)-1, -1):
        if s[i].isdigit():
            stack.append(s[i])
            continue
        if s[i] in '+-*/':
            if len(stack) != 2:
                raise ValueError
            a = int(stack.pop())
            b = int(stack.pop())
            if s[i] == '+':
                c = a + b
            elif s[i] == '-':
                c = a - b
            elif s[i] == '*':
                c = a * b
            elif s[i] == '/':
                c = a // b
            if i != - len(s):
                stack.append(c)

    return c


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")
