from .board import Board

def voisins(position : Board) -> list[Board]:
    """Give the reacheable positions one step away from a given one."""
    reachable_positions = []
    temp=position
    for move in position.allowed_moves(): # where the method calculates all the playable moved based on a given position
        temp.movement(move) # calculate a new position by playing a move on the former one
        reachable_positions.append(temp)
        temp=position
    return reachable_positions

def dijkstra(start_board):
    """Explore graph with dijkstra method."""
    priority_queue = [(start_board,0)]
    graph = {str(start_board): (0,None)}
    seen = [(start_board,0)]
    
    while priority_queue != []:
        temp = priority_queue.pop()
        print(temp)
        neighbors = voisins(temp[0])

        for elem in neighbors:

            if elem not in graph:
                graph[str(elem)] = (temp[1] + 1, temp[0])
            else:
                if temp[1] + 1 < graph[str(elem)][0]:
                    graph[str(elem)] = (temp[1] + 1, temp[0])
        
            flag=True
            for b in seen:
                if b[0] == elem:
                    flag = False
            if flag:
                seen.insert(0,(elem,temp[1] + 1))
                priority_queue.insert(0, (elem, temp[1] + 1))

    return graph

def solve(start_board, goal_board):
    """Solve the shortest path."""
    graph = dijkstra(goal_board)

    solution = [start_board]
    print("départ")
    print(start_board)
    temp = graph[str(start_board)][1]

    while temp is not None:
        solution.append(temp)
        temp = graph[str(temp)][1]

    return solution
