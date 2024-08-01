class Solution {
public:

    static bool comp(int n1,int n2,vector<int>& mapp){
        string s1=to_string(n1);
        for (auto& it:s1){
            it=mapp[it-'0']+'0';
        }
        string s2=to_string(n2);
        for (auto& it:s2){
            it=mapp[it-'0']+'0';
        }
        int a1=stoi(s1);
        int a2=stoi(s2);
        return a1<a2;
    }
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        auto comparator=[&](int n1, int n2){return comp(n1,n2,mapping);};
        sort(nums.begin(),nums.end(),comparator);
        return nums;
    }

};