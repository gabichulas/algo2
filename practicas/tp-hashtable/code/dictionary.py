class DictionaryElement:
    key = None
    value = None

def createDictionaryString(D,string):
    for ch in string:
        insert(D,ord(ch),ch)
    return D

def areEqual(D,H):
    if len(D) == len(H) and len(D) > 0:
        for i in len(D):
            if not (D[i].key == H[i].key and D[i].value.sort() == H[i].value.sort()):
                return False
        return True
    return False

def insert(D, key, value):
    position = key % 4
    newElement = DictionaryElement()
    newElement.key = key
    newElement.value = value
    if D[position] == None:
        D[position] = [newElement]
    else:
        D[position].append[newElement]
    return D


def search(D, key):
    position = key % 4
    element = D[position]
    if D[position] == None:
        return None
    else:
        for nodo in element:
            if nodo.key == key:
                return key
        return None


def delete(D, key):
    position = key % 4
    element = D[position]
    if D[position] == None:
        return
    elif len(element) == 1:
        D[position].clear()
    else:
        for nodo in element:
            if nodo.key == key:
                element.remove(nodo)
                break
    return D


def findPermutation(string,string2):
    D = []
    D2 = []
    D = createDictionaryString(D,string)
    D2 = createDictionaryString(D2,string2)
    return areEqual(D,D2)



