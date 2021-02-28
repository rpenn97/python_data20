#Itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# from itertools import product
# a = [1, 2, 3]
# b = [4, 5, 6]
# prod = product(a,b, repeat=2)
# print(list(prod))
#
# from itertools import permutations
# a = [1, 2, 3]
# perm = permutations(a)
# print(list(perm))
#
# from itertools import combinations
# a = [1, 2, 3, 4]
# comb = combinations(a, 2)
# print(list(comb))

# from itertools import combinations_with_replacement
# a = [1, 2, 3, 4]
# combwr = combinations_with_replacement(a, 2)
# print(list(combwr))
#
# from itertools import accumulate
# a = [1, 2, 3, 4]
# acc = accumulate(a)
# print(a)
# print(list(acc))

from itertools import groupby
def smaller_than_three(x):
    return x < 3

a = [1, 2, 3, 4]

group_object = groupby(a, key=smaller_than_three)
for key, value in group_object:
    print(key, list(value))