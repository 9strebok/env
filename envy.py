#!/usr/bin/python3
"""Print environment variables"""

import os
from colorama import Fore, Style


def get_longest_element_length(l: list):
    """
    get_longest_element_length (l: list[string]) -> int
    Return the length of the longest element in the list
    """
    return max(len(el) for el in l)


def nice_dict_print(d: dict, str_length: int = 80):
    """
    nice_dict_print(d: dict) -> None
    Nice print a dictionary
    """
    k = d.keys()
    max_lenght = get_longest_element_length(k)
    for _ in k:
        dif = max_lenght - len(_)
        value_len = len(d[_])
        if value_len <= str_length:
            spaces = " " * dif
            print(f"{Fore.CYAN}{spaces}{_}{Style.RESET_ALL}", d[_])
        else:
            spaces = " " * dif
            new_str = f"{(max_lenght + 1) * ' '}"
            print(f"{Fore.CYAN}{spaces}{_}{Style.RESET_ALL}")
            for index, some in enumerate(d[_]):
                if index % (str_length - 1) == 0 and index != 0:
                    new_str +=  "\n" + (max_lenght + 1) * " " + some
                else:
                    new_str += some
            print(new_str)


def main():

    """Main function"""
    env = os.environ
    nice_dict_print(env)


if __name__ == "__main__":
    main()

