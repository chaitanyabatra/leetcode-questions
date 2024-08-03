class Solution {
public:
    int hammingDistance(int x, int y) {
        x=x^y;
        y=0;
        while(x){
            if(x & true) y++;
            x>>=1;
        }
        return y;
    }
};