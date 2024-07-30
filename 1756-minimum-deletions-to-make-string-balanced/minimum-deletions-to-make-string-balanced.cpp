class Solution {
public:
    int minimumDeletions(string s) {
        int n=s.size();
        vector<int> before_b (n,0);
        vector<int> after_a (n,0);
        for(int i=1;i<n;i++){
            if (s[i-1]=='b') {
                before_b[i]=before_b[i-1]+1;
            }
            else before_b[i]=before_b[i-1];
        }
        for(int i=n-2;i>=0;i--){
            if (s[i+1]=='a') {
                after_a[i]=after_a[i+1]+1;
            }
            else after_a[i]=after_a[i+1];
        }
        int ans=INT_MAX;
        for (int i=0;i<n;i++){
            ans=min(ans,before_b[i]+after_a[i]);

        }
        return ans;

        
    }
};