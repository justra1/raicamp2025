'''
text = ["apple" , "banana"]
text.append("orange")
text.insert(0,"melon") #เหมือน append แต่บอกตำแหน่งได้
for texts in text :
    print(f"This is a {texts}.")

i = 0    
while i < 3:
    print("w")
    i = i +2
print("done")
'''
# dictionary in Mobile Robot
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}
start = 'A'
goal = 'E'
frontier = [start]
explored = set() #

print(frontier, explored)

while len(frontier) > 0:
    current = frontier.pop() # remove and put into varaible
    print(current)
    if  current == goal:
        print("Goal reach")
        break
    print(f"neighor of {current} is {graph[current]}")
    for neighbor in graph[current]:
        frontier.append(neighbor)