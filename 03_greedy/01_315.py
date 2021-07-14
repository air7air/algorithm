input1=[1,5,4,3,2,4,5,2]
answer=0
for i in range(len(input1)):
    for j in range(len(input1)):
        if i < j and input1[i] != input1[j]:
            answer+=1

print(answer)