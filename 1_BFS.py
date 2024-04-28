from queue import Queue

def BFS():
    if q.empty():
        return
    v = q.get()
    print(" -->",v,end="")
    visited[v] = 1
    for i in range(n):
        if not visited[i] and graph[v][i]==1:
            q.put(i) 
    BFS()


n = int(input("Enter number of vertices: "))
graph = [[0 for i in range(n)] for i in range (n)]

for i in range(n):
    for j in range(i+1,n):
        graph[i][j] = int(input(f"Enter 1 if edge is present in between graph[{i}][{j}]"))
        graph[j][i] = graph[i][j]

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print("\n")

visited = n * [0]
q = Queue()
q.put(0)
BFS()