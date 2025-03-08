class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

def ip_to_tuple(ip):
    return tuple(map(int, ip.split('.')))

def main():
    uf = UnionFind()

    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()

    for line in data:
        parts = line.split()
        if parts[0] == 'B':
            ip1 = ip_to_tuple(parts[1])
            ip2 = ip_to_tuple(parts[2])

            uf.add(ip1)
            uf.add(ip2)

            uf.union(ip1, ip2)
        elif parts[0] == 'T':
            ip1 = ip_to_tuple(parts[1])
            ip2 = ip_to_tuple(parts[2])

            uf.add(ip1)
            uf.add(ip2)

            if uf.find(ip1) == uf.find(ip2):
                print("T")
            else:
                print("N")

if __name__ == "__main__":
    main()
