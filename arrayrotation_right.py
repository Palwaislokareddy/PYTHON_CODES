#rotation of the array in right side with k positions
a=list(map(int,input("enter the list elements").split()))
d=int(input("enter the position"))
n=len(a)
d=d%n
a[:]=a[-d:]+a[:d]
print(a)
