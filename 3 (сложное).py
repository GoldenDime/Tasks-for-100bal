def f(n):
    if n == 0:
        return '0'
    s = ''
    while n > 0:
        s = str(n%3) + s
        n//=3
    return s
ans = set()
for i in range(-250, 250):
    n1 = f(abs(i))
    if i % 2 == 0:
        n1 = n1[2:] + n1[:2]
    else:
        n1 = n1[-2:] + n1[:-2]
    s1 = int(n1, 3)
    for j in range(i+1, 251):
        n2 = f(abs(j))
        if j % 2 == 0:
            n2 = n2[2:] + n2[:2]
        else:
            n2 = n2[-2:] + n2[:-2]
        s2 = int(n2, 3)
        ans.add(s1+s2)
print(len(ans))
