class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n=len(hats)
        mod=10**9+7
        persons=defaultdict(list)
        for i,L in enumerate(hats):
            for h in L:
                persons[h].append(i)
        @lru_cache(None)
        def dp(hat,mask):
            if hat==41:
                if mask==(1<<n)-1: 
                    return 1
                return 0
            ans=0
            #we choose a person
            for p in persons[hat]:
                if (mask & (1<<p))==0:
                    ans+=dp(hat+1,mask | (1<<p))
                    ans%=mod
            #dont choose any person
            ans+=dp(hat+1,mask)
            return ans%mod
        return dp(1,0)
