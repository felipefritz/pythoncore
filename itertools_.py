
from itertools import product, permutations, combinations \
    , combinations_with_replacement, accumulate, groupby
# product it will combine as a cartesial

a = [1, 2, 3]
b = [3, 4]

prod = product(a, b)
print(list(prod))

# permutations:
# return all possible ordering combinations of inputs
# as second argument is the length of combinations
perm = permutations(a, 2)
print(list(perm))

# combinations: return an iterable of all the combinations possibles of an input
# combinations_with_replacement : it will combine with repetitions of items
comb = combinations(a, 2)
comb_wr = combinations_with_replacement(a, 2)
print('comb')
print(list(comb))
print(list(comb_wr))

# accumulate: makes an iterator that return the sum of the last number with the current number
acc = accumulate(a)
print(list(acc))

# groupby  makes an iteratorthat return keys and groups
l = [1, 2, 3, 4]
def smaller_than_3(z):
    return z < 3

grouped = groupby(a, key=smaller_than_3)