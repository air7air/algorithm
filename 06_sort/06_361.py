input1=[2,1,2,6,2,4,3,3]
n=5
stage=[0 for _ in range(n+2)] #처음 0단계, 마지막 단계 더해주기

#stage 만들기
for i in range(len(input1)):
    stage[input1[i]]=stage[input1[i]]+1
print("stage:",stage)
sum1=sum(stage)

#실패율
answer=[]
for i in range(1,n+1):
    print("분자",stage[i],"분모",sum1-(sum(stage[1:i])))
    answer.append([i,stage[i]/(sum1-(sum(stage[1:i])))])
print(answer)

# 정렬
answer.sort(reverse=True, key=lambda x:x[1])
for i in range(n):
    print(answer[i][0]," ",end="")
