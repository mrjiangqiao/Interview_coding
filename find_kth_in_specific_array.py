#-*-coding:utf-8-*-
# def find_count(m,n,mid):
#     count = 0
#     for i in range(1, n + 1):
#         if mid // i >= m:
#             count += m
#         else:
#             count += mid // i
#     return count
#
# n, m, k = map(int, input().split(" "))
# min = 1
# max = n * m
# while min <= max:
#     mid = (min + max) // 2
#     count = find_count(m, n, mid)
#     if count < k:
#         min = mid + 1
#     else:
#         max = mid - 1
# print(min)

#*********复杂度高的实现方法
n, m, k = 150,200,50
array_input = []
for i in range(1,n+1):
    for j in range(1,m+1):
        array_input.append(i*j)
array_input.sort()
print(array_input[k-1])