n=5
k=3

input1=[1,2,5,4,3]
input2=[5,5,6,6,5]

input1.sort()
input2.sort(reverse=True)

answer1=input1[k:]+input2[:k]

print(sum(answer1))

