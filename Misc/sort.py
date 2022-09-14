import bisect

a = [[5,2], [2,3], [3,2], [4,1]]
print(sorted(a))
a.sort(key= lambda x:x[1])
print(a)

a = [10,9,8,2]
# a.sort()
print(bisect.bisect(a, 7))