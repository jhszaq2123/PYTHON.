from collections import defaultdict, deque

def dfs(graph, start):
    visited = set()
    result = []

    def explore(node):
        visited.add(node)
        result.append(node)
        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                explore(neighbor)

    explore(start)
    return result


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    visited.add(start)

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def process_input():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])  
    idx = 1
    output = []

    for graph_index in range(1, t + 1):
        output.append(f"graph {graph_index}")

        n = int(data[idx])
        idx += 1

        graph = defaultdict(list)
        for _ in range(n):
            line = list(map(int, data[idx].split()))
            vertex = line[0]
            neighbors = line[2:] 
            graph[vertex] = neighbors
            idx += 1

        while True:
            query = list(map(int, data[idx].split()))
            idx += 1
            if query == [0, 0]:  
                break

            start_vertex, method = query
            if method == 0:
                result = dfs(graph, start_vertex)
            else:
                result = bfs(graph, start_vertex)

            output.append(" ".join(map(str, result)))

    print("\n".join(output))


if __name__ == "__main__":
    process_input()
