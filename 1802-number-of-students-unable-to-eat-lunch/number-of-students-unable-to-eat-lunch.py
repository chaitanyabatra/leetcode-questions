class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sqst,crst=0,0
        for i in students:
            if i==1:
                sqst+=1
            else:
                crst+=1
        for i in sandwiches:
            if i==1:
                if sqst>0:
                    sqst-=1
                else:
                    break
            if i==0:
                if crst>0:
                    crst-=1
                else:
                    break
        return crst+sqst