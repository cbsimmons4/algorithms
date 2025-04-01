from math import sqrt
from collections import defaultdict, deque
import matplotlib.pyplot as plt

# Constants
DEFAULT_CAPACITY_POINTS = 8  # Updated maximum number of points per QuadTree node
DEFAULT_CAPACITY_EDGES = 15  # Default maximum number of edges per QuadTree node
VISUALIZATION_FIGSIZE = (10, 10)  # Default figure size for visualization
MAX_DEPTH = 5  # Maximum depth of the quadtree

class Point:
    def __init__(self, x, y, data=None):
        # Initialize a point with x, y coordinates and optional data
        self.x = x
        self.y = y
        self.data = data


class QuadTreeNode:
    def __init__(self, boundary, capacity_points=DEFAULT_CAPACITY_POINTS, capacity_edges=DEFAULT_CAPACITY_EDGES, depth=0):
        # Initialize a QuadTreeNode with a boundary, point capacity, edge capacity, and depth
        self.boundary = boundary  # [x_min, y_min, x_max, y_max]
        self.capacity_points = capacity_points
        self.capacity_edges = capacity_edges
        self.depth = depth  # Current depth of this node
        self.points = []  # Points stored in this node
        self.edges = []  # Edges stored in this node (as tuples of points)
        self.divided = False  # Flag to check if the node is subdivided
        self.high_density = False  # Flag to indicate high-density nodes
        self.children = []  # [NW, NE, SW, SE]

    def subdivide(self):
        # Subdivide the node into four children
        if self.high_density or self.depth >= MAX_DEPTH:
            return  # Prevent subdivision if the node is marked as high-density or max depth is reached

        x_min, y_min, x_max, y_max = self.boundary
        mid_x = (x_min + x_max) / 2
        mid_y = (y_min + y_max) / 2

        self.children = [
            QuadTreeNode([x_min, y_min, mid_x, mid_y], self.capacity_points, self.capacity_edges, self.depth + 1),  # NW
            QuadTreeNode([mid_x, y_min, x_max, mid_y], self.capacity_points, self.capacity_edges, self.depth + 1),  # NE
            QuadTreeNode([x_min, mid_y, mid_x, y_max], self.capacity_points, self.capacity_edges, self.depth + 1),  # SW
            QuadTreeNode([mid_x, mid_y, x_max, y_max], self.capacity_points, self.capacity_edges, self.depth + 1),  # SE
        ]
        self.divided = True

        # Reassign points to children
        points_to_reassign = self.points[:]
        self.points = []  # Clear points from the current node
        for point in points_to_reassign:
            for child in self.children:
                if child.insert(point):
                    break

        # Reassign edges to all intersecting children
        edges_to_reassign = self.edges[:]
        self.edges = []  # Clear edges from the current node
        for edge in edges_to_reassign:
            for child in self.children:
                if child._edge_in_boundary(edge):
                    if edge not in child.edges:  # Avoid redundant insertion
                        child.insert_edge(edge)

    def insert(self, point):
        # Insert a point into the QuadTreeNode
        if not self._in_boundary(point):
            return False

        if self.high_density or len(self.points) < self.capacity_points or self.depth >= MAX_DEPTH:
            self.points.append(point)  # Directly store in high-density nodes or if max depth is reached
            return True

        if not self.divided:
            self.subdivide()

        for child in self.children:
            if child.insert(point):
                return True

        return False  # Fallback if no child accepts the point

    def insert_edge(self, edge, visited=None):
        # Insert an edge into the QuadTreeNode
        if visited is None:
            visited = set()

        # Prevent infinite recursion by tracking visited nodes
        if id(self) in visited:
            return False
        visited.add(id(self))

        if not self._edge_in_boundary(edge):
            return False

        if self.high_density or len(self.edges) < self.capacity_edges or self.depth >= MAX_DEPTH:
            if edge not in self.edges:  # Avoid duplicate edges
                self.edges.append(edge)
            return True

        if not self.divided:
            self.subdivide()

        # Add the edge to all intersecting child nodes
        for child in self.children:
            if child._edge_in_boundary(edge):
                child.insert_edge(edge, visited)

        return True  # Successfully handled the edge

    def _in_boundary(self, point):
        # Check if a point is within the node boundary
        x_min, y_min, x_max, y_max = self.boundary
        return x_min <= point.x < x_max and y_min <= point.y < y_max

    def _edge_in_boundary(self, edge):
        # Check if an edge is within the node boundary
        x_min, y_min, x_max, y_max = self.boundary
        p1, p2 = edge
        return (
            (x_min <= p1.x < x_max and y_min <= p1.y < y_max) or
            (x_min <= p2.x < x_max and y_min <= p2.y < y_max) or
            self._edge_intersects_boundary(edge)
        )

    def _edge_intersects_boundary(self, edge):
        # Check if an edge intersects the boundary of the node
        x_min, y_min, x_max, y_max = self.boundary
        p1, p2 = edge

        def intersects(p1, p2, x1, y1, x2, y2):
            # Check if a line segment intersects a rectangle edge
            dx, dy = p2.x - p1.x, p2.y - p1.y
            if dx == 0 and dy == 0:  # Edge is a point
                return x1 <= p1.x <= x2 and y1 <= p1.y <= y2
            if dx == 0:  # Vertical line
                return x1 <= p1.x <= x2 and (y1 <= p1.y <= y2 or y1 <= p2.y <= y2)
            if dy == 0:  # Horizontal line
                return y1 <= p1.y <= y2 and (x1 <= p1.x <= x2 or x1 <= p2.x <= x2)
            # General case: Check intersection with rectangle edges
            try:
                t1 = (x1 - p1.x) / dx if dx != 0 else float('inf')
                t2 = (x2 - p1.x) / dx if dx != 0 else float('inf')
                t3 = (y1 - p1.y) / dy if dy != 0 else float('inf')
                t4 = (y2 - p1.y) / dy if dy != 0 else float('inf')
                return any(0 <= t <= 1 for t in [t1, t2, t3, t4])
            except ZeroDivisionError:
                return False  # Handle division by zero gracefully

        # Check intersection with each boundary edge
        return (
            intersects(p1, p2, x_min, y_min, x_max, y_min) or  # Bottom edge
            intersects(p1, p2, x_min, y_max, x_max, y_max) or  # Top edge
            intersects(p1, p2, x_min, y_min, x_min, y_max) or  # Left edge
            intersects(p1, p2, x_max, y_min, x_max, y_max)     # Right edge
        )

    def query_range(self, range_boundary, found_points, found_edges):
        # Query points and edges within a range
        if not self._intersects(range_boundary):
            return

        for point in self.points:
            if self._point_in_range(point, range_boundary):
                found_points.append(point)

        for edge in self.edges:
            if self._edge_in_range(edge, range_boundary):
                found_edges.append(edge)

        if self.divided:
            for child in self.children:
                child.query_range(range_boundary, found_points, found_edges)

    def _intersects(self, range_boundary):
        # Check if the range intersects with the node boundary
        x_min, y_min, x_max, y_max = self.boundary
        r_x_min, r_y_min, r_x_max, r_y_max = range_boundary
        return not (x_max < r_x_min or x_min > r_x_max or y_max < r_y_min or y_min > r_y_max)

    def _point_in_range(self, point, range_boundary):
        # Check if a point is within a range
        r_x_min, r_y_min, r_x_max, r_y_max = range_boundary
        return r_x_min <= point.x < r_x_max and r_y_min <= point.y < r_y_max

    def _edge_in_range(self, edge, range_boundary):
        # Check if an edge is within a range
        p1, p2 = edge
        return (
            self._point_in_range(p1, range_boundary) or
            self._point_in_range(p2, range_boundary) or
            self._edge_intersects_boundary(edge)
        )

    def search(self, x, y):
        # Search for a point in the QuadTreeNode
        for point in self.points:
            if point.x == x and point.y == y:
                return point
        if self.divided:
            for child in self.children:
                result = child.search(x, y)
                if result:
                    return result
        return None  # Return None if the point is not found


class PMQuadTree:
    def __init__(self, boundary, capacity_points=DEFAULT_CAPACITY_POINTS, capacity_edges=DEFAULT_CAPACITY_EDGES):
        # Initialize the PMQuadTree with a root node and adjacency list for edges
        self.root = QuadTreeNode(boundary, capacity_points, capacity_edges)
        self.edges = defaultdict(list)  # Adjacency list for edges

    def add(self, x, y, data=None):
        # Add a point to the QuadTree
        point = Point(x, y, data)
        return self.root.insert(point)

    def remove(self, x, y):
        # Remove a point from the QuadTree and its associated edges
        def _remove(node, x, y):
            for i, point in enumerate(node.points):
                if point.x == x and point.y == y:
                    del node.points[i]
                    return True
            if node.divided:
                for child in node.children:
                    if _remove(child, x, y):
                        return True
            return False

        point = self.search(x, y)
        if point:
            del self.edges[point]
            for edge_list in self.edges.values():
                edge_list[:] = [edge for edge in edge_list if edge != point]
        return _remove(self.root, x, y)

    def search(self, x, y):
        # Search for a point in the QuadTree
        def _search(node, x, y):
            for point in node.points:
                if point.x == x and point.y == y:
                    return point
            if node.divided:
                for child in node.children:
                    result = _search(child, x, y)
                    if result:
                        return result
            return None

        return _search(self.root, x, y)

    def range_query(self, x_min, y_min, x_max, y_max, edge=None):
        # Query points and edges within a range
        found_points = []
        found_edges = []
        range_boundary = [x_min, y_min, x_max, y_max]

        if edge:
            range_boundary = [
                min(x_min, edge[0].x, edge[1].x),
                min(y_min, edge[0].y, edge[1].y),
                max(x_max, edge[0].x, edge[1].x),
                max(y_max, edge[0].y, edge[1].y),
            ]

        self.root.query_range(range_boundary, found_points, found_edges)
        return found_points, found_edges

    def addEdge(self, p1, p2):
        # Add an edge between two points
        if p1 not in self.edges:
            self.edges[p1] = []
        if p2 not in self.edges:
            self.edges[p2] = []
        if p2 not in self.edges[p1]:
            self.edges[p1].append(p2)
        if p1 not in self.edges[p2]:
            self.edges[p2].append(p1)
        self.root.insert_edge((p1, p2))

    def removeEdge(self, p1, p2):
        # Remove an edge between two points
        if p1 in self.edges and p2 in self.edges[p1]:
            self.edges[p1].remove(p2)
        if p2 in self.edges and p1 in self.edges[p2]:
            self.edges[p2].remove(p1)

    def getDistance(self, p1, p2):
        # Get the shortest distance between two points using edges
        visited = set()
        queue = deque([(p1, 0)])  # (current_point, current_distance)

        while queue:
            current, distance = queue.popleft()
            if current == p2:
                return distance
            visited.add(current)
            for neighbor in self.edges[current]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + self._euclidean_distance(current, neighbor)))

        return float('inf')  # Return infinity if no path exists

    def _euclidean_distance(self, p1, p2):
        # Calculate the Euclidean distance between two points
        return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def print_grid(self, grid_size=20):
        """
        Print the PMQuadTree as a 2D grid with points and edges.
        :param grid_size: The size of the grid (number of rows and columns).
        """
        x_min, y_min, x_max, y_max = self.root.boundary
        grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

        # Normalize points to fit within the grid
        def normalize(point):
            x = int((point.x - x_min) / (x_max - x_min) * (grid_size - 1))
            y = int((point.y - y_min) / (y_max - y_min) * (grid_size - 1))
            return x, y

        # Add points to the grid
        for node in self._get_all_points(self.root):
            x, y = normalize(node)
            grid[y][x] = 'P'  # Mark points with 'P'

        # Add edges to the grid
        for p1, neighbors in self.edges.items():
            x1, y1 = normalize(p1)
            for p2 in neighbors:
                x2, y2 = normalize(p2)
                self._draw_line(grid, x1, y1, x2, y2)

        # Print the grid
        for row in grid:
            print(' '.join(row))

    def _get_all_points(self, node):
        """
        Recursively collect all points in the QuadTree.
        """
        points = node.points[:]
        if node.divided:
            for child in node.children:
                points.extend(self._get_all_points(child))
        return points

    def _draw_line(self, grid, x1, y1, x2, y2):
        """
        Draw a line between two points on the grid using Bresenham's line algorithm.
        """
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            if 0 <= x1 < len(grid[0]) and 0 <= y1 < len(grid):
                grid[y1][x1] = 'E'  # Mark edges with 'E'
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def visualize(self, title="PMQuadTree Visualization"):
        """
        Visualize the PMQuadTree using Matplotlib.
        Points are shown as dots, edges are shown as lines, and potential next splits are shown as dashed lines.
        Each depth level is visualized with a different color.
        :param title: Title of the visualization.
        """
        fig, ax = plt.subplots(figsize=VISUALIZATION_FIGSIZE)
        x_min, y_min, x_max, y_max = self.root.boundary

        # Define colors for each depth level
        depth_colors = ['k', 'r', 'g', 'b', 'm']  # Black, Red, Green, Blue, Magenta

        # Draw the QuadTree boundaries recursively
        def draw_boundaries(node):
            x_min, y_min, x_max, y_max = node.boundary
            color = depth_colors[node.depth % len(depth_colors)]  # Cycle through colors based on depth

            # Draw current boundaries
            ax.plot([x_min, x_max], [y_min, y_min], color + '-', lw=0.5)  # Bottom
            ax.plot([x_min, x_max], [y_max, y_max], color + '-', lw=0.5)  # Top
            ax.plot([x_min, x_min], [y_min, y_max], color + '-', lw=0.5)  # Left
            ax.plot([x_max, x_max], [y_min, y_max], color + '-', lw=0.5)  # Right

            # Draw potential next splits as dashed lines
            if not node.divided and node.depth < MAX_DEPTH:
                mid_x = (x_min + x_max) / 2
                mid_y = (y_min + y_max) / 2
                ax.plot([mid_x, mid_x], [y_min, y_max], color + '--', lw=0.5)  # Vertical dashed line
                ax.plot([x_min, x_max], [mid_y, mid_y], color + '--', lw=0.5)  # Horizontal dashed line

            if node.divided:
                for child in node.children:
                    draw_boundaries(child)

        draw_boundaries(self.root)

        # Plot points
        for point in self._get_all_points(self.root):
            ax.plot(point.x, point.y, 'bo')  # Blue dots for points

        # Plot edges
        for p1, neighbors in self.edges.items():
            for p2 in neighbors:
                ax.plot([p1.x, p2.x], [p1.y, p2.y], 'r-')  # Red lines for edges

        # Set plot limits and labels
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_aspect('equal', adjustable='box')
        ax.set_title(title)  # Use the provided title
        ax.set_xlabel("X")
        ax.set_ylabel("Y")

        plt.show()
