# time1=0
# time2=0
# minute=[0,0]
# second=[0,0]
# # 두자리수
# # 3 or 13 or 23 or 31~39 -> 12개
#
# 초: 12
# 분: 12 * 60
# 시: 3의 배수가 아닐때 : 12 *60
#     3의 배수일때 3: 60*60
#                 13:60*60
#                 23:60*60
#
#
# 모든 경우의 수 : 24*60*60
# n=0일때 1*60*60
# n=1일때 2*60*60
# n=2일때 3*60*60
#
# a=62
# 시간: a//360
# 분: a//60
# 초: a%60

n=5
answer=0
361


for i in range((n+1)*60*60):
    if i>=360:
    number=str(i//360)+str(i%60)
    print(number)
    if '3' in number:
        answer += 1
print(answer)

