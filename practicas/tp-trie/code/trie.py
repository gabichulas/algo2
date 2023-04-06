class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

def insert(T,element):
    if T.root == None:
        T.root = TrieNode()
        T.root.children = []
        T.root.children.append(TrieNode())
        T.root.children[0].parent = T.root
        completeword(T.root.children[0],element,0)
    end = False
    i = 0
    cont = 0
    list = T.root.children
    current = list[0]
    while end != True:
        if current.key == element[i]:
            i +=1
            if i == len(element):
                current.isEndOfWord = True
                return T
            list = current.children
            if not list:
                current.children = []
                current.children.append(TrieNode())
                current.children[0].parent = current
                end = True
            else:
                current = list[0]        
        if current[cont+1] == None:
            list.insert(0,TrieNode())
            current[0].parent = current
            end = True
        else:
            cont += 1
    completeword(list[0],element,i)
    return T




def completeword(node,element,i):
    for i in range(i,len(element)-1):
        node.key = element[i]
        node.childen = []
        node.children.append(TrieNode())
        node.children[0].parent = node
        node = node.children[0]
    node.isEndOfWord = True



arbol = Trie()
insert(arbol,"rodrigo")

print(arbol.root.children[0])
