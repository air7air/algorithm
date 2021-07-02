### 4_3
# input1='a1'
input1=input()
# change number
alpha=['a','b','c','d','e','f','g','h']
x=alpha.index(input1[0])
y=int(input1[1])

# how to move
dx=[2,2,-1,1,-2,-2,1,-1]
dy=[1,-1,-2,-2,1,-1,2,2]
answer=0

# move location
for i in range(len(dx)):
    nx=x+dx[i]
    ny=y+dy[i]

    if nx < 1 or ny < 1 or nx > 8 or ny >8:
        continue
    answer+=1

print(answer)