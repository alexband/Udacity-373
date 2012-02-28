colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = [[1.0/20]*5] * 4

def sense(p, Z):
    q = []
    for i, a in enumerate(p):
        z = []
        for j, b in enumerate(a):
            hit = (Z == colors[i][j])
            z.append((b * (hit * sensor_right + (1-hit) * (1-sensor_right))))
        q.append(z)
    s = sum([x for y in q for x in y])
    for i, a in enumerate(q):
        for j, b in enumerate(a):
            q[i][j] = q[i][j] / s
    return q

STAY = [0,0]
RIGHT = [0,1]
LEFT = [0,-1]
DOWN = [1,0]
UP = [-1,0]

#if not move success ,stay in the same position
#the world is circular

def move(p, U):
    if U == STAY:
        return p
    elif U == RIGHT:
        q = []
        for glist in p:
            z = []
            for i in range(len(glist)):
                s = p_move * glist[(i-1) % len(glist)]
                s = s + (1-p_move) * glist[i]
                z.append(s)
            q.append(z)
        return q
    elif U == LEFT:
        q = []
        for glist in p:
            z = []
            for i in range(len(glist)):
                s = p_move * glist[(i+1) % len(glist)]
                s = s + (1-p_move) * glist[i]
                z.append(s)
            q.append(z)
        return q
    elif U == DOWN:
        q = []
        for i in range(len(p)):
            z = []
            current = p[i]
            upper = p[i-1]
            for j in range(len(current)):
                s = p_move * upper[j]
                s = s + (1-p_move) * current[j]
                z.append(s)
            q.append(z)
        return q
    elif U == UP:
        q = []
        for i in range(len(p)):
            z = []
            current = p[i]
            if i < len(p) - 1:
                lower = p[i+1]
            else:
                lower = p[0]
            for j in range(len(current)):
                s = p_move * lower[j]
                s = s + (1-p_move) * current[j]
                z.append(s)
            q.append(z)
        return q
    else:
        print 'wrong movement'
        return p


#Your probability array must be printed 
#with the following code.
for a, b in zip(motions, measurements):
    p = move(p, a)
    p = sense(p, b)

show(p)

