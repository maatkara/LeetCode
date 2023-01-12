from collections import defaultdict, Counter

import pytest

string_ = """
299. Bulls and Cows
https://leetcode.com/problems/bulls-and-cows/?envType=study-plan&id=level-1
Medium

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, 
you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. 
Note that both secret and guess may contain duplicate digits.

Example 1:
-------------
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Example 2:
-------------
Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow 
since the non-bull digits can only be rearranged to allow one 1 to be a bull.

Constraints:
-------------
1 <= secret.length, guess.length <= 1000
secret.length == guess.length
secret and guess consist of digits only.
Space complexity: O(1)

12.01.23
"""
N_MAX = int(1e3)
N_MIN = 1


def get_hint(secret: str, guess: str) -> str:
    """ TC: O(n), SC:  O(1)"""
    bulls = 0
    freq_s = defaultdict(int)
    freq_g = defaultdict(int)

    for s, g in zip(secret, guess):
        if s == g:
            bulls += 1
        else:
            freq_s[s] += 1
            freq_g[g] += 1

    cows = sum(min(freq_s[ch], freq_g[ch]) for ch in freq_s)

    return f'{bulls}A{cows}B'


def get_hint1(secret: str, guess: str) -> str:  # sub
    """ TC: O(n), SC:  O(1)"""
    freq_s = Counter(secret)
    freq_g = Counter(guess)

    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(freq_s[ch], freq_g[ch]) for ch in freq_s) - bulls

    return f'{bulls}A{cows}B'


def get_hint2(secret: str, guess: str) -> str: 
    """ TC: O(n), SC:  O(1)"""
    freq_s = Counter(secret)
    freq_g = Counter(guess)

    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum((freq_s & freq_g).values()) - bulls

    return f'{bulls}A{cows}B'


test_data = [
    ('1807', '7810', '1A3B'),
    ('1123', '0111', '1A1B'),
    ('1111', '0123', '1A0B'),
    ('1', '1', '1A0B'),
    ('1', '2', '0A0B'),
    ('10', '01', '0A2B'),
    ('10', '10', '2A0B'),

]

f_l = [get_hint, get_hint1, get_hint2]


@pytest.mark.parametrize('secret, guess, expected', test_data)
def test(secret: str, guess: str, expected: str):
    for f in f_l:
        ans = f(secret, guess)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint, choices

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        s = ''.join(choices([str(i) for i in range(10)], k=n))
        g = ''.join(choices([str(i) for i in range(10)], k=n))

        return s, g

    print_time(f_l, get_args, n_iter)


"""
TIME: 
             min      mean     max
======================================
get_hint   4.5e-06  7.6e-05  1.6e-04
get_hint1  5.3e-06  6.9e-05  1.5e-04  sub
get_hint2  5.4e-06  6.8e-05  1.4e-04
======================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Hash'

    file_name = 'bulls-and-cows-299.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
