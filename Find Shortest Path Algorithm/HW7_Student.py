def HW7_Student(start_node, end_node, graph):
    shortestDist = {}
    visited = []
    prevNode = {}
    final = []
    for node in graph:
        if node == start_node:
            shortestDist[node] = 0
        else:
            shortestDist[node] = float('inf')

    closestNode = start_node

    while len(visited) <= len(graph):
        print("RESTART")
        currentNode = closestNode
        shortestdistance = float("inf")
        for neighbor in graph[currentNode][1:]:
            print("neighbor node:",neighbor)
            if neighbor in visited:
                pass
            else:
                tentativeDist = shortestDist[currentNode] +  graph[neighbor][0]
                print("tentativeDist:",tentativeDist)
                print("shortestDist[neighbor]:",shortestDist[neighbor])
                if tentativeDist < shortestDist[neighbor]:
                    shortestDist[neighbor] = tentativeDist
                    prevNode[neighbor] = currentNode
                    print("updating distance from node",currentNode,"to",neighbor,"as:",tentativeDist)
                if tentativeDist < shortestdistance:
                    print("Node:",neighbor,"is closer to node:",currentNode,"than any other node seen so far:")
                    shortestdistance = tentativeDist
                    print("Distance to beat is now:",shortestdistance)
                    closestNode = neighbor
                else:
                    pass
        if currentNode in visited:
            pass
        else:
            visited.append(currentNode)
        print("visited:",visited)
        if end_node in visited:
            print("should return right answer")
            myNode = end_node
            final.append(myNode)
            while prevNode[myNode] != start_node:
                final.append(myNode)
                myNode = prevNode[myNode]
            final.append(start_node)
            final = final[::-1]
            return final
            #append nodes to final array

    return []
