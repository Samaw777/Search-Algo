
#DFS
graph = {
    'S': ['D', 'E', 'P'],
    'D': ['B', 'C', 'E'],
    'E': ['R', 'H'],
    'P': ['Q'],
    'B': ['A'],
    'C': [],
    'R': ['F'],
    'H': ['Q'],
    'Q': [],
    'A': [],
    'F': ['G']
}

def DFS_SEARCH(graph, start, goal):
    seen = set()
    array = [(start, [start])]
    fringes = {start: [start]}
    while array:
        (node, path) = array.pop()
        if node not in seen:
            if node == goal:
                return path, fringes
            seen.add(node)
            for neighbornode in graph[node]:
                array.append((neighbornode, path + [neighbornode]))
                if neighbornode not in fringes:
                    fringes[neighbornode] = path + [neighbornode]
    return None, fringes

goal = 'G'
start = 'S'
path, fringes = DFS_SEARCH(graph, start, goal)
if path:
    print("Final Path:", path)
else:
    print(f"Path not found from {start} to {goal}.")

print("All the Fringes to the final path:")
for key, value in fringes.items():
    print(key, ":", value)


#BFS

graph = {
    'S': ['D', 'E', 'P'],
    'D': ['B', 'C', 'E'],
    'E': ['R', 'H'],
    'P': ['Q'],
    'B': ['A'],
    'C': [],
    'R': ['F'],
    'H': ['Q'],
    'Q': [],
    'A': [],
    'F': ['G']
}

def searchbfs(graph, start, goal):
    seen = set()
    arrayqueue = [(start, [start])]
    AllFringes = {start: [start]}
    while arrayqueue:
        (vertex, path) = arrayqueue.pop(0)
        if vertex not in seen:
            if vertex == goal:
                return path, AllFringes
            seen.add(vertex)
            for neighbor in graph[vertex]:
                arrayqueue.append((neighbor, path + [neighbor]))
                if neighbor not in AllFringes:
                    AllFringes[neighbor] = path + [neighbor]
    return None, AllFringes

goal = 'G'
start = 'S'
path, AllFringes = searchbfs(graph, start, goal)
if path:
    print("Final Path:", path)
else:
    print(f"Path not found from {start} to {goal}.")

print("Fringes:")
for key, value in AllFringes.items():
    print(key, ":", value)
