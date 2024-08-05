class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);
        unordered_set<string> distinct;
        unordered_set<string> duplicate;

        for (auto it: arr){
            if (duplicate.count(it)) continue;
            
            if (distinct.count(it)) {
                distinct.erase(it);
                duplicate.insert(it);
            } else {
                distinct.insert(it);
            }
        }
        for (auto it:arr){
            if (distinct.count(it))k--;
            if (k==0) return it;
        }
        return "";

    }
};