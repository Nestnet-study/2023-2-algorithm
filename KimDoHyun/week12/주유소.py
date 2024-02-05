n=int(input())
edge=list(map(int,input().split()))
vert=list(map(int,input().split()))
result=0
vert_min=min(vert)
skip_point=0
for i in range(n):
    recent_cost=vert[i]
    if skip_point>i:continue
    if vert_min==recent_cost:
        edge_sum=0
        for k in range(i,n-1):edge_sum+=edge[k]
        result+=edge_sum*vert_min
        break
    for j in range(i+1,n):
        if recent_cost>vert[j]:
            edge_sum=0
            for k in range(i,j):edge_sum+=edge[k]
            result+=edge_sum*recent_cost
            skip_point=j
            break

print(result)