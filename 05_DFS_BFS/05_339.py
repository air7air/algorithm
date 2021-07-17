from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
# n, m, k, x = map(int, input().split())
n,m,k,x=4,4,2,1

# graph = [[] for _ in range(n+1)]
# print(graph)
#
# for _ in range(m):
#     a,b = map(int, input().split())
#     graph[a].append(b)

graph=[[], [2, 3], [3, 4], [], []]

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q=deque([x])

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node]==-1:
            distance[next_node]=distance[now]+1
            q.append(next_node)

print(distance)

check=False
for i in range(len(distance)):
    if distance[i]==k:
        print(i)
        check=True

if check ==False:
    print("-1")