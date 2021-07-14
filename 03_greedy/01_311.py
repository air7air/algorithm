#01_311
input1=[2,3,1,2,2]
length=len(input1)
zero=[0]*length
input1.sort(reverse=True)
zero[0]=input1[0]
for i in range(1,length):
    if zero[i-1] > 1: #3->2->1
        zero[i]=zero[i-1]-1
        zero[i-1]=0
    else: # return oneself
        zero[i]=input1[i]
print(sum(zero))