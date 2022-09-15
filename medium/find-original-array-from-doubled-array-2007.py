import pytest

string_ = """
2007. Find Original Array From Doubled Array
https://leetcode.com/problems/find-original-array-from-doubled-array/
Medium

An integer array original is transformed into a doubled array changed 
by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. 
If changed is not a doubled array, return an empty array. 
The elements in original may be returned in any order.
 

Example 1:
-------------------
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]

Explanation: 
One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:
-------------------
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:
-------------------
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.

Hints^

1. If changed is a doubled array, you should be able to delete elements 
and their doubled values until the array is empty.

2. Which element is guaranteed to not be a doubled value? It is the smallest element.

3. After removing the smallest element and its double from changed, 
is there another number that is guaranteed to not be a doubled value?

Constraints:
-------------------
1 <= changed.length <= 10^5
0 <= changed[i] <= 10^5


15.9.22
"""
N_MAX = int(1e5)
A_MAX = int(1e5)


def find_original_array(changed: list) -> list:
    if len(changed) % 2:
        return []

    original = []
    m = max(changed)
    ht = [0] * (m + 1)

    for el in changed:
        ht[el] += 1
    del changed

    i = 0
    while 2 * i < m + 1:

        if not ht[i]:
            i += 1
            continue

        while ht[i]:  # > 0 or < 0 (for 0 in changed)
            if ht[2 * i] > 0:
                original.append(i)
                ht[i] -= 1
                ht[2 * i] -= 1
            else:
                return []
        i += 1

    return original if not sum(ht) else []


test_data = [
    ([6, 12, 24, 48, 9, 18], [6, 9, 24]),
    ([1, 3, 4, 2, 6, 8], [1, 3, 4]),
    ([6, 3, 0, 1], []),
    ([1], []),
    ([1, 3, 4, 2, 6, 8, 9], []),
    ([1, 3, 4, 2, 6, 8, 1, 2], [1, 1, 3, 4]),
    ([1, 3, 2, 6, 8, 1, 2], []),
    ([0, 0, 1, 3, 4, 2, 6, 8, 1, 2], [0, 1, 1, 3, 4]),
    ([0, 0, 1, 3, 4, 2, 6, 0, 1, 2], []),
    ([0] * 10, [0] * 5),
    (range(N_MAX), []),
    ([N_MAX] * N_MAX, []),
    ([4, 0, 3, 0], []),
    ([4, 8, 0, 0], [0, 4])
]

f_l = [find_original_array]


@pytest.mark.parametrize('changed, expected', test_data)
def test(changed: list, expected):
    for i, f in enumerate(f_l):
        ans = f(changed)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    print_time(f_l, args=None,
               n_max=N_MAX, a_max=A_MAX,
               n_min=1, a_min=0, n_iter=n_iter)


"""
TIME:
                       min      mean     max
================================================
find_original_array  3.4e-03  3.6e-03  4.0e-03
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'
    file_name = 'find-original-array-from-doubled-array-2007' + 'py'
    print('\n')
    print(get_readme(string_, topic, file_name))
