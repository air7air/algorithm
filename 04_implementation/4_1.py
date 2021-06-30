# input1=5
# input2=['R','R','R','U','D','D']

input1=int(input())
input2=input().split()

left, right = 1 , 1

for i in input2:
    if i == 'L':
        right -= 1
        if right < 1:
            right +=1
    elif i == 'R':
        right += 1
        if input1 > 5:
            right -=1
    elif i == 'U':
        left -= 1
        if left < 1:
            left +=1
    else:
        left += 1
        if input1 > 5:
            left -=1

print(left,right)
