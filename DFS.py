def dfs(graph, source):
    stack = [source]
    visited = set()
    visited.add(source)
    while stack:
        node = stack.pop()
        print(f"Visited {node}")
        for n in graph[node]:
            if n not in visited:
                stack.append(n)
                visited.add(n)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
dfs(graph, 'A')