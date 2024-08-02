class Solution {
public:
    int nonSpecialCount(int l, int r) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);
        int total=r-l+1;
        int n=ceil(sqrt(r))+1;
        vector<int> sieve(n,true);
        sieve[0]=false;
        sieve[1]=false;
        for(int p=2;p*p<n;p++){
            if (sieve[p]==true){
                for (int i=p*p;i<n;i+=p) sieve[i]=false;
            }
        }
        for (int i=ceil(sqrt(l));i<=floor(sqrt(r));i++){
            if (sieve[i]==true) total--;
        }
        return total;
    }
};//find primes in range l**0.5 to r**0.5[sieve] and then count how many primes,- that amount from r-l+1