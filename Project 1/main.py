import json
import math
import task1,task2,task3

energy_constraint = 287932


g = open("G.json")
cost = open("Cost.json")
coord = open("Coord.json")
dist = open("Dist.json")
G = json.load(g)
Cost = json.load(cost)
Coord = json.load(coord)
Dist = json.load(dist)

print("Task 1: ")
print()
task1.UCS("1","50",G,Dist,Cost)
print()
print("Task 2: ")
print()
task2.UCS("1","50",G,Dist,Cost,energy_constraint)
print("Task 3: ")
print()
task3.Astar("1","50",G,Dist,Cost,energy_constraint,Coord)
