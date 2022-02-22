class Solution:
    def reorganizeString(self, s: str) -> str: 
        res="" 
        charc=Counter(s) 
        heap=[[-cnt,char] for char,cnt in charc.items()] 
        heapq.heapify(heap) 
        
        prev = None 
        
        while heap or prev: 
            if prev and not heap: 
                return "" 
            
            cnt,char=heapq.heappop(heap) 
            res+=char 
            cnt+=1 
            
            if prev: 
                heapq.heappush(heap,prev) 
                prev=None 
                
            if cnt!=0: 
                prev = [cnt, char]  
                
        return res
        
