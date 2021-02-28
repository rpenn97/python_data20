# Lambda arguments: expression
# add10 = lambda x: x + 10
# print(add10(5))
#
# y=5
# def add10_func(y):
#     return y + 10
#
# mult = lambda j,k: j*k
# print(mult(2,7))

# points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
#
# points2D_xsort = sorted(points2D)
# points2D_ysort = sorted(points2D, key=lambda x: x[1])
# points2D_sumsort = sorted(points2D, key=lambda x: x[0] + x[1])
#
# print(points2D)
# print(points2D_xsort)
# print(points2D_ysort)
# print(points2D_sumsort)

#map function
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))

c = [x*2 for x in a]
print(c)

#PAUSED at 2:04:04
