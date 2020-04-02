def merge_result(start, end, mid, a):
    i = start
    j = mid+1
    tmp_list = []
    while(i<=mid and j<=end):
        if a[i]<a[j]:
            tmp_list.append(a[i])
            i+=1
        else:
            tmp_list.append(a[j])
            j+=1
    while(i<=mid):
        tmp_list.append(a[i])
        i+=1
    while(j<=end):
        tmp_list.append(a[j])
        j += 1
    for i in range(len(tmp_list)):
        a[start+i] = tmp_list[i]

def divide_and_conquer(start, end, a):
    mid = (start + end)//2
    if start<end:
        divide_and_conquer(start, mid, a)
        divide_and_conquer(mid+1, end, a)
        merge_result(start,end, mid, a)

def quicksort(low, high, a):
    if low < high:
        left = low
        right = high
        tmp_value = a[low]
        while(left<right):
            while(a[right]>=tmp_value and right>left):
                right-=1
            if right>left:
                a[left] = a[right]
            while(a[left]<=tmp_value and right>left):
                left+=1
            if right>left:
                a[right] = a[left]
        a[left] = tmp_value
        quicksort(low, left-1, a)
        quicksort(left+1, high, a)

init_list = [3,45,6,3,8,5,47,43,56,9,6]
a = 0
b = len(init_list)-1
# divide_and_conquer(a, b, init_list)
quicksort(a,b,init_list)
print(init_list)
