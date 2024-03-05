class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)

        visited_stops = set([source])
        visited_routes = set()
        queue = deque([(source, 0)])  # (current stop, number of buses taken)

        while queue:
            current_stop, buses_taken = queue.popleft()
            if current_stop == target:
                return buses_taken

            for route_i in graph[current_stop]:
                if route_i not in visited_routes:
                    visited_routes.add(route_i)
                    for stop in routes[route_i]:
                        if stop not in visited_stops:
                            visited_stops.add(stop)
                            queue.append((stop, buses_taken + 1))

        return -1  # If no path exists
