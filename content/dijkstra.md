---
title: "Dijkstra Algorithm – Complete Notes"
description: "Comprehensive notes on Dijkstra's shortest path algorithm"
type: docs
---

# 📘 Dijkstra Algorithm – Complete Notes

---

## 1. Core Idea

**Dijkstra = BFS for Weighted Graphs**

* Finds shortest path from a source node to all other nodes
* Works only for **non-negative edge weights**
* Greedy algorithm

### Golden Rule

> Always expand the currently closest unvisited node first.

---

## 2. When to Use Dijkstra

Use when problem asks for:

* Shortest path
* Minimum cost
* Cheapest route
* Minimum effort
* Fastest way

**ONLY if weights are non-negative**

---

## 3. Data Structures Required

To implement efficiently:

* **Distance Array** → stores best known distance
* **Min Heap / Priority Queue** → to pick nearest node quickly
* **Adjacency List** → graph representation

---

## 4. Algorithm Steps (High Level)

1. Set distance[source] = 0
   Others = ∞
2. Push (0, source) into min heap
3. While heap not empty:

   * Pop node with smallest distance
   * Relax all its outgoing edges
4. Repeat until all nodes processed

---

## 5. Python Implementation (Standard)

```python
import heapq

def dijkstra(n, edges, source):
    dist = [float('inf')] * n
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > dist[node]:
            continue

        for neighbor, weight in edges[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist
```

---

## 6. MOST IMPORTANT LINE

```python
if current_dist > dist[node]:
    continue
```

### Why?

* A node can appear multiple times in heap
* This skips outdated entries
* Makes algorithm efficient

---

# 7. Time Complexity Breakdown

### Final Complexity

**👉 O((V + E) log V)**

---

### How We Derive It

#### Operations involved:

* `heappop` → called at most V times
* `heappush` → at most E times

| Operation | Count | Cost  | Total   |
| --------- | ----- | ----- | ------- |
| heappop   | V     | log V | V log V |
| heappush  | E     | log V | E log V |

Total:

```
O(V log V + E log V)
= O((V + E) log V)
```

---

### Why log V and not log E?

* Heap size never exceeds V
* So each operation is O(log V)

---

## 8. Theoretical Improvement

### Using Fibonacci Heap

Operation costs:

* decrease-key → O(1)
* insert → O(1)
* extract-min → O(log V)

This improves Dijkstra to:

👉 **O(E + V log V)**

---

### BUT in practice:

* Fibonacci heaps are complex
* Not used in CP or interviews
* Binary heap is standard

---

## 9. Interview Answer Guide

If asked:

> "What is the time complexity of Dijkstra?"

### Correct Default Answer:

**O((V + E) log V)**
(using binary heap)

---

If asked:

> "Can it be improved?"

Then answer:

> Yes, with Fibonacci heap it becomes **O(E + V log V)**

---

## 10. When Dijkstra DOES NOT Work

Fails if graph has:

❌ Negative edge weights

Use instead:

👉 **Bellman-Ford Algorithm**

---

# 11. Handling Input Format (u, v, w)

Most problems give edges as:

```
(u, v, w)
```

This is NOT directly usable.

---

### You must build an adjacency list

```python
def build_graph(n, edge_list):
    edges = {i: [] for i in range(n)}

    for u, v, w in edge_list:
        edges[u].append((v, w))   # directed

    return edges
```

---

### Then Dijkstra loop works:

```python
for neighbor, weight in edges[node]:
    new_dist = current_dist + weight
```

---

## 12. Directed vs Undirected

### Directed Graph

```python
edges[u].append((v, w))
```

### Undirected Graph

```python
edges[u].append((v, w))
edges[v].append((u, w))
```

---

# 13. Overall Workflow

Given input edges `(ui, vi, wi)`:

1. Convert to adjacency list
2. Run Dijkstra using heap
3. Get shortest distances

---

# 14. Pattern to Remember Forever

```
Initialize distances  
Push source to heap  

while heap not empty:
    pop smallest  
    relax neighbors
```

---

# 15. Must-Solve LeetCode Problems

### Easy

* 743 – Network Delay Time
* 1631 – Path With Minimum Effort

### Medium

* 1514 – Path with Maximum Probability
* 787 – Cheapest Flights Within K Stops
* 1976 – Number of Ways to Arrive at Destination
* 1334 – Find the City With the Smallest Number of Neighbors

### Hard

* 882 – Reachable Nodes in Subdivided Graph
* 2093 – Minimum Cost with Discounts
* 2577 – Minimum Time to Visit a Cell in a Grid

---

# 16. Key Takeaways

* Dijkstra = greedy + priority queue
* Needs adjacency list
* Works only for non-negative weights
* Standard complexity: **O((V + E) log V)**
* Theoretical best: **O(E + V log V)**

---

## Final Memory Hook

> **"Greedy BFS with a Min Heap"**

Remember this and you'll never forget Dijkstra 😄