static int fastIO = []
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    return 0;
}();
class Solution {
public:
    int numTeams(vector<int>& rating) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);

        long long count=0;
        long long n=rating.size();
        for (int i=0;i<n-2;i++){
            for(int j=i;j<n-1;j++){
                for(int k=j;k<n;k++){
                    if (rating[i]>rating[j] && rating[j]>rating[k]) count++;
                    if (rating[i]<rating[j] && rating[j]<rating[k]) count++;
                }
            }
        }
        return count;
    }
};