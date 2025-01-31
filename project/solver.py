from .board import Board

def voisins(position : Board) -> List[Position]:
    """Give the reacheable positions one step away from a given one."""
    reachable_positions = []
    for move in position.allowed_moves(): # where the method calculates all the playable moved based on a given position
        next_position = movement(position, move) # calculate a new position by playing a move on the former one
        reachable_positions.append(next_position)
    return reachable_positions

def dijkstra(start_board):
    """Explore graph with dijkstra method."""
    priority_queue = [(start_board,0)]
    graph = {start_board: (0,None)}
    seen = []
    
    while priority_queue != []:
        temp = priority_queue.pop()
        neighbors = voisins(temp[0])

        for elem in neighbors:

            if elem not in graph:
                graph[elem] = (temp[1] + 1, temp[0])
            else:
                if temp[1] + 1 < graph[elem]:
                    graph[elem] = (temp[1] + 1, temp[0])
        
            if elem not in seen:
                seen.insert(0,(elem,temp[1] + 1))

    return graph

def solve(start_board, goal_board):
    """Solve the shortest path"""
    graph = dijkstra(goal_board)

    distance = graph[start_board][0]

    solution = [start_board]
    temp = graph[start_board][1]

    while temp is not None:
        solution.append(temp)
        temp = graph[temp][1]

    return distance, solution
