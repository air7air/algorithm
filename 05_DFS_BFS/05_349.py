from collections import deque

n=[5,6]

#쁠,마,곱,나눗셈
a=0,0,1,0
num=['+','-','*','%']
dd=deque()
for i in range(len(a)):
    for j in range(a[i]):
        dd.append(num[i])
print(dd)

answer = [[] for i in range(len(n))]
answer[0]=[n[0]]
www=deque()
for i in range(0,len(n)-1): #n 순서대로
    for j in answer[i]: #결과 다시 넣은 값
        for k in dd: # 담긴 연산 수
            if k =='+':
                answer[i+1].append(j + n[i+1])
            elif k == '-':
                answer[i+1].append(j - n[i+1])
            elif k == '*':
                answer[i+1].append(j * n[i+1])
            elif k == '%':
                answer[i+1].append(j // n[i+1])
            print("answer:",answer)
        # answer.popleft()

print(min(answer[len(n)-1]),max(answer[len(n)-1]))
