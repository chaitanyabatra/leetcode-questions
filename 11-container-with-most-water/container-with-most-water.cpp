class Solution {
public:
    int maxArea(vector<int>& height) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);
        
        int maxarea=0;
        int l=0;
        int r=height.size()-1;

        while (l<r){
            maxarea=max(maxarea,(r-l)*min(height[l],height[r]));

            if (height[l]>height[r]) r--;
            else l++;
        }
        return maxarea;
    }
};