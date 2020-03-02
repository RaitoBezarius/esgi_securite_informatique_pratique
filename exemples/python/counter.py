from collections import Counter

def count_freq_fr_words():
    c = Counter()
    with open('/usr/share/dict/words', 'r') as f:
        for word in f:
            for letter in word.strip():
                c[letter.lower()] += 1

    return c

