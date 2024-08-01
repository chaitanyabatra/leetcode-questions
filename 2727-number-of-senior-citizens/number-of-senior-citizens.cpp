class Solution {
public:
    int countSeniors(vector<string>& details) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);
        int n=details.size();
        int count=0;
        for (int i=0;i<n;i++){
            int age=stoi(details[i].substr(11,2));
            if (age>60) count++;
        }
        return count;
    }
};