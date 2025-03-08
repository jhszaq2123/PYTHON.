import heapq
import sys

# Dijkstra's algorithm to find the shortest path
def dijkstra(n, graph, start, end):
    # Initialize distances as infinity
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    
    # Min-heap priority queue (distance, node)
    pq = [(0, start)]  # (distance, node)
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if current_dist > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    # Return the shortest distance to the destination city
    return dist[end] if dist[end] != float('inf') else 'NONE'

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    t = int(data[idx])  # Number of test cases
    idx += 1
    results = []
    
    for _ in range(t):
        # Read number of cities, number of highways, start city, end city
        n, m, start, end = map(int, data[idx].split())
        idx += 1
        
        # Initialize the graph
        graph = [[] for _ in range(n + 1)]
        
        # Read the highways
        for _ in range(m):
            u, v, time = map(int, data[idx].split())
            graph[u].append((v, time))
            graph[v].append((u, time))
            idx += 1
        
        # Apply Dijkstra's algorithm to find the shortest path
        result = dijkstra(n, graph, start, end)
        results.append(str(result))
    
    # Output all results
    print("\n".join(results))

if __name__ == "__main__":
    main()
