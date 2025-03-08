import sys
sys.setrecursionlimit(10000)

def dfs(graph, node, parent):
    farthest_node = node
    max_distance = 0

    for neighbor in graph[node]:
        if neighbor != parent:
            dist, farthest = dfs(graph, neighbor, node)
            dist += 1  # Add the edge between the current node and the neighbor
            if dist > max_distance:
                max_distance = dist
                farthest_node = farthest

    return max_distance, farthest_node

def main():
    N = int(input())
    
    # Create adjacency list for the tree
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # First DFS to find the farthest node from node 1
    _, farthest_node = dfs(graph, 1, -1)
    
    # Second DFS from the farthest node found
    max_distance, _ = dfs(graph, farthest_node, -1)
    
    print(max_distance)

if __name__ == "__main__":
    main()
