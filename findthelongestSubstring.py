'''
lengthOfLongestSubstring(self, s: str)  给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
minWindow(self, s: 'str', t: 'str') 从S串中找到覆盖t串全部字符地最小子串
lengthOfLongestSubstringTwoDistinct(self, s: str) 寻找一个字符串中最多包含两个不同字符地最长子串
'''

class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] == 0:
                counter += 1
            lookup[s[end]] += 1
            end +=1
            while counter > 2:
                if lookup[s[start]] == 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sublen = 0
        if s == "":
            return max_sublen
        n = len(s)
        sub_str = []
        for i in range(n):
            if s[i] in sub_str:
                index = sub_str.index(s[i])
                sub_str = sub_str[index + 1:]
            sub_str.append(s[i])
            tmp_len = len(sub_str)
            if tmp_len > max_sublen:
                max_sublen = tmp_len
        return max_sublen


# a = "abaacd"
# res = Solution()
# print(res.lengthOfLongestSubstringTwoDistinct(a))











