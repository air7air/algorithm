input1='abcabcdede'
index1=[0]*len(input1)
input1=[i for i in input1]
how=len(input1)//2
final=len(input1)
for n in range(2,how):
    ii = []
    for i in range(0,len(input1)-len(input1)%n,n): #n개씩 나누기
        ii.append(input1[i:i+n])
    print(ii)
    array1=[0]*len(ii)#n개 0으로 된 배열 만들기
    for i in range(len(ii)-1):
        if ii[i]==ii[i+1]: #앞뒤 같으면1
            array1[i]=1
    answer=0
    for i in range(len(array1)):
        if array1[i] == 1 and array1[i+1]==0 : ## 1,0 ->sum
            answer+=1
    print("답:",answer+len(input1)%n+array1.count(0)*n) #1,0인것 카운트+나머지+0인거 카운트*n
    final=min(final,answer+len(input1)%n+array1.count(0)*n)
print(final)