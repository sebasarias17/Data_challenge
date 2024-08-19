from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        n = len(graph) 
        if n == 1:
            return 0 
        # Cola para BFS: almacena tuplas (nodo_actual, máscara_actual, distancia_actual)
        queue = deque()
        visited = set()

        for i in range(n):
            mask = 1 << i  
            queue.append((i, mask, 0))  # Añadir (nodo inicial, máscara, distancia 0) a la cola
            visited.add((i, mask))  # Marcar este estado como visitado

        # Comienza BFS
        while queue:
            node, mask, dist = queue.popleft() 

            if mask == (1 << n) - 1:
                return dist  

            for neighbor in graph[node]:
                
                next_mask = mask | (1 << neighbor)

                if (neighbor, next_mask) not in visited:
                    queue.append((neighbor, next_mask, dist + 1))  
                    visited.add((neighbor, next_mask))  
        return -1  