class Solution {
public:
    string reverseWords(string s) {
        stack<string> st;
        int n=s.size();
        int i=0;
        while (i<n){
            string temp;
            while (s[i]!=' ' && i<n){
                temp+=s[i];
                i++;
            }
            if (temp.size()!=0) st.push(temp);
            i++;
        }
        string ans;
        string t=st.top();
        st.pop();
        ans+=t;
        while (!st.empty()){
            string p=st.top();
            st.pop();
            ans+=' '+p;
        }
        return ans;
    }
};