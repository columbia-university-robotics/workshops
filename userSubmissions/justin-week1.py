import sys
if __name__ == "__main__":
    graph = {}
    graph[0] = [1,2]
    graph[1] = [2,7]
    graph[2] = [3,7,9]
    graph[3] = [4,6]
    graph[4] = []
    graph[6] = []
    graph[7] = [8,9]
    graph[8] = [10]
    graph[9] = []
    graph[10] = [12]
    graph[12] = []

#start at 0, return a path to 4

#for root in graph.keys():
#    values = graph[root]
#    for nextVal in values:
#        print(str(root) + "->" + str(nextVal))

def dfs(graph, start, goal):
    stack = [(start,start)] #in format parent,value
    pred = {}
    while stack:
            node = stack.pop()
            previous = node[0]
            current = node[1]
            if previous != 0 and pred[previous]:
                pred[current] = [previous] + pred[previous]
            elif previous != 0:
                pred[current] = [previous]
            else:
                pred[current] = 0
            children = graph[current]
            if current == goal:
                print([0] + pred[current][::-1] + [goal])
                return 
            for newNode in children:
                if newNode != previous:
                    stack.append((current,newNode))
    print("node not found")
    return
dfs(graph,int(sys.argv[1]),int(sys.argv[2]))