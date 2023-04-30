class hd:
    def __init__(self,ma,ten,sl,dg,ck) -> None:
        self.ma = ma 
        self.ten = ten
        self.sl = sl
        self.dg = dg 
        self.ck = ck
        self.tt = sl * dg - ck
    def __str__(self) -> str:
        return self.ma +" "+ self.ten + " "+str(self.sl)+" "+str(self.dg)+" "+str(self.ck) + " "+str(self.tt)

list_mh = list()
t = int(input())
for i in range(t):
    x = hd(input(), input(),int(input()),int(input()),int(input()))
    list_mh.append(x)
list_mh.sort(key= lambda x : x.tt,reverse=True)
for i in list_mh:
    print(i)
