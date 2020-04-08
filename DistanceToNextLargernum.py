'''
输入整数序列，最大100，输出当前元素到之后第一个比他大的元素的距离，
没有更大的话输出-1，比如输入1，20，10，40输出1，2，1，-1，时间复杂度不大于O（n）
'''

a = [1,20,10,40,10, 10, 30]
n = len(a)
b = [-1]* n
top = 1
s = [0] * (n+1)
index_list = [0] * (n+1)
s[top] = a[n-1]
index_list[top] = n-1
for i in range(n-2,-1,-1):
    if a[i]<s[top]:
        b[i] = index_list[top] - i
        top +=1
        s[top] = a[i]
        index_list[top] = i
    else:
        while(a[i]>=s[top] and top!=0):
            top-=1
        if top==0:
            top+=1
            s[top] = a[i]
            index_list[top] = i
        else:
            b[i] = index_list[top] - i
            top+=1
            s[top] = a[i]
            index_list[top] = i
print(b)