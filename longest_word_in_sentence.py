#Longest word in a sentence
s=input()
words=s.strip().split()
maxi=0
for i in words:
    if len(i)>maxi:
        a=i
        maxi=len(i)
print(i)