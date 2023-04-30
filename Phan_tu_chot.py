from queue import LifoQueue
t = int(input())
while t:
    t-=1
    n = int(input())
    a = list(map(int,input().split()))
    b = [True] * n
    list_dc = list()
    for i in range(n):
        list_del = list()
        for j in range(len(list_dc)):
            if a[i] == a[list_dc[j]]:
                list_del.append(j)
                b[j] = False
            elif a[i] < a[list_dc[j]]: 
                b[i] = False
                b[j] = False
                list_del.append(j)
            else: break
        list_del.reverse()
        for j in list_del:
            list_dc.pop(j)
        if b[i] == True:
            list_dc.insert(0,i)
        # print(*b)
    print(len(list_dc))
# 3
# 3
# 1 1 1
# 4
# 1 2 3 3
# 8
# 2 1 3 4 5 3 6 7