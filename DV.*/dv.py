def distance_vector_algorithm(N, M, edges, S, T):
    # Initialize distance array with infinity
    dist = [float("inf")] * N
    dist[S - 1] = 0

    print(f"Initial distances: {dist}")

    # Repeat the relaxation process N-1 times
    for i in range(N - 1):
        print(f"Iteration {i+1}")
        for u, v, w in edges:
            if dist[u - 1] + w < dist[v - 1]:
                dist[v - 1] = dist[u - 1] + w
                print(f"Updated dist[{v}] to {dist[v - 1]} using edge ({u}, {v}) with weight {w}")
        print(f"Distances after iteration {i+1}: {dist}")

    # Check for negative weight cycles
    for u, v, w in edges:
        if dist[u - 1] + w < dist[v - 1]:
            print("Graph contains a negative weight cycle")
            return None

    # Return the shortest distance to the target
    return dist[T - 1]

if __name__ == "__main__":
    # Reading input
    N, M = map(int, input("Enter number of nodes and edges:\n").split())
    edges = []
    print("Enter the edges (x y z):")
    for _ in range(M):
        x, y, z = map(int, input().split())
        edges.append((x, y, z))
    S, T = map(int, input("Enter the source and target nodes:\n").split())

    # Calculate shortest distance using Distance Vector Algorithm
    shortest_distance = distance_vector_algorithm(N, M, edges, S, T)

    # Output the result
    if shortest_distance is not None:
        print(f"Shortest distance from router {S} to router {T}: {shortest_distance}")

