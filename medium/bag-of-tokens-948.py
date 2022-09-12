import pytest

from utils.make_string import get_readme

string_ = """
948. Bag of Tokens
https://leetcode.com/problems/bag-of-tokens/
Medium

You have an initial power of power, an initial score of 0,
and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], 
                you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1,
                you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order.
                You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.
 

Example 1:
----------------------
Input: tokens = [100], power = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because
you either have too little power or too little score.

Example 2:
----------------------
Input: tokens = [100,200], power = 150
Output: 1

Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
There is no need to play the 1st token since you cannot play it face up to add to your score.

Example 3:
----------------------
Input: tokens = [100,200,300,400], power = 200
Output: 2

Explanation: Play the tokens in this order to get a score of 2:
1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.
 

Constraints:
----------------------
0 <= tokens.length <= 1000
0 <= tokens[i], power < 10^4

Solution
-----------------------
Sort the tokens and move the two printers.
Take the score with the left pointer while there is enough power, and take the power with the right.

12.9.22
"""
N_MAX = int(1e3)
A_MAX = int(1e4)


def bag_of_tokens_score(tokens: list, power: int) -> int:
    n = len(tokens)
    tokens.sort()

    i, j = 0, n - 1
    score = 0

    while i <= j:
        if power >= tokens[i]:
            score += 1
            power -= tokens[i]
            i += 1
        elif score and j - i >= 1:  # Only one token left: no profit taking the power
            power += tokens[j]
            score -= 1
            j -= 1
        else:
            return score
    return score


test_data = [
    ([100], 50, 0),
    ([100, 200], 150, 1),
    ([100, 200, 0], 150, 2),
    ([100, 200, 201], 100, 1),
    ([100, 200, 300, 400], 200, 2),
    ([100, 200, 300, 400, 500], 200, 2),
    ([100, 200, 300, 400, 500], 0, 0),
    ([0, 200, 300, 400, 500], 0, 2)
]
f_l = [bag_of_tokens_score]


@pytest.mark.parametrize('tokens, power, expected', test_data)
def test(tokens: list, power: int, expected):
    for i, f in enumerate(f_l):
        ans = f(tokens, power)
        print('\n', f.__name__, ans)
        assert ans == expected


def test_time(n_iter: int = 100):
    import random
    import time

    acc = [0] * len(f_l)
    for i in range(n_iter):
        n = N_MAX if i == n_iter - 1 else random.randint(1, N_MAX)
        power = random.randint(0, A_MAX)
        tokens = [random.randint(0, A_MAX) for _ in range(n)]

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(tokens, power)
            t1 = time.perf_counter()

            acc[j] = max(acc[j], t1 - t0)

    for k, f in enumerate(f_l):
        print('\n  ', f.__name__, acc[k])  # 0.00017


# -------------------------------


# TO README
def test_readme():
    topic = 'Two pointer'
    file_name = 'bag-of-tokens-948.py'
    print('\n')
    print(get_readme(string_, topic, file_name))
