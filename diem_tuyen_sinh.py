class ThiSinh:
    def __init__(self,n,ten,diem,dt,kv) -> None:
        self.ma = 'TS{:02d}'.format(n)
        self.ten = ten 
        self.diem = diem
        self.dt = dt
        self.kv = kv
    def xuly(self,ten):
        a = [i for i in ten.split()]
        tmp = ''
        for i in a:
            tmp += i.title() + " "
        return tmp
    def uutien(self):
        if self.kv == '1':
            return  1.5
        if self.kv == '2':
            return  1
        if self.kv == '3':
            return 0
    def uutien1(self):
        if self.dt == 'Kinh':
            return 0
        return 1.5
    def tong(self):
        return self.diem + self.uutien() + self.uutien1()
    def tt(self):
        if self.tong() >= 20.5:
            return "Do"
        return "Truot"
    def __str__(self) -> str:
        return self.ma + " " + self.xuly(self.ten) + '{:.1f}'.format(self.tong()) + " " + self.tt()

t = int(input())
i = 1
a= []
while t > 0:
    t -= 1
    ts = ThiSinh(i,input(),float(input()),input(),input())
    a.append(ts)
    i+= 1
a.sort(key= lambda x: -x.tong())
for i in a:
    print(i)

