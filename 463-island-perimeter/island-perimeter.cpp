class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);
        int edge=0;
        int row=grid.size();
        int col=grid[0].size();

        for (int r=0;r<row;r++){
            for (int c=0;c<col;c++){
                if (grid[r][c]==1){
                    if ((r == 0) || (grid[r - 1][c] == 0)) edge++;
                    if ((r == (row - 1)) || (grid[r + 1][c] == 0)) edge++;
                    if ((c == 0) || (grid[r][c - 1] == 0)) edge++;
                    if ((c == (col - 1)) || (grid[r][c + 1] == 0)) edge++;
                }
            }
        }
        return edge;
    }
};