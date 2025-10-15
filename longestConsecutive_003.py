class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      longest_streak = 0
      num_set = set(nums)
      for num in num_set:
        if num-1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num+1 in num_set:
                current_num += 1
                current_streak += 1
          longest_streak = max(longest_streak,current_streak)
    return longest_streak

#暴力搜索n2
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        longest = 1

        # 外层：枚举每个位置作为起点候选
        for i in range(n):
            cur = nums[i]        # 当前连续段的末尾值
            length = 1           # 当前连续段长度至少为 1

            # 内层：不断在整个数组里寻找 cur+1
            while True:
                next_val = cur + 1
                found = False

                # 扫一遍数组，看有没有 next_val
                for j in range(n):
                    if nums[j] == next_val:
                        cur = next_val   # 扩展成功，更新末尾值
                        length += 1
                        found = True
                        break            # 这次找到后，退出本轮内层循环，再“重头”找下一个

                if not found:
                    # 没找到下一个，就结束扩展
                    break

            longest = max(longest, length)

        return longest
