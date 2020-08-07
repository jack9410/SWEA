import os
import sys
curr_dir = os.path.dirname(__file__)
sys.stdin = open(curr_dir + '\input.txt', 'r')


from collections import deque
def dfs(idx):
    for i in graph[idx]:
        if i == 99:
            return True
        dq.insert(0,i)
    print(dq)
    dfs(dq.popleft())
    

for _ in range(1,11):

    t_case, edge_num = map(int, input().split())
    # print(t_case, edge_num)
    
    graph = [[]for _ in range(100) ]
    # print(graph)

    edges = list(map(int, input().split()))
    # print(edges)

    for i in range(len(edges)//2):
        start = edges[i*2]
        end = edges[i*2+1]
        # print(start, end)
        graph[start].append(end)
    # print(graph)
    
    dq= deque()
    if dfs(0):
        answer = 1
    else:
        answer = 0

    print('#{} {}'.format(t_case, answer))