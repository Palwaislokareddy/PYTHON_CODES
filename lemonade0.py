a=[5,5,5,20,10]
count5=0
count10=0
for i in a:
    if i==5:
        count5+=1
    elif i==10:
        if count5==0:
            print("false")
            break
        count5-=1
        count10+=1
    elif i==20:
        if count10>0 and count5>0:
            count10-=1
            count5-=1
        elif count5>=3:
            count5-=3
        else:
            print("false")
            break
else:
    print("true")