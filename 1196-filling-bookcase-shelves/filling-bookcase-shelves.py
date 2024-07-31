class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """ 
        cache={}       
        def go(i):
            if i==len(books):return 0
            if i in cache:return cache[i]
            currwidth,maxheight=shelfWidth,0
            minheight=float('inf')
            for j in range(i,len(books)):
                width,height=books[j]
                if width>currwidth:break
                currwidth-=width
                maxheight=max(height,maxheight)
                minheight=min(minheight,go(j+1)+maxheight)
                cache[i]=minheight
            return minheight
        return go(0)