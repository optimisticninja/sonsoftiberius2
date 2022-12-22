#!/usr/bin/env python3

from unrar import rarfile

with open('base_wordlist.txt', 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    for word1 in content:
        for word2 in reversed(content):
            password = word1 + word2
            print(password)
