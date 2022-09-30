if __name__ == "__main__":
    graph = {}
    graph[0] = [1,2]
    graph[1] = [0,2,7]
    graph[2] = [0,1,3,7,9]
    graph[3] = [2,4,6]
    graph[4] = [3]
    graph[6] = [3]
    graph[7] = [1,2,8,9]
    graph[8] = [7,10]
    graph[10] = [8,12]
    graph[12] = [10]

#start at 0, return a path to 4
for root in graph.keys():
    values = graph[root]
    for nextVal in values:
        print(str(root) + "->" + str(nextVal))

