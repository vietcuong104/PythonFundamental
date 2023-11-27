from collections import defaultdict


def group_anagrams(g):
    ddict = defaultdict(list)
    for i in g:
        sorted_i = "".join(sorted(i))
        # print(sorted(i))
        ddict[sorted_i].append(i)

    return ddict.values()


words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))
# rs = group_anagrams(words)
# for i in rs:
#     print(i)