input1="abcabca"
index1=[0]*len(input1)

# for i in range(1,len(input1)):
#     print("i",i)
    #2일때

answer=0
i=3
quo=len(input1)//i
remainder=len(input1)//i
final=[1]*quo
for j in range(quo):
    if input1[j*i:((j+1)*3)-1]==input1[(j+1)*i:((j+2)*3)-1]: #input1[0:2] != input1[3:5]:   [6:8]
        final[j]=0
print(i*(i+1))
##1로 된것을 더해야 함
print(final)



        #0:2    3:5


