#arrange the sentence according to the length of the word
s="an apple a day keeps doctor away".split()
d=[]
for i in s:
    d.append(len(i))
for j in range(len(s)-1):
    f=False
    for i in range(len(s)-1-j):
        if(d[i]>d[i+1]):
            d[i],d[i+1]=d[i+1],d[i]
            s[i],s[i+1]=s[i+1],s[i]
            f=True
    if not f:
        break
print(*s)