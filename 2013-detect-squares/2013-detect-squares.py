class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = self.points.get(tuple(point), 0) + 1
        
    def count(self, point: List[int]) -> int:
        ans = 0
        x,y = point[0], point[1]
        
        for (x1, y1), count1 in self.points.items():
            
            if x1!=x and abs(x1-x)==abs(y1-y):
                if (x1,y) in self.points and (x, y1) in self.points:
                    ans+= self.points[(x1,y)]*self.points[(x, y1)]*count1
                  
        return ans
        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)