# n = int(input())
# students = [] # 학생 정보를 담을 리스트
#
# # 모든 학생 정보를 입력 받기
# for _ in range(n):
#     students.append(input().split())

students=[['a', '2', '3', '5'], ['b', '2', '3', '4'], ['c', '7', '3', '4']]
n=len(students)

'''
[ 정렬 기준 ]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# a=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])
# print(a(['a', '2', '3', '5'], ['b', '2', '3', '4'], ['c', '7', '3', '4']))
print(students)
# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])

#ex)
# data_list = ['but','i','wont','hesitate']
# data_list = list(set(data_list))  #중복 제거
# data_list.sort()
# print(data_list)
# data_list.sort(key=lambda x : len(x))
# print(data_list)
#
# students=[['a', '2', '3', '5'], ['b', '2', '3', '4'], ['c', '7', '3', '4']]
# n=len(students)