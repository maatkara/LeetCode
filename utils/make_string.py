string = """
48. Rotate Image
https://leetcode.com/problems/rotate-image/
Medium

fskjgkfj;gj;h s
gfkjhd;lkjh;d
"""
topic = 'Array'
file_name = 'rotate_image_48.py'


def get_readme(string, topic, file_name):
    github_link = "[Python](https://github.com/maatkara/LeetCode/blob/main/"

    str_l = string.split('\n')[1:4]
    github_link += f'{str_l[-1].lower()}/{file_name})'
    si, s_name = str_l[0].split('.')
    readme_str = '|' + ' | '.join([si.strip(), f'[{s_name.strip()}]({str_l[1]})', topic, github_link, str_l[-1]]) + '|'

    return readme_str
