# left=0
#
# for i in range(3):
#     for j in range(2):
#         if j == 0 or j == 1:
#             left+=1
#     if left>2:
#         continue
#     last=left
# print(last)

for i in range(10):       # 0부터 99까지 증가하면서 100번 반복
    if i % 2 == 0:         # i를 2로 나누었을 때 나머지가 0면 짝수
        continue           # 아래 코드를 실행하지 않고 건너뜀
    print(i)