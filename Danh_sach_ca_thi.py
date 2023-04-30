class ct:
    def __init__(self,mc,nt,gt,pt):
        self.mc = mc
        self.nt = nt
        self.gt = gt
        self.pt = pt
        self.ntss = nt[6:]+nt[3:5]+nt[:2]+gt+mc
    def __str__(self):
        return self.mc+" "+self.nt+" "+self.gt+" "+self.pt
with open("CATHI.in") as f:
    t = int(f.readline().strip())
    li = list()
    for i in range(1,t+1):
        li.append(ct(f"C{i:03}",f.readline().strip(),f.readline().strip(),f.readline().strip()))
li.sort(key= lambda x : x.ntss)
print(*li,sep="\n")