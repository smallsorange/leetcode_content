class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for i,num in enumerate(nums):
            complements=target-num
            if complements in num_map:
                return [num_map[complements],i]#补数索引和当前索引
            num_map[num]=i #返回2到字典

#运行逻辑
#1.输出nums target，建立hash字典，加快处理速度
#2.遍历循环，enumerate，i是序号，num是数值大小
#3.计算差值complements
#4.判断 如果complements在hash字典里面就返回 补数索引和当前索引i
#5.将数值key和索引value保存到字典里面 {num：i}
