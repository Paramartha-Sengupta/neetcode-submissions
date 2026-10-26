class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # s="abcabcbb"
        hashmap = {}
        sub = ""
        maxsub=0
        i = -1
        for x in s:
            i+=1
            if x not in sub:
                hashmap[x]=i
                sub+=x
                # print('Pool 1')
                # print(x,i)
                # print(hashmap)
                # print(sub)
            else:
                sub=s[hashmap[x]+1:i]+x
                hashmap[x]=i
                # print('Pool 2')
                # print(x,i)
                # print(hashmap)
                # print(sub)
            maxsub = max(maxsub,len(sub))
        return maxsub


        