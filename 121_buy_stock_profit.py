#finding the profit for buying the low price and selling for more profit
p=[13,14,2,5,8,1,4]
mp=0
bp=p[0]
for i in range(1,len(p)):
    if p[i]>bp:
        pro=p[i]-bp
        if pro>mp:
            mp=pro
    else:
        bp=p[i]
print(mp)

#################################################################################################################3
a=[13,14,2,5,8,1,4]
m=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[j]-a[i]>m:
            m=a[j]-a[i]
print(m)
########################################################################################################################
prices=list(map(int,input().split()))
max_p=0
buy_price=prices[0]
for i in range(1,len(prices)):
    if prices[i]>buy_price:
        max_p=max(max_p,prices[i]-buy_price)
    else:
        buy_price=prices[i]
print(max_p)
#####################################################################################################################
a=[13,14,2,5,8,1,4]
mp=0
b=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[j]-a[i]>mp:
            b.append(a[j]-a[i])
print(max(b))