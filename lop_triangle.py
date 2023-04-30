import math
class Point:
    def __init__(self,x,y): 
        self.x = x
        self.y = y
    
    def kc(self,a):
        ds = math.sqrt((a.x - self.x)**2 + (a.y - self.y)**2)
        return float(ds)
t = int(input())
a = []
for _ in range(t):
    a = a + [float(j) for j in input().split()]

for i in range(0,t*6,6):
    p1 = Point(a[i],a[i+1])
    p2 = Point(a[i+2],a[i+3])
    p3 = Point(a[i+4],a[i+5])
    
    kc1 = p1.kc(p2)
    kc2 = p1.kc(p3)
    kc3 = p2.kc(p3)

    if kc1+kc2 <= kc3 or kc1 + kc3 <= kc2 or kc2 + kc3 <= kc1:
        print("INVALID")
    else:
        print('{:.3f}'.format(kc1+kc2+kc3))