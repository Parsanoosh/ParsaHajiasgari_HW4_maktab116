def last(n):
    return n[-1]

def sort(tuples):
    return sorted(tuples, key=last)

sample_list = [(1, 3), (3, 2), (2, 1)]
sorted_list = sort(sample_list)
print(sorted_list)
sample_list.sort(key=lambda x: x[-1])
print(sample_list)
