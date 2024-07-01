class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        start by adding beginword to the beginning of the wordlist
        make adj array using onediff function
        in onediff function we iterate over both words in wordList together such that the difference between them is of one character only
        then we start a bfs at beginWord till we get to endWord(k), updating our count
        after q empty, if count is not 0 we return count else we return 0
        """
        wordList.insert(0, beginWord)
        if endWord not in wordList:return 0
        e=wordList.index(endWord)
        m=len(wordList)
        n=len(wordList[0])

        def onediff(i,j):
            diff=0
            a=wordList[i]
            b=wordList[j]
            for k in range(n):
                if a[k]!=b[k]:
                    diff+=1
            return diff==1
        
        
        adj=[[] for _ in range(m)]
        for i in range(m):
            for j in range(i+1,m):
                if onediff(i,j):
                    adj[i].append(j)
                    adj[j].append(i)
                    
        q=deque()
        vis=[0 for _ in range(m)]
        q.append([0,1])
        vis[0]=1
        while q:
            node,dist=q.popleft()
            for a in adj[node]:
                if vis[a]==0:
                    vis[a]=1
                    if a==e:return dist+1
                    else:
                        q.append([a,dist+1])
                        
        return 0