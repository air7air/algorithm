#law of large numbers

# n=5
# m=8
# k=3
# input1=[2,4,5,4,6]
# large1=0
# large2=0
#
# for i in input1:
#     if i >= large1: #가장 큰수
#         large1=i
# if large1 in input1: #가장 큰 수 제거
#     input1.remove(large1)
# for i in input1: #두번째 큰수
#     if i >= large2:
#         large2=i
#
# answer=large1*k*(m//k)+large2*(m%k)
# print(answer)


#law of large numbers
n=5
m=8
k=3
input1=[2,4,5,4,6]
large1=0
large2=0

for i in input1:
    if i >= large1: #가장 큰수
        large1=i
if large1 in input1: #가장 큰 수 제거
    input1.remove(large1)
for i in input1: #두번째 큰수
    if i >= large2:
        large2=i

answer=large1*k*(m//k)+large2*(m%k)
print(answer)