
a=[i for i in range(26)]

for _ in range(int(input())):
	s = input()
	n = len(s)//2
	x = s[:n]
	y = s[n:]
	s1 = 0
	for i in x:
		s1 = s1 + ord(i)-65
	x1 = ''
	for i in x:
		q = (a[ord(i)-65]+s1)%26 
		x1 = x1 + str(chr(a[q]+65))
	s2=0
	for i in y:
		s2 = s2 + ord(i)-65
	x2 = ''
	for i in y:
		q = (a[ord(i)-65]+s2)%26 
		x2 = x2 + str(chr(a[q]+65))
	ans = ''
	for i in range(len(x1)):
		q = (a[ord(x1[i])-65]+a[ord(x2[i])-65])%26
		ans = ans + str(chr(a[q]+65))
	print(ans)