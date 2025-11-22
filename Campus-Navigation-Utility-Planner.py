import heapq
from collections import defaultdict

# BUILDING TREE (BST)
class BuildingNode:
    def __init__(self, bid, name, details):
        self.bid = bid
        self.name = name
        self.details = details
        self.left = None
        self.right = None

class BuildingTree:
    def __init__(self):
        self.root = None

    def insert(self, root, node):
        if not root:
            return node
        if node.bid < root.bid:
            root.left = self.insert(root.left, node)
        else:
            root.right = self.insert(root.right, node)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"{root.bid}: {root.name} - {root.details}")
            self.inorder(root.right)

# GRAPH FOR CAMPUS PATHS
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    # Dijkstra Algorithm
    def dijkstra(self, start):
        dist = {node: float('inf') for node in self.graph}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, node = heapq.heappop(pq)
            for nxt, w in self.graph[node]:
                if dist[nxt] > d + w:
                    dist[nxt] = d + w
                    heapq.heappush(pq, (dist[nxt], nxt))
        return dist

    # Kruskal MST
    def kruskal(self):
        edges = []
        for u in self.graph:
            for v, w in self.graph[u]:
                if (v, u, w) not in edges:
                    edges.append((u, v, w))

        edges.sort(key=lambda x: x[2])
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        for node in self.graph:
            parent[node] = node

        mst = []
        for u, v, w in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, w))

        return mst

class ExprNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def evalExprTree(root):
    if not root.left and not root.right:
        return int(root.val)
    left = evalExprTree(root.left)
    right = evalExprTree(root.right)
    if root.val == '+': return left + right
    if root.val == '-': return left - right
    if root.val == '*': return left * right
    if root.val == '/': return left / right

if __name__ == "__main__":

    print("\n--- Building Tree (BST Traversal) ---")
    bt = BuildingTree()
    bt.root = bt.insert(None, BuildingNode(2, "Library", "Central Campus"))
    bt.insert(bt.root, BuildingNode(1, "Admin Block", "North Wing"))
    bt.insert(bt.root, BuildingNode(3, "Hostel", "South Wing"))
    bt.inorder(bt.root)

    print("\n--- Campus Graph (Dijkstra Shortest Path) ---")
    g = Graph()
    g.addEdge("A", "B", 4)
    g.addEdge("A", "C", 2)
    g.addEdge("B", "D", 7)
    g.addEdge("C", "D", 1)
    print("Shortest distances from A:", g.dijkstra("A"))

    print("\n--- Utility Layout (Kruskal MST) ---")
    print("MST Edges:", g.kruskal())

    print("\n--- Expression Tree (Energy Bill Calculator) ---")
    root = ExprNode('*')
    root.left = ExprNode('+')
    root.right = ExprNode('3')
    root.left.left = ExprNode('5')
    root.left.right = ExprNode('2')
    print("Energy Cost:", evalExprTree(root))
