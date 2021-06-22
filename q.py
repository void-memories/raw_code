for _ in range(int(input())):
    # n=int(input())
    d,k=map(int,input().split())
    # ar=list(map(int,input().split()))

    if 2*((k*(d//k)-1)**2)<=d*d:
        print('Utkarsh')
    else:
        print('Ashish')
    # print(2*((k*(d//k))**2),d*d)
        
    