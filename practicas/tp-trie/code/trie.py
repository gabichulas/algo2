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
    else:
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
    for i in range(i,len(element)):
        node.key = element[i]
        node.children = []
        node.children.append(TrieNode())
        node.children[0].parent = node
        node = node.children[0]
    node=node.parent
    node.isEndOfWord = True
    node.children = None



def search(T,element):
    if T==None or len(element)==0:
        False
    else:
        return searchR(T.root.children,element)

def searchR(current,element):
    letra = searchLetter(current,element)
    if letra != None:
        if len(element)>1:    
            if letra.children != None:
                return searchR(letra.children,element[1:])
            else:
                return False
        elif letra.isEndOfWord == True:
            return True
        else:
            return False
            
    else:
        return False


def searchLetter(list,element):
    for i in list:
        if i.key==element[0]:
            return i
    return None


def delete(T,element):
    if T==None or len(element)==0:
        return False
    else:
        value = deleteR(T.root.children,element)
        if value == '.':
            return True
        else:
            return value
    
def deleteR(current,element):
    letra = searchLetter(current,element)
    if letra != None:
        if len(element) > 1:
            if letra.children != None:
                resp = deleteR(letra.children,element[1:])
                if resp == ".":
                    if letra.isEndOfWord:
                        return True
                    else:
                        current.remove(letra)
                        return "."
        if letra.isEndOfWord:
            if letra.children != None:
                letra.isEndOfWorld = False
            else:
                current.remove(letra)
                return "."
        else:
            return False
    else:
        return False
    

arbol = Trie()
insert(arbol,"rodri")

print(search(arbol,"rodri"))

delete(arbol,"rodri")

print(search(arbol,"rodri"))


