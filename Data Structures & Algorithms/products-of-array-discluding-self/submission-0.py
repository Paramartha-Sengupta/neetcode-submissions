class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_arr = [1]*len(nums)
        r_arr = [1]*len(nums)
        l_val, r_val = 1,1
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                l_val = l_val * nums[i-1]
                l_arr[i] = l_val
        for j in range(len(nums)-1,-1,-1):
            if j==len(nums)-1:
                continue
            else:
                r_val = r_val * nums[j+1]
                r_arr[j] = r_val
        for k in range(len(nums)):
            l_arr[k] = l_arr[k] * r_arr[k]
        return l_arr

        