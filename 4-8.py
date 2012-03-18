# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    def motion(state, move, grid):
        row_index = state[0] + move[0]
        column_index = state[1] + move[1]
        if not 0<=row_index<len(grid) or not 0<=column_index<len(grid[0]):
            return []
        return [row_index, column_index]
    
    def valid_motion(index, grid):
        if grid[index[0]][index[1]] == 1:
            return []
        return index
    
    def goal_state(state, goal):
        return state == goal
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    state = init
    open_list = []
    used_list = []
    result = ''
    cost = 0
    while True:
        if goal_state(state, goal):
            return [cost, state[0], state[1]]
        else:
            used_list.append(state)
            movements = []
            for d in delta:
                movements.append(motion(state, d, grid))
            movements = filter(None, movements)
            cost += 1
            for m in movements:
                if valid_motion(m, grid) and m not in used_list:
                    open_list.append([cost,m[0], m[1]])
                    used_list.append(m)
        if not open_list:
            result = 'fail'
            break
        else:
            from operator import itemgetter
            open_list = sorted(open_list, key=itemgetter(0))
            state = open_list[0][1:]
            cost = open_list[0][0]
            open_list = open_list[1:] if len(open_list) > 1 else []
    return result

print search()




