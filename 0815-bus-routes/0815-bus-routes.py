class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source==target:
            return 0
        
        graph = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)
        
        queue = deque([(source, 0)])
        v_stop = set()
        v_bus = set()
        
        while(queue):
            stop, busNum = queue.popleft()
            
            if stop==target:
                return busNum
                
            for bus in graph[stop]:
                if bus not in v_bus:
                    v_bus.add(bus)
                    for stop in routes[bus]:
                        if stop not in v_stop:
                            v_stop.add(stop)
                            queue.append((stop, busNum+1))
                            
        
        return -1
            
        
                
            
