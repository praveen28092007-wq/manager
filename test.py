from collections import deque 
graph = {} 
n = int(input("Enter number of nodes: ")) 
for i in range(n): 
    node = input("Enter node: ") 
    neighbours = input("Enter neighbours: ").split() 
    graph[node] = neighbours 
start = input("Enter starting node: ") 
def bfs(start): 
    queue = deque() 
    visited = [] 
    queue.append(start) 
    while queue: 
        node = queue.popleft() 
        if node not in visited: 
            visited.append(node) 
            print(node, end=" ") 
            for neighbour in graph[node]: 
                queue.append(neighbour) 
def dfs(node, visited): 
if node not in visited: 
    visited.append(node) 
    print(node, end=" ") 
for neighbour in graph[node]: 
dfs(neighbour, visited) 
print("BFS:") 
bfs(start) 
print("\nDFS:") 
dfs(start, []) 