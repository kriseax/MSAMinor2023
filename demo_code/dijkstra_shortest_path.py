import math
def dijkstra(graph, start):
    #initialize tentative and confirmed dictionaries
    tentative = {}
    confirmed = {}

    #add start node cost to the confirmed dictionary
    confirmed[start] = 0
    
    #place the start nodes neighbors in the tentative dictionary
    for node, distance in graph[start].items():
        tentative[node] = distance

    #set next to the node just added to confirmed
    next = start
    
    #while the tentative dictionary still has nodes
    while tentative:
        shortest_distance = math.inf
        #select node from tentative dictionary with the lowest cost
        for node, distance in tentative.items():
            #determine shortest distance node
            if distance <shortest_distance:
                shortest_distance = distance
                next = node

        #add lowest cost node to comfirmed dictionary and update next
        confirmed[next] = shortest_distance
        # remove next node from tentative dictionary
        tentative.pop(next)

        #place next nodes neighbors on tentative list.
        for node, distance in graph[next].items():
            cost = confirmed[next] + distance
            #if the neighbor is not in tentative, add to tentative.
            #if neighbor in tentative, update cost if necessary
            #if neighbor in confirmed then ignore
            if node in confirmed:
                continue
            elif (node in tentative) and (cost < tentative[node]):
                tentative[node] = cost
            elif node not in tentative:
                tentative[node] = cost
    
    return confirmed

def main():
    graph = {
        'A': {'B': 5, 'C':10},
        'B': {'A': 5, 'C': 3, 'D': 11},
        'C': {'A': 10,'B': 3, 'D':2},
        'D': {'B':11, 'C':2}
    }

    #choose a start node
    start_node = 'D'

    distances = dijkstra(graph, start_node)

    for node, distance in distances.items():
        print(f"{node} -> {distance}")

main()