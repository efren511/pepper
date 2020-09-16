#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from termcolor import *

banner = """ _____________________
|  _________________  |
| | LA CHOFIS 7u7 . | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|"""

def main():
    print(colored(banner, "blue"))
    cc1 = input(colored("\nIngresa una CC: ", "yellow"))
    cc2 = input(colored("\nIngresa otra CC: ", "yellow"))
    tres1 = cc1[9:11]
    tres2 = cc2[9:11]
    t1 = 0
    t2 = 0
    for n in tres1:
        t1 = t1 + int(n)
    for n in tres2:
        t2 = t2 + int(n)
    t1 = t1 / 2
    t2 = t2 / 2
    t1 = t1 * 5.
    t2 = t2 * 5.
    t1 = int(t1)
    t2 = int(t2)
    r = t1 + t2
    b = cc1[0:8]
    print(colored("\n---------------------------", "green"))
    print(colored("Tu BIN es:", "green"), colored(b + "{}{}".format(r,"xxxxxx")))
    print(colored("---------------------------", "green"))

if __name__ == '__main__':
    main()
