import random
import string
import time
from collections import Counter, defaultdict

import pytest

"""
383. Ransom Note
https://leetcode.com/problems/ransom-note/
Easy

Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
!N Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

23.08.2022
"""
N_MAX = 105
X_MAX = 26


def can_construct(ransom_note: list, magazine: str) -> bool:
    """Return true if ransom_note can be constructed by using the letters from magazine and false otherwise"""

    magazine_d = Counter(magazine)
    ransom_note_d = defaultdict(int)
    del magazine

    for key in ransom_note:
        if key not in magazine_d:
            return False
        ransom_note_d[key] += 1

    for key in ransom_note_d:
        if ransom_note_d[key] > magazine_d[key]:
            return False

    return True


a_l = [random.choice(string.ascii_lowercase) for _ in range(1, N_MAX + 1)]
a_lr = ''.join(ch for ch in reversed(a_l))
a_l = ''.join(a_l)

test_data = [
    ('a', 'b', False),
    ('aa', 'ab', False),
    ('aa', 'aab', True),
    ('aa', 'aab', True),
    (a_l, a_lr, True)
]


@pytest.mark.parametrize('ransom_note, magazine, expected', test_data)
def test(ransom_note, magazine, expected):
    f = can_construct
    assert f(ransom_note, magazine) == expected


def test_time(n_iter=100):
    f = can_construct
    acc = 0
    for _ in range(n_iter):
        n = random.randint(1, N_MAX)
        magazine = ''.join([random.choice(string.ascii_lowercase) for _ in range(1, N_MAX + 1)])
        ransom_note = ''.join([random.choice(string.ascii_lowercase) for _ in range(1, n + 1)])
        t0 = time.perf_counter()
        f(ransom_note, magazine)
        t1 = time.perf_counter()

        acc = max(acc, t1 - t0)

    print('\n', acc)  # 2e-5

    # max time
    ransom_note = ''.join([random.choice(string.ascii_lowercase) for _ in range(1, N_MAX + 1)])
    magazine = ''.join([random.choice(string.ascii_lowercase) for _ in range(1, N_MAX + 1)])
    t0 = time.perf_counter()
    f(ransom_note, magazine)
    t1 = time.perf_counter()

    acc = max(acc, t1 - t0)

    print('\n', acc)  # 2e-5
    assert acc < 0.1
