import heapq
import sys


class Graphs:
    def __init__(self, directed = False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_string = ""

        for node, neighbours in self.adj_list.items():
            graph_string += f"{node} -> {neighbours}\n"

        return graph_string

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists")

    def add_edge(self,from_node,to_node, weight=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)
        if weight is None:
            self.adj_list[from_node].add(to_node)

            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node, weight))

            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        queue.append(neighbour)
        return order

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbour in sorted(neighbours, reverse=True):
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)
        return order

    def obtain_neighbours(self, node):
        return self.adj_list.get(node, set())


#DIJKSTRA'S ALGORITHM
    def dijkstra(self, start_node):
        # Priority queue: (distance, node)
        heap = [(0, start_node)]
        distances = {node: float('inf') for node in self.adj_list}
        distances[start_node] = 0
        visited = set()

        while heap:
            current_dist, current_node = heapq.heappop(heap)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbour in self.adj_list[current_node]:
                # If graph is unweighted (no tuples), skip Dijkstra
                if not isinstance(neighbour, tuple):
                    continue

                neighbour_node, weight = neighbour
                new_dist = current_dist + weight

                if new_dist < distances[neighbour_node]:
                    distances[neighbour_node] = new_dist
                    heapq.heappush(heap, (new_dist, neighbour_node))

        return distances


if __name__ == "__main__":
    graph_obj = Graphs(directed = True)

    graph_obj.add_edge("A","B",2)
    graph_obj.add_edge("A","J",2)
    graph_obj.add_edge("A","C",3)
    graph_obj.add_edge("A","D",4)
    graph_obj.add_edge("B","D",0)
    graph_obj.add_edge("D","C",7)

    print(graph_obj)
    print("BREADTH FIRST SEARCH: \n")
    print(graph_obj.bfs("A"))

    print("DEPTH FIRST SEARCH: \n")
    print(graph_obj.dfs("A"))

