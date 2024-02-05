def dfs(vert,start):
    visited[vert]=True
    value=field[vert]
    if not visited[value]:dfs(value,start)
    elif visited[value] and value==start:result.append(value)

n=int(input())
field=[0]
result=[]
for i in range(n):field.append(int(input()))

for i in range(1,n+1):
    visited=[False]*(n+1)
    dfs(i,i)

result.sort()
print(len(result))
for ele in result:print(ele)