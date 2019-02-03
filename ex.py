def count_partitions(n, m):
    """Count the ways to partition n using parts up to m."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        print(with_m, without_m)
        return with_m + without_m

def partitions(n, m):
    if n==0:
        return Link(Link.empty)
    elif n<0 or m==0:
        return Link.empty
    else:
        using_m = partitions(n-m, m)
        with_m = map_link(lambda p: Link(m, p), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)
def list_partitions(n, m, lst=[]):
    """List the ways to partition n using parts up to m."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == []:
        return 0
    else:
        with_m = list_partitions(n-m[0], m)
        without_m = list_partitions(n, m[1:])
        lst.append(m)
        print(with_m, without_m)
        total = with_m + without_m
        print(lst)
        return total

def list_partitions(total, max_pieces, max_value):
    """
    >>> list_partitions(1, 1, 1)
    [[1]]
    >>> list_partitions(1, 2, 1)
    [[1]]
    >>> list_partitions(10, 0, 1)
    []
    >>> list_partitions(10, 1, 1)
    []
    >>> list_partitions(10, 1, 10)
    [[10]]
    >>> list_partitions(2, 2, 1)
    [[1, 1]]
    >>> list_partitions(2, 2, 2)
    [[1, 1], [2]]
    >>> list_partitions(3, 3, 3)
    [[1, 1, 1], [2, 1], [3]]
    """
    def helper(t, mp, mv, sofar, partitions):
        #print(t, mp, mv, sofar, partitions)
        if t == 0 and sofar != []:
            partitions = partitions + [sofar]
        if mp <= 0 or mv <= 0 or t <= 0:
            return partitions
        def looper(i, upper, old_parts, partitions):
            #print(i, upper, old_parts, partitions)
            if i >= upper:
                return partitions
            else:
                new_parts = helper(t-i, mp-1, i, sofar + [i], old_parts)
                new_parts = [e for e in new_parts if e != []]
                partitions = partitions + new_parts
                return looper(i+1, upper, old_parts, partitions)
        # print(t, mp, mv, sofar, partitions)
        return looper(1, mv+1, partitions, partitions)

    return helper(total, max_pieces, max_value, [], [])
