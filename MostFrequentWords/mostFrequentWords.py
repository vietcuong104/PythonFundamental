words = []
with open("demo.txt", "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter

count = Counter(words)
top = count.most_common(5)
print(top)
