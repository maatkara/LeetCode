import random
import string

import pytest

string_ = """
71. Simplify Path
https://leetcode.com/problems/simplify-path/description
Medium
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style 
file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' 
refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. 
For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory 
        (i.e., no period '.' or double period '..')
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
 

Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.

19.10.23
"""
N_MIN = 1
N_MAX = int(1e4)


def simplify_path(path: str) -> str:
    path = path.split('/')
    stack = []

    for w in path:
        if not w or w == '.':
            continue
        elif w == '..':
            if not stack:
                continue
            stack.pop()
        else:
            stack.append(w)

    return '/' + '/'.join(stack)


test_data = [
    ("/home/", "/home"),
    ("/../", "/"),
    ("/home//foo/", "/home/foo"),
    ("/abc/...//", "/abc/..."),
    ("/abc/...", "/abc/...")
]

f_l = [simplify_path]


@pytest.mark.parametrize('nums, expected', test_data)
def test(nums: str, expected: bool):
    for f in f_l:
        ans = f(nums)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    # import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        m: int = N_MAX // 10 if i == n_iter - 1 else n // 10
        k = 4 if n - m > 4 else min(1, n - m)

        nums = random.choices(string.ascii_letters + string.digits + '_', k=n - m - k) + ['/'] * m + ['.'] * k
        random.shuffle(nums)

        return '/' + ''.join(nums),

    print_time(f_l, get_args, n_iter)


"""
TIME:
                 min      mean     max
==========================================
simplify_path  3.6e-06  7.3e-05  3.3e-04
==========================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Stack'
    file_name = 'simplify-path-71.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
