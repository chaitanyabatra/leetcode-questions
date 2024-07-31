class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        // ios_base::sync_with_stdio(false);
        // cin.tie(0);
        // cout.tie(0);
        long long n=matrix.size();
        long long m=matrix[0].size();
        vector<int> minrow(n,1000000);
        vector<int> maxcol(m,0);
        for(int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                minrow[i]=min(minrow[i],matrix[i][j]);
                maxcol[j]=max(maxcol[j],matrix[i][j]);
            }
        }
        vector<int> ans;
        // for(auto it:minrow) cout<<"minrow"<<it<<endl;
        // for(auto it:maxcol) cout<<"maxcol"<<it<<endl;

        for(int i =0;i<n;i++){
            for(int j=0;j<m;j++){
                if (minrow[i]==maxcol[j]) ans.push_back(minrow[i]);
            }

        }
        return ans;
    }
};