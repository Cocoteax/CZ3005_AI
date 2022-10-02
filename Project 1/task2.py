import heapq #Importing in-built priority queue for UCS 
import json
import math

def UCS(src, goal, G, Dist, Cost, energy_constraint):
    pq = []
    pi = [] # Path
    path = []
    heapq.heapify(pq)
    visited = set()
    visited.add(src)
    heapq.heappush(pq,[[0,0],-1,src]) #[Distance, energy] , Parent node, Source node

    while pq:
        smallest = heapq.heappop(pq)
        node = smallest[2]
        parent = smallest[1]
        distance = smallest[0][0]
        neighbors = G[node]
        energy = smallest[0][1]
        visited.add(node)
        pi.append(smallest)
        
        if node == goal:
            s = goal
            for i in range(len(pi)-1,-1,-1):
                if pi[i][2] == parent:
                    s = parent + " -> " + s
                    parent = pi[i][1]
                    
            print("Shortest path:",str(s))
            print()
            print("Energy Cost: "+str(energy))
            print()
            print("Shortest Distance: " + str(distance))
            print()
            return
        
        for n in neighbors:
            if n not in visited:
                dis = node+','+n
                cost = Dist[dis]
                if Cost[dis] + energy < energy_constraint:
                    heapq.heappush(pq,[[distance+cost, Cost[dis]+energy], node, n])  
                    
        

     