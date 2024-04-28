import heapq
import itertools

class PuzzleNode:
    def __init__(self,state,parent=None,move=None,cost=0,heuristic=0):
        self.state = state
        self.parent = parent
        self.move = move 
        self.cost = cost
        self.heuristic = heuristic
        self.priority = cost + heuristic

    def __lt__(self,other):
        self.priority < other.priority
    
    def __eq__(self,other):
        self.state == other.state

def manhattan_distance(state):
    goal_state = [[1,2,3],[4,5,6],[7,8,0]]
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                value = state[i][j]
                target_i,target_j = divmod(value - 1,3)
                distance += abs(i - target_i) + (j - target_j)
    return distance

def generate_neighbours(node):
    neighbours = []
    for i in range(3):
        for j in range(3):
            if node.state[i][j] == 0:
                zero_i,zero_j = i,j
    for move_i,move_j in [(0,1),(1,0),(0,-1),(-1,0)]:
        new_i, new_j = zero_i + move_i, zero_j + move_j
        if 0 <= new_i <3 and  0<= new_j<3:
            new_state = [row[:] for row in node.state]   # new_state = node.state (not useful)
            new_state[zero_i][zero_j],new_state[new_i][new_j] = new_state[new_i][new_j],new_state[zero_i][zero_j]
            neighbours.append(PuzzleNode(new_state,node,move = (new_i,new_j),cost = node.cost+1,heuristic= manhattan_distance(new_state)))
    return neighbours

def solve_8_puzzle(initial_configuration):
    initial_state = PuzzleNode(initial_configuration,heuristic=manhattan_distance(initial_configuration))
    heap = [initial_state]
    heapq.heapify(heap)
    explored = set()

    while heap:
        current_node = heapq.heappop(heap)
        if current_node.state == [[1,2,3],[4,5,6],[7,8,0]]:
            return construct_solution(current_node)
    
        explored.add(tuple(itertools.chain.from_iterable(current_node.state)))

        for neighbours in generate_neighbours(current_node):
            if tuple(itertools.chain.from_iterable(neighbours.state)) not in explored:
                heapq.heappush(heap, neighbours)    

    return None        


def construct_solution(node):
    path = []
    while node.parent is not None:
        path.append((node.move,node.state))
        node = node.parent
    path.reverse()
    return path
    

initial_configuration = [[1,2,3],[4,5,6],[0,7,8]]

solution = solve_8_puzzle(initial_configuration)

if solution:
    for move, state in solution:
        print("move: ",move)
        for row in state:
            print(row)
        print(" - - - - - ")
else:
    print("Solution does not exist")