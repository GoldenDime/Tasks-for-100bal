def f(n):
    s = ''
    while n > 0:
        s = str(n%3) + s
        n//=3
    return s
for i in range(-250, 250):
    n1 = f(i)
    if i % 2 == 0:
        n1 = '12' + n1[2:] + '1'
    else:
        n1 = '21' + n1[2:] + '0'
    s1 = int(n1, 3)
    for j in range(i+1, 251):
        n2 = f(j)
        if j % 2 == 0:
            n2 = '12' + n2[2:] + '1'
        else:
            n2 = '21' + n2[2:] + '0'
        s2 = int(n2, 3)
        if s1+s2 == 666 and abs(i - j) >= 450:
            print(s1+s2, i, j)
            exit()
