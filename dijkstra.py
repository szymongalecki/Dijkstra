"""
Minimal implementation of Dijkstra's algorithm

sources:
https://www.youtube.com/watch?v=_lHSawdgXpI
Algorithm Design - Jon Kleinberg and Eva Tardos
"""

graph = {
    "s": {"u": 1, "v": 2, "x": 4},
    "u": {"y": 3, "x": 1},
    "v": {"x": 2, "z": 3},
    "x": {"z": 2, "y": 1},
    "y": {},
    "z": {},
}


def dijkstra(graph: dict, start: str) -> dict:
    # S - visited nodes,
    # V - all nodes,
    # D - node: distance from start to node
    S = set()
    V = set(graph.keys())
    D = {node: float("+inf") for node in graph.keys()}
    D[start] = 0

    # until all nodes are visited,
    # pick the unvisited node with the smallest distance from the start,
    # update distances of nodes that can be reached from this node
    while S != V:
        node = min(V - S, key=lambda n: D[n])
        dist = D[node]
        S.add(node)
        for n, d in graph[node].items():
            D[n] = min(D[n], dist + d)
        print(f"(Node, Distace) : ({node}, {dist})\nDistances : {D}\n")
    return D


# distance from 's' to 'z'
print(dijkstra(graph, "s")["z"])
