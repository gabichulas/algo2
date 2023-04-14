class DictionaryElement:
    key = None
    value = None


def insert(D, key, value):
    position = key % 9
    newElement = DictionaryElement()
    newElement.key = key
    newElement.value = value
    if D[position] == None:
        D[position] = [newElement]
    else:
        D[position].append[newElement]
    return D


def search(D, key):
    position = key % 9
    element = D[position]
    if D[position] == None:
        return None
    else:
        for nodo in element:
            if nodo.key == key:
                return key
        return None


def delete(D, key):
    position = key % 9
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
