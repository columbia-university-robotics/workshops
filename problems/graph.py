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
        print(str(root) + "->" + str(nextVal))

