class Solution {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);
        int n=books.size();
        vector<int> cache(n,-1);
        function<int(int)> go = [&](int i) {
            
            if (i==n) return 0;
            if (cache[i]!=-1) return cache[i];
            int currwidth=shelfWidth;
            int maxheight=0;
            int minheight=10000000;
            for(int j=i;j<n;j++){
                int width=books[j][0];
                int height=books[j][1];
                if(width>currwidth) break;
                currwidth=currwidth-width;
                maxheight=max(maxheight,height);
                minheight=min(minheight,go(j+1)+maxheight);
            }
            cache[i]=minheight;
            return cache[i];
        };
        return go(0);
    }
};