def pingpong(n):
    def helper(k, direction, ret):
        if k == n:
            return ret + direction
        elif k % 7 == 0 or has_seven(k):
            return helper(k + 1, -direction, ret + direction)
        else:
            return helper(k + 1, direction, ret + direction)

    return helper(1, 1, 0)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def g_iter(n):
    if n == 1 or n == 2 or n == 3:
        return n
    g1, g2, g3 = 3, 2, 1
    i, current = 4, 0
    while i <= n:
        current = g1 + 2*g2 + 3*g3
        g1, g2, g3 = current, g1, g2
        i += 1
    return current
