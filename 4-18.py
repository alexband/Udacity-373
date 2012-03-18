# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------
def compute_value():
    def motion(state, move, grid):
        row_index = state[0] + move[0]
        column_index = state[1] + move[1]
        if not 0<=row_index<len(grid) or not 0<=column_index<len(grid[0]):
            return []
        return [row_index, column_index]

    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    value[goal[0]][goal[1]] = 0
    policy[goal[0]][goal[1]] = '*'
    open_list = []
    used_list = []
    open_list.append([0,goal[0],goal[1]])
    used_list.append(goal)
    while open_list:
        open_list.sort()
        open_list.reverse()
        next = open_list.pop()[1:]
        movements = []
        for i, d in enumerate(delta):
            move = motion(next, d, grid)
            if move:
                movements.append([move[0], move[1], i])
        for m in movements:
            if m[:2] not in used_list:
                used_list.append([m[0],m[1]])
                if grid[m[0]][m[1]] == 1:
                    value[m[0]][m[1]] = 99
                else:
                    v = value[next[0]][next[1]]+1
                    value[m[0]][m[1]] = v
                    open_list.append([v, m[0],m[1]])
                    policy[m[0]][m[1]] = delta_name[(m[2]+2) % 4]
    return policy #make sure your function returns a grid of values as demonstrated in the previous video.



value = compute_value()
for v in value:
    print v
