a = "aieef"
b = "klaief"
def counting(a1):
    d="aeiou"
    str1=""
    l=0
    while l<len(a1):
        if a1[l] in d:
            str1+=a1[l]
        l+=1
    return str1           
s=counting(a)
m=counting(b)
if s in m:
    print(len(s))
else:
    print(len(m))
            