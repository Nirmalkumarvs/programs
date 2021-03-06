class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        g = [3*n * [1] for _ in range(3*n)]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == '\\':
                    g[3*r][3*c]=g[r*3+1][c*3+1]=g[r*3+2][c*3+2]=0
                elif grid[r][c] == '/':
                    g[3*r][c*3+2]=g[3*r+1][c*3+1]=g[3*r+2][c*3]=0
        def check(r,c,n,g):
            if r < 0 or c <0 or r == n or c == n or g[r][c] != 1:
                return
            g[r][c] = 2
            check(r-1,c,n,g)
            check(r+1,c,n,g)
            check(r,c-1,n,g)
            check(r,c+1,n,g)
        
        res = 0
        for r in range(3*n):
            for c in range(3*n):
                if g[r][c] == 1:
                    res +=1
                    check(r,c,n*3,g) 
        return res
       
