mx = -10**20
for i in range(-250, 250):
    n1 = bin(abs(i))[2:]
    if i % 2 == 0:
        n1 = '10' + n1[2:] + '1'
    else:
        n1 = '11' + n1[2:] + '0'
    s1 = int(n1, 2)
    for j in range(i+1, 251):
        n2 = bin(abs(j))[2:]
        if j % 2 == 0:
            n2 = '10' + n2[2:] + '1'
        else:
            n2 = '11' + n2[2:] + '0'
        s2 = int(n2, 2)
        if mx <= s1+s2:
            mx = s1+s2
            print(s1+s2, i, j)
