#define intt long long
class Solution {
public:
    int numTeams(vector<int>& rating) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);

        intt n=rating.size();
        intt count=0;
        for(intt i=1;i<n-1;i++){
            intt leftgreater=0;
            intt leftsmaller=0;
            for (intt j=0;j<i;j++){
                if (rating[j]>rating[i]) leftgreater++;
                if (rating[j]<rating[i]) leftsmaller++;
            }
            intt rightgreater=0;
            intt rightsmaller=0;
            for (intt k=i+1;k<n;k++){
                if (rating[k]>rating[i]) rightgreater++;
                if (rating[k]<rating[i]) rightsmaller++;
            }
            count=count+leftgreater*rightsmaller+leftsmaller*rightgreater;
        }
        return count;
   }
};