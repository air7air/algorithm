def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return "yes"
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid - 1
    return "no"

total_n=4
total=[6,7,10,2]
total.sort()
find=[4,10,2]

for i in find:
    result=binary_search(total, i, 0, total_n-1)
    print(result,' ', end='')
