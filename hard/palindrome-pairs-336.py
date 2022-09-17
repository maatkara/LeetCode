import pytest

string_ = """
336. Palindrome Pairs
https://leetcode.com/problems/palindrome-pairs/
Hard

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, 
so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:
-------------------
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:
-------------------
Input: words = ["a",""]
Output: [[0,1],[1,0]]
 

Constraints:
-------------------
1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.

Solution:
-------------------
We have a palindrome only in 3 cases:
---------------------------------------------------------------------------------------------------
                                                     Examples:
---------------------------------------------------------------------------------------------------                                                     
1) words[i]=='' and word[j] is a palindrome |       '' + 'aba' ->  'aba' is a palindrome;
2) reversed words[i] is in words            |  reversed 'abcd' -> 'dcba' in words;
3) suffix or prefix of reversed words[i]    |     suffix 'lls' -> 's' in words and 'll' is a palindrome  
   is in other words and rest part          |
   of reversed words[i] is a palindrome     |
 

17.9.22
"""
N_MAX = int(5e3)
A_MAX = int(3e2)


def check_palindrome(word: str, i: int = 0, j: int = None):
    j = j if j is not None else len(word) - 1

    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1

    return True


def palindrome_pairs(words: list) -> list:
    n = len(words)
    words_d = {w: i for i, w in enumerate(words)}
    ans = []

    for i in range(n):
        # 1, words[i]=='' check: are there palindromes among other words?
        if not words[i]:
            for j in range(n):
                if i != j and check_palindrome(words[j]):
                    ans += [[j, i], [i, j]]

        # 2 check: reversed word among other words?
        bw, l_w = words[i][::-1], len(words[i])
        if bw in words_d and words_d[bw] != i:
            ans.append([i, words_d[bw]])

        # 3 check: 1) part (suffix or prefix) of reversed word in words? and 2) rest of rev word is a palindrome?
        for j in range(1, l_w):
            for k in range(2):

                bwj, l, r = (bw[j:], 0, j - 1) if k else (bw[:j], j, l_w - 1)  # suffix if k else prefix

                if bwj in words_d and check_palindrome(bw, l, r):
                    ans += [[i, words_d[bwj]]] if k else [[words_d[bwj], i]]

    return ans


test_data = [
    (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]),
    (["bat", "tab", "cat"], [[0, 1], [1, 0]]),
    (["a", ""], [[0, 1], [1, 0]]),
    (["aba", ""], [[0, 1], [1, 0]]),
    (["aba"], []),
]

f_l = [palindrome_pairs]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: list, expected):
    for i, f in enumerate(f_l):
        ans = f(nums)
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
=============================================
palindrome_pairs  1.3e-04  1.4e-04  3.0e-04
"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'String'
    file_name = 'palindrome-pairs-336.py'
    print('\n')
    print(get_readme(string_, topic, file_name))
