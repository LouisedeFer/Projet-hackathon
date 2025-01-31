from .board import Board

def voisins(position : Board) -> List[Position]:
    """Give the reacheable positions one step away from a given one."""
    reachable_positions = []
    for move in position.allowed_moves(): # where the method calculates all the playable moved based on a given position
        next_position = position.play(move) # calculate a new position by playing a move on the former one
        reachable_positions.append(next_position)
    return reachable_positions



