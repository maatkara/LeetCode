import random

import pytest

string_ = """
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1
Medium

Implement the RandomizedSet class:

RandomizedSet() 
Initializes the RandomizedSet object.
bool insert(int val) 
        Inserts an item val into the set if not present.
        Returns true if the item was not present, false otherwise.
bool remove(int val) 
        Removes an item val from the set if present. 
        Returns true if the item was present, false otherwise.
int getRandom() 
        Returns a random element from the current set of elements 
        (it's guaranteed that at least one element exists when this method is called). 
        Each element must have the same probability of being returned.
        
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:
-----------------
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:
-----------------
-2^31 <= val <= 2^31 - 1
At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.

04.08.23
"""
N_MIN = 1
N_MAX = int(2e5)
A_MAX = int(2**31) - 1
A_MIN = -A_MAX - 1


class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False

        self.hash_map[val] = len(self.hash_map)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False

        # in data list: ind val <-> last ind  -> pop
        remove_ind = self.hash_map[val]

        self.hash_map[self.data[-1]] = remove_ind
        self.data[remove_ind], self.data[-1] = self.data[-1], self.data[remove_ind]

        self.data.pop()
        self.hash_map.pop(val)
        return True

    def getRandom(self) -> int:
        if not self.data: return 0  # Only for test
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


def random_set_dispatcher(commands: list[str], vals: list[list[int]]) -> list[bool, int, None]:

    ans = [None]
    obj = RandomizedSet()

    for com, val in zip(commands[1:], vals[1:]):
        if com == 'insert':
            ans.append(obj.insert(val[0]))
        elif com == 'remove':
            ans.append(obj.remove(val[0]))
        else:
            ans.append(obj.getRandom())
    return ans


test_data = [
    (["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
     [[], [1], [2], [2], [], [1], [2], []], [None, True, False, True, 2, True, False, 2])

]

f_l = [random_set_dispatcher]  #


@pytest.mark.parametrize('commands, vals, expected', test_data)
def test(commands: list[str], vals: list[list[int]], expected: list[bool, int, None]):
    for f in f_l:
        ans = f(commands, vals)
        print('\n', f.__name__, ans)

        assert ans == expected


def test_time(n_iter: int = 100):
    from utils.print_time4random import print_time
    import numpy as np

    def get_args(i: int) -> tuple:
        n: int = N_MAX if i == n_iter - 1 else random.randint(N_MIN, N_MAX)
        coms: list = [] + random.choices(["insert", "remove", "getRandom"], k=n)
        vals: list = np.random.randint(A_MIN, A_MAX + 1, size=n).tolist()
        coms = ["RandomizedSet"] + coms
        vals = [[]] + [[val] for val in vals]

        return coms, vals

    print_time(f_l, get_args, n_iter)


"""
                         min      mean     max
==================================================
random_set_dispatcher  2.6e-04  4.7e-02  1.1e-01
==================================================
"""


# -------------------------------

# TO README
def test_readme():
    from utils.make_string import get_readme

    topic = 'Array'
    file_name = 'insert-delete-getrandom-o1-380.py'

    print('\n')
    print(get_readme(string_, topic, file_name))
