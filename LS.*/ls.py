import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        print(f"Graph initialized with {vertices} vertices.")
        print(f"Enter the edge and weights:")

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
        print(f"Edge added between {u} and {v} with weight {w}.")

    def dijkstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        pq = [(0, src)]
        print(f"Initial distances: {dist}")
        print(f"Initial priority queue: {pq}")

        while pq:
            d, u = heapq.heappop(pq)
            print(f"Popped node {u} with distance {d} from the priority queue.")
            if d > dist[u]:
              print(f"Current distance {d} is greater than known distance {dist[u]} for node {u}, skipping.")
              continue

            for v, w in self.graph[u]:
              print(f"Checking node {v} from node {u} with edge weight {w}.")
              if dist[u] + w < dist[v]:
                  dist[v] = dist[u] + w
                  heapq.heappush(pq, (dist[v], v))
                  print(f"Updated distance for node {v} to {dist[v]}.")
                  print(f"Priority queue updated: {pq}")

        print(f"Final distances: {dist}")
        return dist

if __name__ == "__main__":
    N, M = map(int, input("Enter number of vertices and edges:\n").split())
    graph = Graph(N)

    for _ in range(M):
        x, y, z = map(int, input().split())
        graph.add_edge(x - 1, y - 1, z)

    S = int(input("Enter the source vertex (router): "))
    print(f"Calculating shortest paths from source {S - 1}.")
    shortest_distances = graph.dijkstra(S - 1)

    print("Shortest distances from source router to all routers:")
    for i in range(N):
        print(f"Router {i + 1} (node {i}): {shortest_distances[i]}")


