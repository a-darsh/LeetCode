import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        
        m,n  = len(nums1), len(nums2)
        
        if not m or not n:
            return []
        
        minHeap = [[(nums1[0]+nums2[0]), 0,0]]
        ans = []
        visited = set()
        while minHeap and k:
            _,i,j = heapq.heappop(minHeap)
            ans.append([nums1[i],nums2[j]])
            k-=1
            if i+1<m and (i+1,j) not in visited:
                heapq.heappush(minHeap, [nums1[i+1]+nums2[j],i+1,j])
                visited.add((i+1,j))
            if j+1<n and (i,j+1) not in visited:
                heapq.heappush(minHeap, [nums1[i]+nums2[j+1],i,j+1])
                visited.add((i,j+1))
        return ans
            