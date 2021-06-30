# input1 =500
#
# quotient1 = input1//500
# remainder1 = input1%500
# print(quotient1, remainder1)
#
# quotient2 = remainder1//100
# remainder2 = remainder1%100
# print(quotient2, remainder2)
#
# quotient3 = remainder2//50
# remainder3 = remainder2%50
# print(quotient3, remainder3)
#
# quotient4 = remainder3//10
# print(quotient4)
#
# print("last:", quotient1+quotient2+quotient3+quotient4)


c_type=[500,100,50,10]
input1=550
quo1=0
for i in c_type:
    quo1 += input1//i
    input1 = input1%i
print(quo1)

