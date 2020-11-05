#!/usr/bin/python3
"""Print environment variables"""

import os
from colorama import Fore, Style


def get_longest_element_length(l: list):
    """
    get_longest_element_length (l: list) -> int
    Return the length of the longest element in the list
    """
    res = 0
    for _ in l:
        t = len(_)
        if t > res:
            res = t
    return res


def nice_dict_print(d: dict):
    """
    nice_dict_print(d: dict) -> None

    Nice print a dictionary
    """
    k = d.keys()
    max_lenght = get_longest_element_length(k)
    for _ in k:
        dif = max_lenght - len(_)
        if dif >= 0:
            spaces = " " * dif
            print(f"{Fore.CYAN}{spaces}{_}{Style.RESET_ALL}", d[_])



def main():
    """Main function"""
    env = os.environ
    nice_dict_print(env)


if __name__ == "__main__":
    main()

