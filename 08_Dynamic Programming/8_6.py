# 정수 N을 입력 받기
# n = int(input())

# 모든 식량 정보 입력 받기
# array = list(map(int, input().split()))
array = [1 ,3,1,5]
n=len(array)
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1]) 
for i in range(2, n):
    print("i:",i)
    print('d[i-1], d[i-2], arrayi:',d[i-1], d[i-2], array[i])
    print("d1:",d)
    d[i] = max(d[i - 1], d[i - 2] + array[i])
    print("d2:", d)
# 계산된 결과 출력
print(d[n - 1])

