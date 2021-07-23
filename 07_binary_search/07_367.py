def count_by_value(array, x):
    # 데이터의 갯수
    n = len(array)
    # X가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n - 1)
    print("array, x, 0, n - 1:일번;",array, x, 0, n - 1)
    # 수열에 x가 존재하지 않는 경우
    if a is None:
        return 0  # x 0개 0

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n - 1)

    # 개수를 반환
    return b - a + 1


# 처음 위치를 찾는 이진 탐색 메서드
# 작거나 같으면 왼쪽
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지고 있는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    # 맨 왼쪽이거나, mid 전 인덱스 원소가 target보다 작다 (커져서 target).
    print("mid:",mid)
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        print("답:",mid)
        print("답:22",target , array[mid - 1])
        return mid
    # 중간점의 값 보다 찾는 값이 작거나 같으면 왼쪽을 찾는다.
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    # 중간점의 값 보다 찾는 값이 크면 오른쪽을 찾는다.
    else:
        return first(array, target, mid + 1, end)


# 마지막 위치를 찾는 이진 탐색 메서드
# 크거나 같으면 오른쪽
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지고 있는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    # 맨 왼쪽이거나, mid 다음 인덱스 원소가 target보다 크다 (오름차순).
    if (mid == len(array) - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾는 값이 작은경우 왼쪽 확인
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    # 중간점의 값 보다 찾는 값이 크거나 같으면 오른쪽을 찾는다.
    else:
        return last(array, target, mid + 1, end)


# n, x = map(int, input().split())  # 데이터의 개수 N, 찾고자 하는 값 x 입력 받기
n, x = 7, 1
# array = list(map(int, input().split()))  # 전체 데이터 입력 받기
array=[1, 1, 1,1,1,1,8]
# 값이 x인 데이터의 개수 계산
count = count_by_value(array, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)