t=  int(input())
while t:
    t-=1
    n,p = map(int,input().split())
    ans = 0
    for i in range(p,n+1,p):
        while i % p ==0:
            i//=p
            ans+=1
    print(ans)