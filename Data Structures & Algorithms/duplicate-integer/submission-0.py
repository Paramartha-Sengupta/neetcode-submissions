class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_num={}
        for i,n in enumerate(nums):
            if n in dict_num:
                return True
            else:
                dict_num[n]=i
        return False
        