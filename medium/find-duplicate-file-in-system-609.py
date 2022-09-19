from collections import defaultdict

import pytest

string_ = """
609. Find Duplicate File in System
https://leetcode.com/problems/find-duplicate-file-in-system/
Medium

Given a list paths of directory info, including the directory path, and all the files with contents in this directory,
return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:
"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) 
respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. 
If m = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. 
For each group, it contains all the file paths of the files that have the same content. 
A file path is a string that has the following format:
"directory_path/file_name.txt"

Example 1:
-----------------------
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
Example 2:

Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Follow up:
-----------------------
Imagine you are given a real file system, how will you search files? DFS or BFS?
If the file content is very large (GB level), how will you modify your solution?
If you can only read the file by 1kb each time, how will you modify your solution?
What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part
of it? How to optimize?
How to make sure the duplicated files you find are not false positive?

Constraints:
-----------------------
1 <= paths.length <= 2 * 10^4
1 <= paths[i].length <= 3000
1 <= sum(paths[i].length) <= 5 * 10^5
paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.
You may assume no files or directories share the same name in the same directory.
You may assume each given directory info represents a unique directory. 
A single blank space separates the directory path and file info.

19.9.22
"""
N_MAX = int(2e4)
N_MIX = 1
A_MAX = int(3e3)
A_MIN = 1


def find_duplicate(paths: list) -> list:
    ans = defaultdict(list)

    while paths:
        path_info = paths.pop()
        dir_, *fs = path_info.split()
        for f in fs:
            f_name, content = f.split('(')
            ans[content].append('/'.join((dir_, f_name)))

    return [val for val in ans.values() if len(val) > 1]


test_data = [
    (["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"],
     [["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"], ["root/a/1.txt", "root/c/3.txt"]]),
    (["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"],
     [["root/a/2.txt", "root/c/d/4.txt"], ["root/a/1.txt", "root/c/3.txt"]])
]

f_l = [find_duplicate]


@pytest.mark.parametrize('paths, expected', test_data)
def test(paths: list, expected):
    for i, f in enumerate(f_l):
        ans = f(paths)
        print('\n', f.__name__, ans, expected)
        assert len(ans)==len(expected)



# def test_time(n_iter: int = 100):
#     from utils.print_time4random import print_time
#
#     print_time(f_l, args=None,
#                n_max=N_MAX, a_max=A_MAX,
#                n_min=N_MIX, a_min=A_MIN,
#                n_iter=n_iter)


"""
TIME:

"""


# -------------------------------


# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'String'
    file_name = 'find-duplicate-file-in-system-609.py'
    print('\n')
    print(get_readme(string_, topic, file_name))
