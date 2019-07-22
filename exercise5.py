#!/usr/bin/env python3
from collections import Counter


def main():
    val = input('> ')
    counter = Counter(val.split(' '))
    for item, count in sorted(counter.items(), key=lambda x: x[0]):
        print(f"{item}:{count}")


if __name__ == '__main__':
    main()
