import heapq #Importing in-built priority queue for UCS 
import json
import math



def UCS(src, goal, G, Dist, Cost):
    pq = []
    pi = [] # Path
    path = []
    heapq.heapify(pq)
    visited = set()
    visited.add(src)
    heapq.heappush(pq,[0,-1,src])
    
    while pq:
        smallest = heapq.heappop(pq)
        node = smallest[2]
        parent = smallest[1]
        distance = smallest[0]
        neighbors = G[node]
        visited.add(node)
        pi.append([distance, parent, node])
        
        if node == goal:
            s = goal
            for i in range(len(pi)-1,-1,-1):
                if pi[i][2] == parent:
                    s = parent + " -> " + s
                    parent = pi[i][1]
                    
            print("Shortest path:")
            print(s)
            print()
            print("Shortest Distance: " + str(distance))
            print()
            return
        for n in neighbors:
            if n not in visited:
                dis = node+','+n
                cost = Dist[dis]
                heapq.heappush(pq,[distance+cost, node, n])  