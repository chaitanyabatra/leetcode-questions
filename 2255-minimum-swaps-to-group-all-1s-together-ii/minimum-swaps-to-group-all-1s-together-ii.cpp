class Solution {
public:
    int minSwaps(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);
        int n=nums.size();
        int total=accumulate(nums.begin(), nums.end(), 0);
        int ans=total;
        int temp=accumulate(nums.begin(),nums.begin()+total,0);
        for (int i=0;i<(n);i++){
            ans=min(ans,total-temp);
            temp=temp+nums[(i+total)%n]-nums[i];

        }
        
        return ans;
    }
};