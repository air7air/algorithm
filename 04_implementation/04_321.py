input1='123402'
helf=len(input1)/2
front, beck = 0, 0

for i in range(len(input1)):
    if i < helf:
        front+=int(input1[i])
    else:
        beck+=int(input1[i])

if front == beck:
    print("LUCKY")
else:
    print("READY")