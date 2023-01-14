import heapq
import random
import string
from collections import Counter

import pytest

string_ = """
692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/
Medium

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. 
Sort the words with the same frequency by their lexicographical order.

Example 1:
----------
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
----------
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
 with the number of occurrence being 4, 3, 2 and 1 respectively.

Constraints:
----------
1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
 
Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

Solution:
What Time Complexity for heapq.nsmallest(k, ws)?

heapq.nsmallest is O(k + (n - k)logk). 
It creates a max-heap with k elements and then iterates over the remaining n - k elements, 
only adding them to the list if they are smaller than the heap's max element. 
This way when the loop is done, heap will consist of k smallest elements.


14.01.23
"""
N_MAX = 500
N_MIN = 1

A_MAX = 10
A_MIN = 1


def top_k_frequent(words: list[str], k: int) -> list[str]:
    """ Stack. TC O(n log k) SC = O(n) """
    words = [(-f, w) for w, f in Counter(words).items()]  # O(n)

    return [w for _, w in heapq.nsmallest(k, words)]  # O(k + (n - k)log k) < O(n log k)


test_data = [
    (["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]),
    (["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4,
     ["the", "is", "sunny", "day"]),
    (['one'], 1, ['one'])
]

f_l = [top_k_frequent]


@pytest.mark.parametrize('words, k, expected', test_data)
def test(words: list[str], k: int, expected: list[str]):
    for f in f_l:
        ans = f(words, k)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    from random import randint

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else randint(N_MIN, N_MAX)
        words = [''.join(random.choices(string.ascii_lowercase, k=randint(A_MIN, A_MAX))) for _ in range(N_MIN, n)]
        n_un = len(set(words))
        k = n_un if i == n_iter - 1 else randint(N_MIN, n_un)

        return words, k

    print_time(f_l, get_args, n_iter)


"""
TIME: 
                  min      mean     max
===========================================
top_k_frequent  4.1e-06  1.1e-04  3.3e-04
===========================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Heap'

    file_name = 'top-k-frequent-words-692.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
