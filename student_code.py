from queue import PriorityQueue

def shortest_path(M,start,goal):
    my_map = M
    path = []
    def distance(a, b):
        (x1, y1) = my_map.intersections[a]
        (x2, y2) = my_map.intersections[b]
        return (((x1 - x2)**2) + ((y1 - y2)**2))**0.5

    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from, cost_so_far = {}, {}
    came_from[start], cost_so_far[start] = None, 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            continue
        
        for next in my_map.roads[current]:
            new_cost = cost_so_far[current] + distance(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                
                # f = g + h
                priority = new_cost + distance(goal,next)
                frontier.put(next, priority)
                came_from[next] = current
    
    current = goal
    try:
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()   
        return path
    except:
        return "No path found"
    
