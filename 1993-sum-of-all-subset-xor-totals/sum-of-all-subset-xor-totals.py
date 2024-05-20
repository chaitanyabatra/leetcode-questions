class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def process(index,nums,ans,tempans):

            if index==len(nums)-1:
                ans.append(tempans)
                ans.append(tempans^nums[index])
                return


            #choose
            process(index+1,nums,ans,tempans^nums[index])

            #notchoose
            process(index+1,nums,ans,tempans)

            
        ans=[]
        process(0,nums,ans,0)
        return sum(ans)