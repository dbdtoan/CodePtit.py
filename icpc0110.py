import itertools
def find(a,i):
    dem =0
    for i in a[:i]:
        for j in a[i+1:]:
            if i + j == a[i]:
                dem += 1
    return dem
t = int(input())
while t:
    t -= 1
    n = int(input())
    a = [int(x) for x in input().split()]
    l = list(itertools.combinations(a, 3))
    m = -3*10**8
    for x in l:
        m = max(m,sum(x))
    print(m)