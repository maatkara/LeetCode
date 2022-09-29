def binary_search(d: list, x: int) -> tuple:
    """ Return the left l and  right r indexes in d:
    Invariant: d[l] <= x < d[r]
    d - ascending sorted (not descending)
    """
    n = len(d)
    l, r = 0, n - 1

    while r - l > 1:  # i.e. not neighbor
        mid = (l + r) // 2

        if d[mid] <= x:
            l = mid
        else:
            r = mid
    return l, r