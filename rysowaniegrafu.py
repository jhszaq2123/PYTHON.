def convert_to_dot(graph_type, edges):
    if graph_type in {'d', 'dw'}:
        dot_graph = "digraph {\n"
        connector = "->"
    else:
        dot_graph = "graph {\n"
        connector = "--"
    
    for edge in edges:
        if len(edge) == 2:  
            dot_graph += f"  {edge[0]} {connector} {edge[1]};\n"
        elif len(edge) == 3: 
            dot_graph += f"  {edge[0]} {connector} {edge[1]} [label = {edge[2]}];\n"
    
    dot_graph += "}"
    return dot_graph


def main():
    t = int(input())
    results = []
    
    for _ in range(t):
        graph_type = input().strip()
        n = int(input().strip())
        
        edges = []
        for _ in range(n):
            edge_data = input().strip().split()
            if len(edge_data) == 2:
                edges.append((edge_data[0], edge_data[1]))
            elif len(edge_data) == 3:
                edges.append((edge_data[0], edge_data[1], edge_data[2]))
        
        dot_output = convert_to_dot(graph_type, edges)
        results.append(dot_output)
    
    for result in results:
        print(result)
        print()

if __name__ == "__main__":
    main()
