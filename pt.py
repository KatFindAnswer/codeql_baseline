import re
tmp = input()
sn = [str(i) for i in range(0,10)]
str = tmp[0]
x1 = list()
x2 = list()
for i in range(1,len(tmp)):
    if (tmp[i]=='-'and tmp[i-1] not in sn):
        str+=tmp[i]
    # k xét kí tự đầu tiên, từ kí tự thứ 2  nếu gặp - mà ngay trước là phép toán thì dấu - hiện tại là dấu của số âm
    else:
        if tmp[i] in sn:
            str+=tmp[i]            
        else:
            x1.append(int(str))
            str =''
            x2.append(tmp[i])
            # gặp dấu thì ném dấu vào stack dấu, x1 chứa các số được đổi sang dạng int
x1.append(int(str))
st1 = x1[0:2]
st2 = x2[0:1]
## xét từ số thứ 3, nếu gặp +- thì tính phép toán trước đó
## nếu gặp */ thì không được tính phép toán trước đó, nên chỉ đc đẩy vào stack thôi   ví dụ  10+9*8 
for i in range(2,len(x1)):
    tmp = st2.pop()
    a1 = st1.pop()
    a2 = st1.pop()
    if x2[i-1]=='+' or x2[i-1]=='-':
        if tmp == '*':
            st1.append(a1*a2)
        if tmp == '/':
            st1.append(a2/a1)
        if tmp == '+':
            st1.append(a2+a1)
        if tmp == '-':
            st1.append(a2-a1)
    else:
        if tmp == '*':
            st1.append(a1*a2)
        elif tmp == '/':
            st1.append(a2/a1)
        else:
            st1.append(a2)
            st1.append(a1)
            st2.append(tmp)
    st1.append(x1[i])
    st2.append(x2[i-1])
while len(st2)>0:
    tmp = st2.pop()
    a1 = st1.pop()
    a2 = st1.pop()
    if tmp == '*':
        st1.append(a1*a2)
    if tmp == '/':
            st1.append(a2/a1)
    if tmp == '+':
            st1.append(a2+a1)
    if tmp == '-':
        st1.append(a2-a1)
print(st1[0])