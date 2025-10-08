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

class linear_pq:
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
            if element[1] > priority:
                self.elements.insert(i, (item, priority))
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
