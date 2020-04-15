#-*-coding:utf-8-*-
'''
给定一个数组序列,需要求选出一个区间,使得该区间是所有区间中经过如下计算的值最大的一个：   区间中的最小数*区间所有数的和   最后程序输出经过计算后的最大值即可，不需要输出具体的区间。
如给定序列 [6 2 1]则根据上述公式,可得到所有可以选定各个区间的计算值:   
[6] = 6 * 6 = 36;   [2] = 2 * 2 = 4;   [1] = 1 * 1 = 1;   [6,2] = 2 * 8 = 16;   
[2,1] = 1 * 3 = 3;   [6, 2, 1] = 1 * 9 = 9;   
从上述计算可见选定区间[6]，计算值为36， 则程序输出为36。   区间内的所有数字都在[0, 100]的范围内; 
'''
# stack序号栈始终存储位置上的值比当前值小的坐标序号，pre_num保存各位置上对应的序列和
# 当stack不为空时，pre_num[i] - pre_num[stack[-1]+1])为以right位置值为最小值，对应区间的全部值之和。
# 即每次遇到当前值大于stack栈顶位置对应的位置上的值heights[right]时，以栈顶元素为区间内最小值获得指定区间的计算结果，
# 并与之前的结果进行比较

n=int(input())
heights = [int(x) for x in input().split(" ")]
if n == 0:
    print(0)
heights.append(0) #单调栈做
stack, maxarea, pre_num = [], 0, [0]
for i in range(len(heights)):
    while stack and heights[i] < heights[stack[-1]]:
        right = stack.pop()
        maxarea = max(maxarea, heights[right] * (pre_num[i] if not stack else (pre_num[i] - pre_num[stack[-1]+1])))
    pre_num.append(heights[i] + pre_num[-1])
    stack.append(i)
print(maxarea)
