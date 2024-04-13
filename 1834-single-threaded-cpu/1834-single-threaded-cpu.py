class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        sortedTasks = [[t[0],t[1],idx] for idx, t in enumerate(tasks)]
        sortedTasks.sort()
        minHeap = []
        ans = []
        i = 0 #pointer to the task in sortTasks
        n = len(tasks)
        curTime = 0 
        curTask = []
        
        while len(ans)<n:
            
            while i<n and sortedTasks[i][0]<=curTime:
                heapq.heappush(minHeap, (sortedTasks[i][1], sortedTasks[i][2]))
                i+=1
            
            if minHeap:
                processTime, idx  = heapq.heappop(minHeap)
                curTime+=processTime
                ans.append(idx)
            
            else:
                curTime = sortedTasks[i][0]
                
            
        return ans
                
            
            
        
        
        
        
        
        
        
            