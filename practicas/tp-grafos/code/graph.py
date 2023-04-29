class GraphNode:
    vertex = None
    adjacentvertex = None


def createGraph(V,A):
    graph = []
    if len(V)>0 and len(A)>0:
        for i in range(0,len(V)):
            newNode = GraphNode()
            newNode.vertex = V[i]
            newNode.adjacentvertex = []
            graph.append(newNode)
        
        for j in range(len(A)):
            for k in range(len(graph)):
                if A[j][0] == graph[k].vertex:
                    graph[k].adjacentvertex.append(A[j][1])
                elif A[j][1] == graph[k].vertex:
                    graph[k].adjacentvertex.append(A[j][0]) 
    return graph

def searchVertex(graph,v):
    for i in graph:
        if graph[i].vertex == v:
            return graph[i]
    return None

def existPath(v1,v2,graph):
    vertex1 = searchVertex(graph,v1)
    vertex2 = searchVertex(graph,v2)
    







vertice = [1,2,3,4]
aristas = [[1,2],[1,3],[2,4],[3,4]]
grafo = createGraph(vertice,aristas)

print(grafo[1].adjacentvertex)