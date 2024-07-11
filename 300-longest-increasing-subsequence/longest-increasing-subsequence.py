class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        # code here
        n=len(arr)
        temp=[arr[0]]
        l=1
        for i in range(1,n):
            if arr[i]>temp[-1]:
                temp.append(arr[i])
                l+=1
            else:
                ind=bisect.bisect_left(temp,arr[i])
                temp[ind]=arr[i]
        return l