from itertools import combinations

n, m = 5, 2
# location=[[1,2,0,0,0,],
#           [1,2,0,0,0],
#           [1,2,0,0,0],
#           [1,2,0,0,0],
#           [1,2,0,0,0]]

# n, m = map(int, input().split())
chicken, house = [], []

# for r in range(n):
#     data = list(map(int, input().split()))
#     for c in range(n):
#         if data[c] == 1:
#             house.append((r, c)) # 일반 집
#         elif data[c] == 2:
#             chicken.append((r, c)) # 치킨집

house = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
chicken=[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]

# 모든 치킨 집 중에서 m개의 치킨 집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))
print("캔디",candidates)

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨 집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            print("cx:",cx)
            print("cy:",cy)
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨 집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    print("candidatae:",type(candidate))
    result = min(result, get_sum(candidate))

print(result)