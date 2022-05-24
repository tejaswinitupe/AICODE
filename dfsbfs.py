# Using a Python dictionary to act as an adjacency list
graph = {
'1' : ['2','3','4'],
'3' : ['1', '2','5'],
 '2' : ['1','3'],
 '4' : ['1'],
 '5' : ['3']
}
visited = set() # Set to keep track of visited nodes of graph.
def dfs(visited, graph, node): #function for dfs 
 if node not in visited:
    print(node,end="->")
    visited.add(node)
    for neighbour in graph[node]:
        dfs(visited, graph, neighbour)
# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '1')
print("\n")
visited = [] # List for visited nodes.
queue = []  #Initialize a queue
def bfs(visited, graph, node): #function for BFS
    visited.append(node)
    queue.append(node)
    while queue:# Creating loop to visit each node
        m = queue.pop(0) 
        print (m, end = "-> ") 
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5') # function calling