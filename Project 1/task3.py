
import json
import math

#Implementing A* Search
def straightLineDist(Coord,x,y):
    x_1 = Coord[x][0]
    y_1 = Coord[x][1]
    x_2 = Coord[y][0]
    y_2 = Coord[y][1]
    return math.sqrt(pow(x_1-x_2,2) + pow(y_1-y_2,2)) 

def Astar(start,end,G,Dist,Cost,maxCost,Coord):
    astar_queue =[[[start],0,0,-1,start]]  # totalDist, dist, cost, parent ,node
    pi=[]
    visited = []
    while(len(astar_queue)>0):
        astar_queue = sorted(astar_queue)
        totalDist,dist, cost, parent ,node = astar_queue.pop()
        pi.append([parent ,node])
        if(node==end):
            s = end
            for i in range (len(pi)-1,-1,-1):
                if pi[i][1] == parent:
                    s = parent+ "->" + s
                    parent=pi[i][0]

            print("Shortest path:",str(s))
            print()
            print("Energy Cost: "+str(cost))
            print()
            print("Shortest Distance: " + str(dist))
            print()
            return
            
        if node in visited: 
            continue
        for i in range (len(G[node])):
            if G[node][i] not in visited:
                d = dist + Dist["{},{}".format(int(node),int(G[node][i]))]
                c = cost + Cost["{},{}".format(int(node),int(G[node][i]))]
                total = d + straightLineDist(Coord,end,"{}".format(G[node][i]))
                if c <= maxCost:
                    astar_queue.append([-total,d,c,node,G[node][i]])
        visited.append(node)
    