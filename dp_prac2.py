# -*-coding:utf-8-*-
'''
现在有两个串S和T，你需要从S中取出一个子串，并且从T中取出一个子序列，使得两个取出来的串一样。
这样不同的方案有多少？答案对10^9+7取模。
子串的意思是在字符串中截取连续一段，比如bc是abcd的子串。
子序列的意思是在字符串中截取不一定连续的几段（也可以是一段）连在一起，比如ac是abcd的子序列。
注意，在本题中，两种取法位置不同，但是取出来的字符串是相同的情况算作两种不同的情况，详见样例解释。
输入
输入包含两个字符串S,T  一行一个字符串
|S|,|T|≤5000
输出
输出包含一个数，代表答案对10^9+7取模。

样例输入
aaa
aaa
样例输出
16
提示
样例解释
S有6个子串，T有7个子序列。
S的6个子串：a(1),a(2),a(3),aa(12),aa(23),aaa(123);
T的7个子序列：a(1),a(2),a(3),aa(12),aa(23),aa(13),aaa(123);
可以得知，如果这个相同的串为a，有3×3种取法，如果这个相同的串为aa，有2×3种取法，如果这个相同的串为aaa，有1×1种取法。
总共有16种取法。

解析：
先找出S中的全部子串，再在T中寻找能够获得S的某个字串的挑选方法
'''


spec_str_num = {}
def getsubstr(input_str, len_input):
    for l in range(len_input):
        for r in range(l+1, len_input+1):
            tmp_sub_str = input_str[l:r]
            if tmp_sub_str not in spec_str_num.keys():
                spec_str_num[tmp_sub_str] = 1
            else:
                spec_str_num[tmp_sub_str] += 1

'''
dp[m][n]表示在T[0,m)中可以提取多少个sub_str[0,n)
初始条件：
当n==0时，即目标子串为空时，在一个子串中获得一个空串有1中选择，dp[:][0]=1
当m=0时，从空串选择若干元素构成一个非空串，实现方式为0，dp[0][:]=0
转移方程，除了初始条件外，当T[m-1]==sub_str[n-1]时，
dp[m][n] = dp[m-1][n-1]+dp[m-1][n] 两加和项分别表示匹配选择结果中是否包含T[m-1]时的选择情况
当T[m-1]！=sub_str[n-1]时，dp[m][n] = dp[m-1][n]
由于每次求值只需要根据矩阵当前元素的正上方元素与左上角元素来确认，因此实际实现时可以仅使用dp[m]来实现
并用pre变量来不断变化保存当前dp[m][n]的dp[m-1][n-1]
'''
def numDistinct(T, sub_str):
    T_len = len(T)
    sub_str_len = len(sub_str)
    if T_len < sub_str_len:
        return 0
    else:
        dp = [1] * (T_len+1)
        for i in range(1, sub_str_len+1):
            pre = dp[0]  # n=1时，pre一开始对应于n=0时的dp[0]=1,之后dp[0]=0
            dp[0] = 0    # 除了n=0时，其他情况下dp[0][n]=0
            for j in range(1, T_len+1):
                temp = dp[j]  # 对于j+1来说，pre为更新前的dp[j],对应dp[m-1][n-1]
                if T[j-1] == sub_str[i-1]:
                    dp[j] = dp[j-1] + pre   # 对于j+1来说，更新后的dp[j],对应dp[m-1][n]
                else:
                    dp[j] = dp[j-1]
                pre = temp
    return dp[T_len]

S = input()
T = input()
n1 = len(S)
mod_num = 10**9+7
output = 0
getsubstr(S, n1)
for tmp_sub_str in spec_str_num.keys():
    num_tmp_sub_str = spec_str_num[tmp_sub_str]
    match_num = numDistinct(T, tmp_sub_str)
    output += ((num_tmp_sub_str * match_num) % mod_num)
    output = output % mod_num
print(output)