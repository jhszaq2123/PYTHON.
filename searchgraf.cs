using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        // Read the entire input at once
        var input = Console.In.ReadToEnd();
        var lines = input.Split(new[] { '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries);
        int t = int.Parse(lines[0]); // Number of test cases
        int lineIndex = 1;
        var output = new List<string>();

        for (int caseNumber = 1; caseNumber <= t; caseNumber++)
        {
            output.Add($"graph {caseNumber}");

            // Number of vertices
            int n = int.Parse(lines[lineIndex]);
            lineIndex++;

            // Adjacency list representation of the graph
            var graph = new Dictionary<int, List<int>>();

            for (int i = 0; i < n; i++)
            {
                var parts = lines[lineIndex].Split().Select(int.Parse).ToArray();
                int vertex = parts[0];
                int neighborsCount = parts[1];
                graph[vertex] = parts.Skip(2).ToList();
                lineIndex++;
            }

            // Process queries
            while (true)
            {
                var query = lines[lineIndex].Split().Select(int.Parse).ToArray();
                lineIndex++;
                if (query[0] == 0 && query[1] == 0)
                    break;

                int startVertex = query[0];
                int method = query[1];

                if (method == 0)
                {
                    // DFS
                    var result = DFS(graph, startVertex);
                    output.Add(string.Join(" ", result));
                }
                else
                {
                    // BFS
                    var result = BFS(graph, startVertex);
                    output.Add(string.Join(" ", result));
                }
            }
        }

        // Print the output
        Console.WriteLine(string.Join("\n", output));
    }

    // Depth-First Search (DFS)
    static List<int> DFS(Dictionary<int, List<int>> graph, int start)
    {
        var visited = new HashSet<int>();
        var result = new List<int>();

        void Explore(int node)
        {
            visited.Add(node);
            result.Add(node);

            foreach (var neighbor in graph[node].OrderBy(x => x))
            {
                if (!visited.Contains(neighbor))
                {
                    Explore(neighbor);
                }
            }
        }

        Explore(start);
        return result;
    }

    // Breadth-First Search (BFS)
    static List<int> BFS(Dictionary<int, List<int>> graph, int start)
    {
        var visited = new HashSet<int>();
        var queue = new Queue<int>();
        var result = new List<int>();

        queue.Enqueue(start);
        visited.Add(start);

        while (queue.Count > 0)
        {
            int node = queue.Dequeue();
            result.Add(node);

            foreach (var neighbor in graph[node].OrderBy(x => x))
            {
                if (!visited.Contains(neighbor))
                {
                    visited.Add(neighbor);
                    queue.Enqueue(neighbor);
                }
            }
        }

        return result;
    }
}
