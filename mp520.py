import random

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

#global variables
bfs_queue = []
dfs_queue = []
uc = []
visited = []
a = []
visited = []
costA = 0
not_good_states = []
'''
BFS add to queue
'''

def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    global bfs_queue
    if initialize == True:
        bfs_queue = []
    if node_id <= 0:
        return
    bfs_queue.append((node_id,parent_node_id))

'''
BFS add to queue
'''
def is_queue_empty_BFS():
    # Your code here
    if bfs_queue == []:
        return True
    else:
        return False

'''
BFS pop from queue
'''
def pop_front_BFS():
    if bfs_queue == []:
        return (0,0)
    (node_id, parent_node_id) = bfs_queue.pop(0)
    return (node_id, parent_node_id)

'''
DFS add to queue
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    global dfs_queue
    if initialize == True:
        dfs_queue = []
    if node_id <= 0:
        return
    dfs_queue.insert(0,(node_id,parent_node_id))

'''
DFS add to queue
'''
def is_queue_empty_DFS():
    # Your code here
    if dfs_queue == []:
        return True
    else:
        return False

'''
DFS pop from queue
'''
def pop_front_DFS():
    if dfs_queue == []:
        return (0,0)
    (node_id, parent_node_id) = dfs_queue.pop(0)
    return (node_id, parent_node_id)

'''
UC add to queue
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    global uc
    global visited
    if initialize==True:
        uc=[]
        uc.append((node_id,parent_node_id,cost))
    else:
        sum_cost= cost
        present= False
        for x in range(len(visited)):
            if visited[x][0]==parent_node_id:
                if sum_cost<visited[x][1]:
                    del visited[x]
                    visited.append((parent_node_id,sum_cost))
                present= True
                break
        if not present:
            visited.append((parent_node_id,sum_cost))
        uc.append((node_id,parent_node_id,sum_cost))
    return

'''
UC empty queue
'''
def is_queue_empty_UC():
    # Your code here
    global uc
    if uc == []:
        return True
    else:
        return False

'''
UC pop from queue
'''
def pop_front_UC():
    (node_id, parent_node_id) = (0, 0)
    global uc
    min_cost_index= uc.index(min(uc,key= lambda t: t[2]))
    min_cost_node= uc.pop(min_cost_index)
    return (min_cost_node[0], min_cost_node[1])

'''
A* add to queue
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):

    global a
    if initialize == True:
        a = []
        a.append((node_id, parent_node_id, cost))
    else:
        totalCost = cost
        a.append((node_id, parent_node_id, totalCost))
    return

'''
A* add to queue
'''
def is_queue_empty_ASTAR():
    global a
    if len(a) > 0:
        return False
    else:
        return True

'''
A* pop from queue
'''
def pop_front_ASTAR():
    (node_id, parent_node_id) = (0, 0)
    global a
    global costA
    minimumNode = a.pop(a.index(min(a, key=lambda t: t[2])))
    node_id = minimumNode[0]
    parent_node_id = minimumNode[1]
    return (node_id, parent_node_id)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state
'''
def get_random_state(n):
    state = []
    for i in range(n):
        state.append(random.randint(1,n))
    print(state)
    return state

'''
Compute pairs of queens in conflict
'''
def compute_attacking_pairs(board):
    board = [i-1 for i in board]
    n = len(board)
    row_frequency = [0] * n
    main_diag_frequency = [0] * (2 * n)
    secondary_diag_frequency = [0] * (2 * n)

    for i in range(n):
        row_frequency[board[i]] += 1
        main_diag_frequency[board[i] + i] += 1
        secondary_diag_frequency[n - board[i] + i] += 1

    # print(row_frequency)
    # print(main_diag_frequency)
    # print(secondary_diag_frequency)

    conflicts = 0
    # formula: (N * (N - 1)) / 2
    for i in range(2*n):
        if i < n:
            conflicts += (row_frequency[i] * (row_frequency[i]-1)) / 2
        conflicts += (main_diag_frequency[i] * (main_diag_frequency[i]-1)) / 2
        conflicts += (secondary_diag_frequency[i]
                      * (secondary_diag_frequency[i]-1)) / 2

    return int(conflicts)

'''
The basic hill-climing algorithm for n queens
'''
def hill_descending_n_queens(state, comp_att_pairs):
    n = len(state) #[3,4,1,2]
    min = 10000
    final_state = []
    k=0
    temp = state
    flag = True
    while(1):
        flag = True
        for j in range(1,n+1): #j = 1
            for i in range(1,n+1):  #i = 1
                temp1 = comp_att_pairs(temp[:j-1]+[i]+temp[j:])  #2
                if temp1<min:
                    min = temp1  #2
                    final_state = temp[:j-1]+[i]+temp[j:]  #[1,4,1,2]
                    flag = False
        if flag == True:
            break
        temp = final_state
    # Your code here
    return final_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    final_state = []
    # Your code here
    while(1):
        '''if state in not_good_states:
            continue'''
        state = hill_descending_n_queens(get_rand_st(n),comp_att_pairs)
        con_pairs = comp_att_pairs(state)
        if con_pairs==0:
            final_state=state
            break
    '''print("finale"+str(final_state))'''
    return final_state
