class Solution {
public:
    static bool comp(pair<int,int> p1, pair<int,int> p2){
        if (p1.first<p2.first) return true;
        if (p1.first>p2.first) return false;
        if (p1.second>p2.second) return true;
        return false;
    }
    vector<int> frequencySort(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);

        map<int,int> mp;
        for (auto it:nums){
            mp[it]+=1;
        }
        vector<pair<int,int>> peep; 
        for (auto it:mp){
            peep.push_back({it.second,it.first});
        }
        sort(peep.begin(),peep.end(),comp);

        vector<int> ans;

        for (auto it:peep){
            int freq=it.first;
            int num=it.second;
            for(int i=0;i<freq;i++){
                ans.push_back(num);
            }
        }
        return ans;
    }
};