input1='0001100'
index1=[0]*len(input1)
index0=[0]*len(input1)

answer=0
for i in range(len(input1)):
    if (input1[i-1] == '1' and input1[i]=='0') or (i==0 and input1[i]=='0'): #change 0 -> 1
        index1[i]=1
    elif (input1[i-1] == '0' and input1[i]=='1') or (i==1 and input1[i]=='1'): #change 1-> 0
        index0[i]=1

if sum(index1) < sum(index0):
    answer=sum(index1)
else:
    answer=sum(index0)
print(answer)