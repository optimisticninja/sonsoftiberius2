#!/bin/sh

BASE_WORDLIST="base_wordlist.txt"
WORDLIST="wordlist.txt"

sort -u "$BASE_WORDLIST" > wordlist_no_dupes.txt
mv wordlist_no_dupes.txt "$BASE_WORDLIST"
python3 create_new_wordlist.py > "$WORDLIST"
cat "$BASE_WORDLIST" "$WORDLIST" > wordlist_no_dupes.txt
mv wordlist_no_dupes.txt "$WORDLIST"
hashcat -m 12500 -o cracked.txt trailing_data.hashcat wordlist.txt
