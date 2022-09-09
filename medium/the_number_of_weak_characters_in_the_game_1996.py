import random
import time

import pytest

from utils.make_string import get_readme

string_ = """
1996. The Number of Weak Characters in the Game
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
Medium

You are playing a game that contains multiple characters,
and each of the characters has two main properties: attack and defense.

You are given a 2D integer array properties where
properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels 
*strictly greater* than this character's attack and defense levels. More formally, 
a character i is said to be weak if there exists another character j 
where attack_j > attack_i and defense_j > defense_i.

Return the number of weak characters.


Example 1:
-----------------
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.

Example 2:
-----------------
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.

Example 3:
-----------------
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
 

Constraints:
-----------------
2 <= properties.length <= 10^5
properties[i].length == 2
1 <= attack_i, defense_i <= 10^5

9.9.22
"""
N_MAX = int(1e5)
A_MAX = int(1e5)


def number_of_weak_characters(properties: list) -> int:

    def key_func(prop: list):
        return prop[0], -prop[1]

    ans = 0
    stack = []

    properties.sort(key=key_func)

    for _, d in properties:

        while stack and stack[-1] < d:
            stack.pop()
            ans += 1

        stack.append(d)
    return ans


test_data = [
    ([[5, 5], [6, 3], [3, 6]], 0),
    ([[2, 2], [3, 3]], 1),
    ([[1, 5], [10, 4], [4, 3]], 1),
    ([[1, 1], [1, 1]], 0),
    ([[1, 2], [1, 3]], 0),
    ([[1, 2], [1, 3], [1, 4], [1, 5]], 0),
    ([[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]], 2)
]
f_l = [number_of_weak_characters]


@pytest.mark.parametrize('root, expected', test_data)
def test(root, expected):
    for i, f in enumerate(f_l):
        ans = f(root)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    acc = [0] * len(f_l)
    for i in range(n_iter):
        n = N_MAX if i == n_iter - 1 else random.randint(2, N_MAX)
        properties = [[random.randint(1, A_MAX), random.randint(1, A_MAX)] for _ in range(n)]
        random.shuffle(properties)
        properties = properties

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(properties)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for k, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[k])  # 0.21


# # -------------------------------


# TO README
def test_readme():
    topic = 'Stack'
    file_name = 'the_number_of_weak_characters_in_the_game_1996.py'
    print('\n')
    print(get_readme(string_, topic, file_name))
