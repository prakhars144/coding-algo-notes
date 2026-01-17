# Breadth-First Search (BFS)

BFS is a graph traversal algorithm that explores all vertices at the current depth level before moving to the next depth level.

## How it Works

1. Start from a source node
2. Visit all its neighbors
3. Then visit neighbors of neighbors, and so on

## Implementation

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## Time Complexity

O(V + E) where V is vertices and E is edges.

## Applications

- Shortest path in unweighted graphs
- Finding connected components
- Level-order traversal in trees