n = int(input())
a = list()
stack=list()
ans=0
for i in range(n):
    c = int(input())
    a.append(c)
    if len(stack) == 0:
        stack.append(i)
    else:
        if a[stack[-1]] >a[i]:
            stack.append(i)
        elif a[stack[-1]]==a[i]:
            ans+=1
            stack.append(i)
        else: 
            while len(stack)>0 and a[stack[-1]]<a[i]:
                ans+=1
                stack.pop()
            stack.append(i)
    print(ans,i,a[i],stack,sep="/")
print(ans+n-1)
