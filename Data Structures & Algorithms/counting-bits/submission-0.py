class Solution:
    def countBits(self, n: int) -> List[int]:
        ret_list=[]
        for i in range(n+1):
            res=0
            while i:
                i = i & (i-1)
                res+=1
            ret_list.append(res)
        return ret_list

        