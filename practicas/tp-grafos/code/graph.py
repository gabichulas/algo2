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

def isInList(list,object):
    for node in range(len(list)):
        if list[node] == object:
            return True



vertice = [1,2,3,4,5]
aristas = [[1,2],[1,3],[2,4],[3,4]]
grafo = createGraph(vertice,aristas)

print(existPath(1,2,grafo))