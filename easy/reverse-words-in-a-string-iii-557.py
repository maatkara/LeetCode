import pytest

string_ = """
557. Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
Easy

Given a string s,
reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:
-----------------------
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
----------------------
Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:
----------------------
1 <= s.length <= 5 * 10^4
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.

22.9.22
"""
N_MAX = int(5e5)
N_MIX = 1


def reverse_words(s: str) -> str:
    ans = []

    for word in s.split():
        ans.append(word[::-1])

    return ' '.join(ans)


def reverse_words1(s: str) -> str:
    return ' '.join(word[::-1] for word in s.split())


def reverse_words2(s: str) -> str:
    """ Submitted to LC """
    return ' '.join(s.split()[::-1])[::-1]


test_data = [
    ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    ("God Ding", "doG gniD"),
    ('d', 'd'),
    ('fffff', 'fffff')
]

f_l = [reverse_words2, reverse_words1, reverse_words]


@pytest.mark.parametrize('s, expected', test_data)
def test(s, expected):
    for i, f in enumerate(f_l):
        ans = f(s)
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
===========================================
reverse_words2  1.7e-06  2.0e-03  3.9e-03
reverse_words1  2.7e-06  4.2e-03  8.4e-03
reverse_words   1.6e-06  4.4e-03  8.6e-03
"""
# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Two pointer'
    file_name = 'reverse-words-in-a-string-iii-557.py'
    print('\n')
    print(get_readme(string_, topic, file_name))
