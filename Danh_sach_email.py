
with open("CONTACT.in") as f:
    x = set(f.read().lower().split())
x = list(x)
x.sort()
print(*x,sep="\n")