import re

import pytest

string_ = """
838. Push Dominoes
https://leetcode.com/problems/push-dominoes/
Medium

There are n dominoes in a line, and we place each domino vertically upright. 
In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. 
Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force 
to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

Example 1:
------------------------
Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example 2:
------------------------
838domino.png
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 

Constraints:
------------------------
n == dominoes.length
1 <= n <= 10^5
dominoes[i] is either 'L', 'R', or '.'.

Solution
------------------------
Idea: 
------------
The whole string can be divided into groups with the pattern 'letter + one or more dots + letter'.
There are only 3 variants for such groups:

| #   | Pattern                  | TODO                                                                                                                                        |
|-----|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| 1)  | R.(...).R or L.(...).L   | Replace the dot to R or L, respectively                                                                                                     |
| 2)  | L.(...).R                | No change                                                                                                                                   |
| 3)  | R.(...).L                | First and last n//2 dots will be replaced by R or L, respectively.<br/>If there is an odd number of dots here, leave the central one as is. |

Solution:
------------
1. Add L and R on both sides of the dominoes.
2. Selecting the r'\w\.+\w' pattern (letter + one or more dots + letter).
3. Replace the pattern so that there are no more dots left 
using the imaginary change of point to X (dominoes = re.sub(pattern, sub_func, dominoes))
4. Repeat replacement (item 1).
Re-replacement is needed because the sub function return the string obtained by replacing the 
leftmost `non-overlapping occurrences` of the pattern in string.
5. Replace 'X' to dot and discard 1 and the last character (see item 1).
    

27.9.22
"""
N_MAX = int(1e5)
N_MIX = 1
# A_MIN = 0
# A_MAX = 1000


def sub_func(r):
    match = r.group(0)
    ch0 = match[0]

    if ch0 == match[-1]:
        return match.replace('.', ch0)

    if ch0 == 'L':
        return match.replace('.', 'X')

    n_sub, rest = divmod(len(match), 2)
    return ''.join((match[: n_sub].replace('.', 'R'),
                    match[n_sub:n_sub + rest].replace('.', 'X'),
                    match[n_sub + rest:].replace('.', 'L')))


def push_dominoes(dominoes: str) -> str:
    dominoes = ''.join(('L', dominoes, 'R'))
    pattern = re.compile(r'(\w\.+\w)')

    for _ in range(2):
        dominoes = re.sub(pattern, sub_func, dominoes)

    return dominoes[1:-1].replace('X', '.')


test_data = [
    ("RR.L", "RR.L"),
    (".L.R...LR..L..", "LL.RR.LLRRLL.."),
    (".R..L.", ".RRLL."),
    (".R..L.L.R", ".RRLLLL.R"),
    (".R..L..R..L.", ".RRLL..RRLL.")
]

f_l = [push_dominoes]


@pytest.mark.parametrize('dominoes,expected', test_data)
def test(dominoes, expected):
    for i, f in enumerate(f_l):
        ans = f(dominoes)
        print('\n', f.__name__, ans)
        assert ans == expected


# def test_time(n_iter: int = 100):
#     from utils.print_time4random import print_time
#
#     print_time(f_l, args=None,
#                n_max=N_MAX,  # a_max=A_MAX,
#                n_min=N_MIX,  # a_min=A_MIN,
#                n_iter=n_iter)
#
#
# """
# TIME:
# """
#
#
# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'String'
    file_name = 'push-dominoes-838.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
