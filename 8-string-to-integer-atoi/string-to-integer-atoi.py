class Solution:
    def myAtoi(self, s: str) -> int:
        ans=0
        flag=False
        flag2=False
        fflag=False
        for i in s:
            if i=="-" and ans==0 and not fflag:
                if flag:break
                flag=True
            elif ord(i)>47 and ord(i)<58:
                fflag=True
                ans=ans*10**1
                ans+=(ord(i)-48)
            elif i !=" ":
                if i!="+": break
                else:
                    if fflag or flag2:break
                    flag2=True
            else:
                if fflag or flag or flag2:break
        if flag:
            if flag2: return 0
            ans*=(-1)
        ans=min(ans,2**31-1)
        ans=max(ans,-1*(2**31))
        
        return ans