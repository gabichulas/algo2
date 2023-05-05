from random import *
from linkedlist import *
from myqueue import *

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
    for i in range(len(graph)):
        if graph[i].vertex == v:
            return graph[i]
    return None

def searchVertexIndex(graph,v):
    for i in range(len(graph)):
        if graph[i].vertex == v:
            return i
    return None

def numberOfEdges(graph):
    grades = 0
    for i in range(len(graph)):
        grades += len(graph[i].adjacentvertex)
    return grades/2

def isInList(list,object):
    for node in range(len(list)):
        if list[node] == object:
            return True
        
############################################################

def existPath(v1,v2,graph):
    vertex1 = searchVertex(graph,v1)
    vertex2 = searchVertex(graph,v2)
    visited = []
    queue = LinkedList()
    return existPathR(vertex2,graph,vertex1,visited,queue)

def existPathR(v2,graph,pivot,list,q):
    if len(pivot.adjacentvertex) > 0:
        list.append(pivot.vertex)
        for adj in range(len(pivot.adjacentvertex)):
            if pivot.adjacentvertex[adj] == v2.vertex:
                return True
            elif not isInList(list,pivot.adjacentvertex[adj]):
                enqueue(q,pivot.adjacentvertex[adj])
        while q.head != None:
            newPivot = searchVertex(graph,dequeue(q))
            newQueue = LinkedList()
            return existPathR(v2,graph,newPivot,list,newQueue)
    return False


def isConnected(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i==j:
                continue
            elif not existPath(graph[i].vertex,graph[j].vertex,graph):
                return False
    return True

def isTree(graph):
    if isConnected(graph):
        if numberOfEdges(graph) == len(graph) - 1:
            return True
    return False

def isComplete(graph):
    if isConnected(graph):
        for v in graph:
            if not (len(v.adjacentvertex) == len(graph) - 1):
                return False
        return True
    return False

def convertTree(graph):
    tree_edges = []
    visited = []
    cola = LinkedList()
    for i in range(0,len(graph)):
        visited.append(graph[i].vertex)
        enqueue(cola,graph[i])
        while cola != None:
            currentnode = dequeue(cola)
            for j in range(0,len(currentnode.adjacentvertex)):
                if len(currentnode.adjacentvertex) > 0:
                    if currentnode.adjacentvertex[j] not in visited:
                        vecino = graph[searchVertexIndex(graph,currentnode.adjacentvertex[j])]
                        visited.append(currentnode.adjacentvertex[j])
                        enqueue(cola,vecino)
                    else:
                        if searchinq(cola,currentnode.adjacentvertex[j]) == False:
                            graphcopy = graph
                            indexvecino = searchVertexIndex(graph,currentnode.adjacentvertex[j])
                            indexcurrentnode = searchVertexIndex(graph,currentnode.vertex)
                            graphcopy[indexcurrentnode].adjacentvertex.remove(currentnode.adjacentvertex[j])
                            graphcopy[indexvecino].adjacentvertex.remove(currentnode.vertex)
                            if isTree(graphcopy) == True:
                                tree_edges.append([currentnode.vertex,vecino.vertex])
    return tree_edges    

def searchinq(q,value):
    currentnode = q.head
    while currentnode != None:
        if currentnode.value == value:
            return True
        currentnode = currentnode.nextNode
    return False  

def countConnections(graph):
    visited = []
    comps = 0
    for node in graph:
        if node.vertex not in visited:
            BFS(graph,node,visited)
            comps += 1
    return comps

def BFS(graph,node,visited):
    visited.append(node.vertex)
    for j in range(0,len(node.adjacentvertex)):
        if node.adjacentvertex[j] not in visited:
            vecino = searchVertex(graph,node.adjacentvertex[j])
            BFS(graph,vecino,visited)

def convertToBFSTree(graph, v):
    if not isConnected(graph):
        return print("El grafo no es conexo, no se puede aplicar la operacion.")
    


vertice = [1,2,3,4,5]
aristas = [[1,3],[2,3],[2,4],[1,5],[3,5]]
grafo = createGraph(vertice,aristas)

print(countConnections(grafo))