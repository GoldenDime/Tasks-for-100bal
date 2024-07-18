def f(n):
    s=''
    while n > 0:
        s = str(n%3) + s
        n//=3
    return s
for i in range(-250, 251):
    n = abs(i)
    a = f(n)
    if n % 2 == 0:
        a = '12' + a[2:] + '1'
    else:
        a = '21' + a[2:] + '0'
    r = int(a, 3)
    if r < 1000:
        print(i)
