#reverse the string without split()
a=int(input())
s=list(a)
l=0
r=len(s)-1
while l<r:
    s[l],s[r]=s[r],s[l]
    l+=1
    r-=1
print("".join(s))