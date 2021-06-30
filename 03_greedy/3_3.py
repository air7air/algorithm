# n=2
# k=4
# answer=[]
# first=[7,3,1,8]
# second=[3,3,3,4]
#
# first.sort()
# second.sort()
# answer.append(first[0])
# answer.append(second[0])
#
# answer.sort()
# print(answer[-1])

a,b = map(int,input().split())
answer=[]
for i in range(a):
    c=input().split()
    c.sort()
    answer.append(c[0])

answer.sort()
print(answer[-1])