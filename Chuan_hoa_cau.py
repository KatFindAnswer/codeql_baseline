import re
while True:
    try:
        s=input()
        s=re.sub('\s+',' ',s)
        if s[len(s)-1]!='.' and s[len(s)-1]!='?' and s[len(s)-1]!='!': 
            s+='.'
        s=s.strip()
        ss=''
        for i in s.split():
            if i!='.' and i!='?' and i!='!':
                ss+=" "+i
            else:
                ss+=i
            if ss[len(ss)-1]=='.' or ss[len(ss)-1]=='?' or ss[len(ss)-1]=='!':
                ss=ss.strip().capitalize()
                print(ss)
                ss=''
    except : 
        break