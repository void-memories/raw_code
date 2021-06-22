def getans(n):
    cnt=0
    an_v=1
    lv=1
    while lv<=n:
        an_v+=1
        cnt+=1
    
    return cnt

for i in range(1,100):
    print(i,getans(i))