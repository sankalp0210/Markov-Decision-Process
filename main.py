from copy import deepcopy
# Input Part
data = []
n, m = map(int,raw_input().split())
for i in range(n):
    data.append(map(float, raw_input().split()))

e, w = map(int,raw_input().split())
end = []
wall = []
for i in range(e):
    end.append(map(int, raw_input().split()))
for i in range(w):
    wall.append(map(int,raw_input().split()))

start_i, start_j = map(int, raw_input().split())
unit_step = float(raw_input())

# initialisation
final_util = deepcopy(data)
temp_util = deepcopy(data)


# checking if the state is valid or not
def check_state(p, q):
    if( p>=n or q>=m or p<0 or q<0 or [p, q] in wall):
        return False
    return True


def argmax(p,q):
    moveVal = [0, 0, 0, 0]
    stateVal = [0, 0, 0, 0]

    stateVal[0] = temp_util[p+1][q] if check_state(p+1,q) else temp_util[p][q] 
    stateVal[1] = temp_util[p][q+1] if check_state(p,q+1) else temp_util[p][q] 
    stateVal[2] = temp_util[p-1][q] if check_state(p-1,q) else temp_util[p][q] 
    stateVal[3] = temp_util[p][q-1] if check_state(p,q-1) else temp_util[p][q] 

    moveVal[0] = 0.8*stateVal[0] + 0.1*stateVal[1] + 0.1*stateVal[3]
    moveVal[1] = 0.8*stateVal[1] + 0.1*stateVal[0] + 0.1*stateVal[2]
    moveVal[2] = 0.8*stateVal[2] + 0.1*stateVal[1] + 0.1*stateVal[3]
    moveVal[3] = 0.8*stateVal[3] + 0.1*stateVal[0] + 0.1*stateVal[2]

    return max(moveVal)


# value iteration
delta = 1
numIter = 0
for i in range(n):
        st = ''
        for j in range(m):
            st += str("{0:.3f}".format(final_util[i][j])) + '\t'
        print st
print '\n' 
while(delta >= 0.01):
    delta = 0
    numIter += 1
    temp_util = deepcopy(final_util)
    for i in range(n):
        for j in range(m):
            if not ([i, j] in end or [i,j] in wall):
                final_util[i][j] = 0.99*argmax(i,j) + unit_step
            if temp_util[i][j] != 0:
                delta = max(delta, abs(final_util[i][j] - temp_util[i][j])/temp_util[i][j])
            else:
                delta = max(delta, abs(final_util[i][j] - temp_util[i][j]))
    for i in range(n):
        st = ''
        for j in range(m):
            st += str("{0:.3f}".format(final_util[i][j])) + '\t'
        print st
    print '\n' 
print "Number of Iterations : ", numIter
