# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth)
# and returns a smooth path.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the previous video:
#
# If your function isn't submitting it is possible that the
# runtime is too long. Try sacrificing accuracy for speed.
# -----------
#gradient descent to make 
#(Xi-Yi)**2 --> min 
#(Yi-Yi+1)**2 --> min
#
# Xi means the element in old path
# Yi means the element in new path
# j means for x cordinate and y cordiante we use the same method
# tolerance means until the change would not make a difference big than that


from math import *

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

# ------------------------------------------------
# smooth coordinates
#

def smooth(path, weight_data = 0.5, weight_smooth = 0.1):

    # Make a deep copy of path into newpath
    newpath = [[0 for col in range(len(path[0]))] for row in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]


    #### ENTER CODE BELOW THIS LINE ###
    tolerance = 0.00001
    change = tolerance
    while (change >= tolerance):
        change = 0.0
        #a new round runs gradiant descent
        for i in range(1,len(path)-1):
            for j in range(len(path[0])):
                aux = newpath[i][j]
                newpath[i][j] = newpath[i][j] + weight_data * ( path[i][j] - newpath[i][j])
                newpath[i][j] = newpath[i][j] + weight_smooth * (newpath[i-1][j] + newpath[i+1][j] - (2.0 * newpath[i][j]))
                #how's the change compare with tolerance?
                change += abs(aux - newpath[i][j])
    return newpath # Leave this line for the grader!

# feel free to leave this and the following lines if you want to print.
newpath = smooth(path)

# thank you - EnTerr - for posting this on our discussion forum
for i in range(len(path)):
    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'






