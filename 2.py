n,m = map(int,input().split())
li = list()
for i in range(n):
    li.append(list(map(int,input().split())))
li =  sorted(li,key= lambda x:(x[1]/x[0]),reverse = True)
s = 0
for i in li:
    if m >= i[0]:
        m-=i[0]
        s+=i[1]
print(s)
