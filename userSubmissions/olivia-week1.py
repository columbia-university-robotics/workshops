if __name__ == "__main__":
    graph = {}
    graph[0] = [1,2]
    graph[1] = [2,7]
    graph[2] = [1,3,7,9]
    graph[3] = [4,6]
    graph[4] = []
    graph[6] = []
    graph[7] = [8,9]
    graph[8] = [10]
    graph[10] = [12]
    graph[12] = []

#start at 0, return a path to 4
for root in graph.keys():
    values = graph[root]
    for nextVal in values:
        pass
        print(str(root) + "->" + str(nextVal))
print(graph)

goal = 4
starting = 0
visitedPoints = []
path = []

def depthFirstSearch(visitedPoints, graph, point):
    # check if we have already visited this point
    if point not in visitedPoints:
        # check if this point has any children
        if point in graph.keys() and (len(graph[point]) > 0):
            visitedPoints.append(point)
            path.append(point)
            print(graph[point])

            # if a child of the point is the goal, we are done
            for child in graph[point]:
                if child == goal:
                    path.append(goal)
                    print(path)
                    exit()
                
                # if we are not done, keep going with the algorithm
                else:
                    depthFirstSearch(visitedPoints, graph, child)
        else:
            path.pop()

depthFirstSearch(visitedPoints,graph,starting)