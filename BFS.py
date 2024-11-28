from collections import deque

def bfs(graph, source):
    q = deque([source])
    visited = set()
    visited.add(source)
    while q:
        node = q.popleft()
        print(f"Visited {node}")
        for n in graph[node]:
            if n not in visited:
                q.append(n)
                visited.add(n)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bfs(graph, 'A')