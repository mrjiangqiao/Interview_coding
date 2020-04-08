# Interview_coding
Interview coding practice, implement with python3

## file lists
### dp_forBracketStaining.py
1. 问题描述
成对括号染色问题：Codeforced 149D
给出你一个正确的括号序列(正确的括号序列指的是，对于整个序列，有且只有一种方式使得每个括号都可以完成匹配)，初始状态下，所有括号都是红色的，但是很显然这样太丑了。
RGB是一种很普遍的染色方案，现在需要你把部分括号染成绿色或者蓝色，要求染色完成后的括号满足以下条件：
(1) 每一对相匹配的括号中有且只有一个括号可以被染成绿色或蓝色，另一个保持红色。
(2) 相邻的括号不能同为绿色或者同为蓝色。
请问你共有多少种符合条件的染色方案，由于答案可能很大，所以请你输出方案数对998244353取模的结果。
2. 问题解析
* 利用堆栈入栈出栈找到互相匹配的括号
* 利用动态规划dp对问题进行分解
* f[x,y,i,j]表示给x位置开始y位置结束的括号序列，x处染i颜色,y处染j颜色时候的共有多少种染色方案，初始化为0
* 最基础子问题为y=x+1的情况，此时正确染色情况分为4中且染色方案数量均为1；
然后每个大问题可以分解
（1）x,y正好匹配时候的情况：f[x,y,i,j]与f[x+1,y-1,i,j]存在联系
（2）x,y不匹配的情况：寻找到与x匹配的位置mid_pair，则
``` 
f[x,y,i,j] = f[x,y,i,j] + f[x,mid_pair,i,m]*f[mid_pair+1,y,n,j]
```

### find_kth_in_specific_array.py
1. 问题描述
找到N行M列矩阵中第k大的数字
2. 问题解析
* 部分有序序列可以使用二分查找来进行处理
* 返回数组中小于等于当前中间值的数字的数量，从而不断地缩小查找范围更新中间值

### Singlelist.py
使用python实现单链表，转载，对应博客内容请参考[博客链接]（https://www.cnblogs.com/yudanqu/）

### findthelongestSubstring.py
1. 功能描述
lengthOfLongestSubstring(self, s: str)  给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
minWindow(self, s: 'str', t: 'str') 从S串中找到覆盖t串全部字符地最小子串
lengthOfLongestSubstringTwoDistinct(self, s: str) 寻找一个字符串中最多包含两个不同字符地最长子串

### FindMedianSortedArrays.py
1. 问题描述
寻找两个有序序列合并后的中值问题 Leetcode 4，要求时间复杂度 O(log(m + n))，m与n分别为两个序列的长度
2. 问题解析
将两个有序序列分别取midi,midj将原序列分为两个部分，并合并左侧部分作为min_left,合并右侧部分（包含midi与midj处的值）作为max_right。
令左右两部分满足左边的最大值小于右侧的最小值，并保障两个部分中元素数量差值小于等于1。
满足上述的序列中很容易获得两个有序序列合并后的中值。

### DistanceToNextLargernum.py
1. 问题描述
输入整数序列，最大100，输出当前元素到之后第一个比他大的元素的距离，
没有更大的话输出-1，比如输入1，20，10，40输出1，2，1，-1，时间复杂度不大于O（n）

### findsensitivewords.py
1. 问题描述
替换字符串中敏感词为对应字符数量的\*号，敏感词不区分大小写
2、解决方法
此处利用了python中的re工具包中的相关函数来实现，注意其中matchfunc函数的写法以及sub函数中flags=re.I参数的作用

### findsimilarstr.py
1. 问题描述
将字符串变换具有相似模式的顺序字符串，如将“efggac”转换为“abccde”

### mergesort_and_quicksort.py
1. 功能描述
快速排序以及归并排序的简单实现

### re_char2ascii.py
1、功能描述
将excel表格的单元格描述方式进行转换
change1()函数将“R15C29”转换为对应的“AC15”
change2()函数将“AC15”转换为对应的“R15C29”



