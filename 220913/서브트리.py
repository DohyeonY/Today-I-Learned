def inorder(T):
    global count
    if T==0:
        return
    count+=1
    inorder(c1[T])
    inorder(c2[T])

T=int(input())
for t in range(1,T+1):
    e,n=map(int,input().split())
    c1=[0](e+2)
    c2=[0](e+2)
    edges=list(map(int,input().split()))
    for i in range(0,len(edges),2):
        p=edges[i]
        c=edges[i+1]
        if c1[p]==0:
            c1[p]=c
        else:
            c2[p]=c

    count=0
    inorder(n)
    print(f'#{t} {count}')