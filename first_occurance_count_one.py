#Find the first character in the string s that does not repeat.
a=input()
s={}
for i in a:
    s[i]=s.get(i,0)+1
for i in s:
    if s[i]==1:
        print(i)

