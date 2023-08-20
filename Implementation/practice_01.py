dic = {8: 'D', 10: 'D', 11: 'D', 13: 'L'}

import itertools

a= [[1, 2], [3, 4], [5, 6]]

nCr = itertools.combinations(a, 2)
print(len(list(nCr)))