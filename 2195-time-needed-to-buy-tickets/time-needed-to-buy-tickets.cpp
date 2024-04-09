class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int count=0;
        for(int i=0;i<=k;i++){
            if(tickets[i]<=tickets[k]){
                count+=tickets[i];
            }
            else{
                count+=tickets[k];
            }
        }
        for(int i=k+1;i<tickets.size();i++){
            if(tickets[i]<tickets[k]){
                count+=tickets[i];
            }
            else{
                count+=(tickets[k]-1);
            }
        }
        return(count);
    }
};