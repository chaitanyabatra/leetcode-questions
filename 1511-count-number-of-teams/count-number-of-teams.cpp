#include <iostream>
#include <vector>

using namespace std;

static int fastIO = []{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    return 0;
}();

class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        if (n < 3) return 0;
        
        int count = 0;
        for (int i = 0; i < n; ++i) {
            int leftSmaller = 0, leftLarger = 0;
            int rightSmaller = 0, rightLarger = 0;
            
            // Count elements smaller and larger than rating[i] on the left
            for (int j = 0; j < i; ++j) {
                if (rating[j] < rating[i]) leftSmaller++;
                if (rating[j] > rating[i]) leftLarger++;
            }
            
            // Count elements smaller and larger than rating[i] on the right
            for (int k = i + 1; k < n; ++k) {
                if (rating[k] < rating[i]) rightSmaller++;
                if (rating[k] > rating[i]) rightLarger++;
            }
            
            // Calculate valid teams
            count += leftSmaller * rightLarger + leftLarger * rightSmaller;
        }
        
        return count;
    }
};
