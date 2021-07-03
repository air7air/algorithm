input1=[['홍길동','95'],['이순신','77']]
print(len(input1))

input2=[]
for i in range(len(input1)):
    input2.append(int(input1[i][1]))

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left = [i for i in tail if i <= pivot]
    right = [i for i in tail if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(input2))

input3=quick_sort(input2)

input4=[]
for i in input3:
    for j in range(len(input1)):
        if i == int(input1[j][1]):
            input4.append(input1[j][0])

print(input4)