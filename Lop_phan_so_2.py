from math import gcd
class Ps:
    def __init__(self,x,y):
        self.x = x//gcd(x,y)
        self.y = y//gcd(x,y)
    def __str__(self) -> str:
        return str(self.x)+"/"+(str(self.y))
    def add(self,a):
        msc = self.y*a.y// gcd(self.y,a.y)
        ts = self.x * msc // self.y + a.x * msc //a.y
        return Ps(ts,msc)
li = list(map(int,input().split()))
n = Ps(li[0],li[1])
m = Ps(li[2],li[3])
print(n.add(m))
