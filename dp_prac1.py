'''
拿出装有货物的保温箱，需在最短的时间内用最少的保温箱将货物装好。 
  
我们把问题简单描述一下: 
1 每个货物占用空间都一模一样 
2 保温箱的最大容量是不一样的,每个保温箱由两个值描述: 保温箱的最大容量 bi ,当前已有货物个数 ai ,(ai<=bi) 
3 货物转移的时候,不必一次性全部转移,每转移一件货物需要花费 1秒 的时间
'''
# n = int(input().strip())
# food = list(map(int, input().strip().split()))
# capacity = list(map(int, input().strip().split()))

food = [5, 2, 3]
capacity = [6, 3, 4]
n = len(food)

max_food = sum(food)
max_capacity = sum(capacity)
dp = [[len(food), 0] for _ in range(max_capacity+1)]
dp[0] = [0, 0]

for k in range(1, n+1):
    for i in range(max_capacity, 0, -1):
        count = dp[max(i - capacity[k-1], 0)][0]
        weight = dp[max(i - capacity[k-1], 0)][1]
        if dp[i][0] < count+1:
            continue
        elif dp[i][0] > count+1:
            dp[i][0] = count + 1
            dp[i][1] = weight + food[k-1]
        else:
            dp[i][1] = max(weight + food[k - 1], dp[i][1])

min_step = 0
min_bin = n
for i in range(max_food, max_capacity+1):
    if dp[i][0] < min_bin:
        min_bin = dp[i][0]
        min_step = dp[i][1]
    elif dp[i][0] == min_bin:
        min_step = max(dp[i][1], min_step)
min_step = max_food - min_step
# print(max_food, min_step)
print(str(min_bin) + ' ' + str(min_step))

