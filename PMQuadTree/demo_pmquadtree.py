from pmquadtree import PMQuadTree, Point
import random

def check_node_capacity(quadtree, capacity):
    def traverse(node):
        if node is None:
            return
        total_items = len(node.points) + len(node.edges)
        if total_items > capacity:
            print(f"Node at boundary {node.boundary} exceeds capacity with {len(node.points)} points and {len(node.edges)} edges.")
        for child in node.children:
            traverse(child)
    traverse(quadtree.root)

def main():
    # Define a smaller boundary for the QuadTree (x_min, y_min, x_max, y_max)
    boundary = [0, 0, 100, 100]
    quadtree = PMQuadTree(boundary, capacity_points=4, capacity_edges=15)  # Correct parameter names

    # Case 1: Adding more points
    print("Case 1: Adding points...")
    points = []
    for i in range(20):  # Increase to 20 points
        x, y = random.randint(0, 100), random.randint(0, 100)
        data = f"Point-{i}"
        quadtree.add(x, y, data)
        points.append((x, y, data))
    quadtree.visualize(title="Case 1: Adding Points")
    print("\n")

    # Case 2: Adding more edges
    print("Case 2: Adding edges...")
    point_objects = [quadtree.search(x, y) for x, y, _ in points]
    point_objects = [p for p in point_objects if p is not None]  # Filter out None values
    for _ in range(15):  # Increase to 15 random edges
        if len(point_objects) >= 2:
            p1, p2 = random.sample(point_objects, 2)
            quadtree.addEdge(p1, p2)
    quadtree.visualize(title="Case 2: Adding Edges")
    print("\n")

    # Case 3: Performing a small range query
    print("Case 3: Performing range query for points within (20, 20, 80, 80)...")
    points_in_range, edges_in_range = quadtree.range_query(20, 20, 80, 80)
    print("Points in range:")
    for point in points_in_range:
        print(f"({point.x}, {point.y}) - {point.data}")
    print("Edges in range:")
    for edge in edges_in_range:
        print(f"(({edge[0].x}, {edge[0].y}) -> ({edge[1].x}, {edge[1].y}))")
    quadtree.visualize(title="Case 3: Range Query")
    print("\n")

    # Case 4: Adding points and edges to reach maximum density
    print("Case 4: Adding points and edges to reach maximum density...")
    points = []
    for i in range(20):  # Add 20 more points to trigger splits
        x, y = random.randint(0, 100), random.randint(0, 100)
        data = f"Point-{20 + i}"
        quadtree.add(x, y, data)
        points.append(Point(x, y, data))

    # Add edges between random points
    for _ in range(10):  # Add 10 random edges
        if len(points) >= 2:
            p1, p2 = random.sample(points, 2)
            quadtree.addEdge(p1, p2)

    quadtree.visualize(title="Case 4: Maximum Density with Points and Edges")
    print("\n")

    # Case 5: Adding edges that cause splitting without nodes in subplots
    print("Case 5: Adding edges that cause splitting without nodes...")
    edge_points = [
        Point(10, 10, "EdgePoint1"),
        Point(90, 10, "EdgePoint2"),
        Point(10, 90, "EdgePoint3"),
        Point(90, 90, "EdgePoint4"),
    ]
    for point in edge_points:
        quadtree.add(point.x, point.y, point.data)

    edges = [
        (edge_points[0], edge_points[1]),  # Horizontal edge
        (edge_points[2], edge_points[3]),  # Horizontal edge
        (edge_points[0], edge_points[2]),  # Vertical edge
        (edge_points[1], edge_points[3]),  # Vertical edge
    ]
    for p1, p2 in edges:
        quadtree.addEdge(p1, p2)
    quadtree.visualize(title="Case 5: Edges Causing Splitting")
    print("\n")

    # Case 6: Querying after multiple operations
    print("Case 6: Querying after multiple operations...")
    points_in_range, edges_in_range = quadtree.range_query(0, 0, 50, 50)
    print("Points in range:")
    for point in points_in_range:
        print(f"({point.x}, {point.y}) - {point.data}")
    print("Edges in range:")
    for edge in edges_in_range:
        print(f"(({edge[0].x}, {edge[0].y}) -> ({edge[1].x}, {edge[1].y}))")
    quadtree.visualize(title="Case 6: Query After Operations")
    print("\n")

    # Case 7: Testing maximum tree depth
    print("Case 7: Testing maximum tree depth...")
    for i in range(100):  # Add 100 points to ensure the tree reaches max depth
        x, y = random.randint(0, 100), random.randint(0, 100)
        data = f"Point-{i}"
        quadtree.add(x, y, data)
    quadtree.visualize(title="Case 7: Maximum Tree Depth")
    print("\n")

if __name__ == "__main__":
    main()
