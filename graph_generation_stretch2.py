import random
import math

def get_point_plane(width, height, size):
    plane = []
    for i in range(size):
        point = random.uniform(0, width), random.uniform(0, height)
        plane.append(point)
    return plane

def get_plane_based_graph(seed: int, size: int, density: float, 
                          noise: float, width=1000, height=1000) -> \
                          tuple[dict[int, dict[int, float]], list[tuple[float, float]]]:
    random.seed(seed)
    threshold = density * math.dist((0, 0), (width, height))

    point_plane = get_point_plane(width, height, size)
    graph: dict[int, dict[int, float]] = {i: {} for i in range(size)}
    for i in range(size):
        for j in range(size):
            if i != j:
                distance = math.dist(point_plane[i], point_plane[j])
                modified_distance = max(0.0, distance + random.normalvariate(mu=0, sigma=noise))
                if distance <= threshold:
                    graph[i][j] = modified_distance
    return graph, point_plane