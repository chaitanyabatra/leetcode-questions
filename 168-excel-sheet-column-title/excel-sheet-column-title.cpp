class Solution {
public:
    string convertToTitle(int c) {
       string ans;
       while (c){
        c--;
        char a ='A'+c%26;
        c=c/26;
        ans=a+ans;
       } 
       return ans;
    }
};