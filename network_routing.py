def find_shortest_path_with_heap(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the heap-based algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """

class linear_pq():
    def __init__(self):
        self.elements: list[tuple[str, str]] = []
    
    def push(self, item, priority) -> bool:
        for i, element in enumerate(self.elements):
            if element[1] > priority:
                self.elements.insert(i, (item, priority))
                return True
        self.elements.append((item, priority))
        return True

    def pop(self):
        if self.elements:
            return self.elements.pop(0)[0]
        raise ValueError("No Elements in the PQ")
    
    def is_empty(self) -> bool:
        return len(self.elements) == 0
    
    def update_priority(self, item, priority) -> bool:
        for i, element in enumerate(self.elements):
            if element[0] == item:
                del self.elements[i]
                break
        for i, element in enumerate(self.elements):
            if element[1] > priority:
                self.elements.insert(i, (item, priority))
                break
        return True


def find_shortest_path_with_linear_pq(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the array-based (linear lookup) algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    prev = {node: None for node in graph}
    pq = linear_pq()
    for node, distance in distances.items():
        pq.push(node, distance)
    while not pq.is_empty():
        u = pq.pop()
        for v, cost in graph[u].items():
            if distances[v] > distances[u] + cost:
                distances[v] = distances[u] + cost
                prev[v] = u
                pq.update_priority(v, distances[v])
    total_cost = distances[target]
    path = []
    traversal_node = target
    while traversal_node is not None:
        path.append(traversal_node)
        traversal_node = prev[traversal_node]
    path.reverse()
    if len(path) == 1 and path[0] != source:
        path = []
    return path, total_cost
