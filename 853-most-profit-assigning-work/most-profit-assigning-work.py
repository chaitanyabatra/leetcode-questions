class Solution:
    def maxProfitAssignment(self, d: List[int], p: List[int], w: List[int]) -> int:
        w.sort()
        a=0
        ar=[]

        for i in range(len(d)):
            ar.append([d[i],p[i]])
        ar=sorted(ar, key=lambda x: (x[0],x[1]))
        print(ar)
        h=0
        k=0
        m=0
        print(w)
        for i in w:
            if i>=max(d):
                a=a+max(p)
            else:
                k=0
                for j in range(h,len(d)):
                    if i>=ar[j][0]:
                        k=1
                        h=j
                        if ar[j][1]>m:
                            m=ar[j][1]
                    else:
                        if k==1:
                            a=a+m
                        break
            print(a)


        return a

            
        
        