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
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    prev = {node: None for node in graph}
    pq = HeapPQ()
    run_dijkstras(graph, distances, prev, pq)
    total_cost = distances[target]
    path = get_path(source, target, prev)
    return path, total_cost

class BasePQ:
    def push(self, item, priority):
        raise NotImplementedError()
    
    def pop(self):
        raise NotImplementedError()
    
    def is_empty(self) -> bool:
        raise NotImplementedError()
    
    def update_priority(self, item, priority):
        raise NotImplementedError()

class LinearPQ(BasePQ):
    def __init__(self):
        self.elements: list[tuple[str, str]] = []
    
    def push(self, item, priority):
        for i, element in enumerate(self.elements):
            if element[1] > priority:
                self.elements.insert(i, (item, priority))
                return
        self.elements.append((item, priority))

    def pop(self):
        if self.elements:
            return self.elements.pop(0)[0]
        raise ValueError("No Elements in the PQ")
    
    def is_empty(self) -> bool:
        return len(self.elements) == 0
    
    def update_priority(self, item, priority):
        for i, element in enumerate(self.elements):
            if element[0] == item:
                del self.elements[i]
                break
        for i, element in enumerate(self.elements):
            if element[1] > priority:
                self.elements.insert(i, (item, priority))
                break

class HeapPQ(BasePQ):
    def __init__(self):
        self.elements: list[tuple[int, float]] = []
        self.reference: dict[int, int] = {}
        self.pop_count = 0

    def is_empty(self) -> bool:
        return len(self.elements) == 0

    def push(self, item, priority):
        self.elements.append((item, priority))
        last_index = len(self.elements) - 1
        self.reference[item] = last_index
        self._percolate_up(last_index)

    def pop(self):
        last_index = len(self.elements) - 1
        if last_index < 0:
            raise ValueError("No Elements in the PQ")
        self._swap(0, last_index)
        item, priority = self.elements.pop()
        self._percolate_down()
        self.pop_count += 1
        del self.reference[item]
        return item

    def update_priority(self, item, priority):
        index = self.reference[item - self.pop_count]
        self.elements[index] = (item, priority)
        self._percolate_up(index)

    def _percolate_down(self):
        index = 0
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2
        while left_child < len(self.elements):
            smallest = self._get_smallest_child(left_child, right_child)
            if self.elements[index][1] > self.elements[smallest][1]:
                self._swap(index, smallest)
                index = smallest
                left_child = (2 * index) + 1
                right_child = (2 * index) + 2
            else:
                break

    def _get_smallest_child(self, left_child, right_child):
        if right_child >= len(self.elements):
            return left_child
        if self.elements[left_child][1] < self.elements[right_child][1]:
            return left_child
        return right_child

    def _swap(self, i, j):
        self.elements[i], self.elements[j] = self.elements[j], self.elements[i]
        self.reference[self.elements[i][0]] = i
        self.reference[self.elements[j][0]] = j

    def _percolate_up(self, index: int):
        index = index
        while index > 0:
            parent = ((index + 1) // 2) - 1
            if self.elements[index][1] < self.elements[parent][1]:
                self._swap(index, parent)
                index = parent
            else:
                break

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
    pq = LinearPQ()
    run_dijkstras(graph, distances, prev, pq)
    total_cost = distances[target]
    path = get_path(source, target, prev)
    return path, total_cost

def get_path(source, target, prev):
    path = []
    traversal_node = target
    while traversal_node is not None:
        path.append(traversal_node)
        traversal_node = prev[traversal_node]
    path.reverse()
    if len(path) == 1 and path[0] != source:
        path = []
    return path

def run_dijkstras(graph, distances, prev, pq: BasePQ):
    for node, distance in distances.items():
        pq.push(node, distance)
    while not pq.is_empty():
        u = pq.pop()
        for v, cost in graph[u].items():
            if distances[v] > distances[u] + cost:
                distances[v] = distances[u] + cost
                prev[v] = u
                pq.update_priority(v, distances[v])
