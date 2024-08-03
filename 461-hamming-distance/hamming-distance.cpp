class Solution {
public:
    int hammingDistance(int x, int y) {
        int result = x^y;
        int answer=0;
        while(result>0){
            answer+=result&1;
            result>>=1;
        }
        return answer;
    }
};
