def thn(n,a,b,c):
    if n==1:
        print(a+' -> ' + c)
    else:
        thn(n-1, a, c, b)
        thn(1, a, b, c)
        thn(n-1, b, a, c)
n = int(input())
thn(n, 'A', 'B', 'C')