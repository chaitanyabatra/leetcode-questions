class Solution {
public:
    int hammingDistance(int x, int y) {
        int ans=0;
        x=x^y;
        while(x){
            if(x & true) ans++;
            x>>=1;
        }
        return ans;
    }
};