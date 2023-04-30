file = open("C:/Users/ASUS/Desktop/.txt", "w")
# for i in range(1,100):
#     file.write(str(i)+'\n')


for i in range(0,26):
    file.write(chr(ord('a')+i)+"\n")
    file.write(chr(ord('A')+i)+"\n")
for i in range(0,10):
    file.write(str(i)+"\n")
    