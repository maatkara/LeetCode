import string

import pytest

string_ = """
990. Satisfiability of Equality Equations
https://leetcode.com/problems/satisfiability-of-equality-equations/
Medium

You are given an array of strings equations that represent relationships between variables 
where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".
Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations,
or false otherwise.

Example 1:
-------------------
Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

Example 2:
-------------------
Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Constraints:
-------------------
1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.

Solution
1. Divide the equations into equalities('==') and inequalities('!=').
2. Union two variables from equalities('==') into one set (class DisjointSets) with one i_id (self.parents).
3. Let's check if both variables from inequality is in the same set of the 'equals'

26.9.22
"""
N_MAX = int(5e2)
N_MIX = 1


# A_MIN = 0
# A_MAX = 1000


class DisjointSets:
    def __init__(self, n):
        self.parents = list(range(n + 1))  # size= n+1: for i = 1 parents[i] = parents[1]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return
        self.parents[i_id] = j_id

    def find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])  # Rewrite the root of the vertex i which is on the way
        return self.parents[i]

    def __str__(self):
        return f'parents: {self.parents}\n'


def equations_possible(equations: list) -> bool:
    ds = DisjointSets(26)
    d_l = []
    d = {s: i for i, s in enumerate(string.ascii_lowercase)}

    for eq in equations:
        eq = eq.split('=')
        a, b = d[eq[0][0]], d[eq[-1]]

        if len(eq) == 3:  # "=='
            if a != b:
                ds.union(a, b)
        else:  # "!='
            if a == b:
                return False
            d_l.append((a, b))

    del equations
    for (i, j) in d_l:
        if ds.find(i) == ds.find(j):
            return False

    return True


test_data = [
    (["a==b", "b!=a"], False),
    (["b==a", "a==b"], True),
    (["b==a", "a==b", "c==d", "e!=f"], True),
    (["b!=a"], True),

]

f_l = [equations_possible]


@pytest.mark.parametrize('equations,expected', test_data)
def test(equations, expected):
    for i, f in enumerate(f_l):
        ans = f(equations)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time

    print_time(f_l, args=None,
               n_max=N_MAX,  # a_max=A_MAX,
               n_min=N_MIX,  # a_min=A_MIN,
               n_iter=n_iter)


"""
TIME:
                      min      mean     max
===============================================
equations_possible  2.9e-06  3.5e-05  2.6e-04
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Union'
    file_name = 'satisfiability-of-equality-equations-990.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
