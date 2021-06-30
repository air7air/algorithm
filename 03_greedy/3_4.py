input1, input2 = map(int, input().split())

result=0
answer=0

while input1!= 1:
    if input1%input2==0:
        input1=input1/input2
        answer+=1
    else:
        input1=input1-1
        answer+=1

print(answer)