n=4
target=5
type=[19, 15, 10, 17]
type.sort(reverse=True)
answer = type[0] - 1 #biggest number-1
sum1 = 0
while target >= sum1:
    sum1=0
    for i in type:
        if i > answer:
            sum1=sum1+i-answer
    if target > sum1:
        answer=answer-1
print(answer)
