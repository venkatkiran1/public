class Solution:
    def minScore(self, n, r):
        k = len(r)
        ds = [[] for _ in range(n+1)]
        for i in range(k):
            ds[r[i][0]].append((r[i][1], r[i][2]))
            ds[r[i][1]].append((r[i][0], r[i][2]))
        
        vis = [0] * (n+2)
        
        q = []
        q.append([n, float('inf')])
        mini = float('inf')
        
        while q:
            tp = q.pop(0)
            mini = min(mini, tp[1])
            vis[tp[0]] = 1 
            for ele in ds[tp[0]]:
                if not vis[ele[0]]:
                    q.append([ele[0], ele[1]])
        
        return mini