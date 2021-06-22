def getans(n):
    cnt=0
    if n==1:
        return cnt
    lv=1
    while lv<=n:
        inner_lv=1
        while inner_lv<=n:
            cnt+=1
            continue
        inner_lv+=1

for i in range(1,100):
    print(i,getans(i))