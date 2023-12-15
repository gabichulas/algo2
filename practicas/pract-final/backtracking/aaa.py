def darCambio(cambio, monedas):
    mejor_solucion = [None]
    def backtrack(resto, monedas_usadas):
        # Si el resto es 0, hemos encontrado una solución
        if resto == 0:
            if mejor_solucion[0] is None or len(monedas_usadas) < len(mejor_solucion[0]):
                mejor_solucion[0] = monedas_usadas
            return
        # Si el resto es negativo o ya hemos usado más monedas que la mejor solución hasta ahora, esta rama no es una buena solución
        if resto < 0 or (mejor_solucion[0] is not None and len(monedas_usadas) >= len(mejor_solucion[0])):
            return
        # Prueba todas las monedas
        for moneda in monedas:
            backtrack(resto - moneda, monedas_usadas + [moneda])

    backtrack(cambio, [])
    return len(mejor_solucion[0]) if mejor_solucion[0] is not None else 0


print(darCambio(14, [1, 2, 6, 7, 10]))

# Se dispone de una mochila que acepta un peso máximo PesoMax, y de k latas de peso P1, P2, P3, …,
# Pk, todos diferentes. Se desea llevar la mayor cantidad de peso posible en la mochila. 
# Implemente un método que decida que latas deben echarse con este fin.

""" def mochila(PesoMax, latas):
    mejorSolucion = [[]]
    def backtrack(resto, latasUsadas):
        if resto >= 0 and pesoLatas(latasUsadas) > pesoLatas(mejorSolucion[0]):
            mejorSolucion[0] = latasUsadas
        if resto < 0 or (resto == 0 and pesoLatas(latasUsadas) <= pesoLatas(mejorSolucion[0])):
            return
        for peso in latas:
            backtrack(resto-peso, latasUsadas + [peso])
    backtrack(PesoMax,[])
    return mejorSolucion[0] """

def mochila(PesoMax, latas):
    latas.sort(reverse=True)
    mejorSolucion = [[]]
    def backtrack(resto, latasUsadas, start):
        if resto >= 0 and pesoLatas(latasUsadas) > pesoLatas(mejorSolucion[0]):
            mejorSolucion[0] = latasUsadas
        if resto <= 0:
            return
        for i in range(start, len(latas)):
            if latas[i] > resto:
                continue
            backtrack(resto-latas[i], latasUsadas + [latas[i]], i+1)
    backtrack(PesoMax, [], 0)
    return mejorSolucion[0]


def pesoLatas(arr):
    pesoRes = 0
    for lata in arr:
        pesoRes += lata
    return pesoRes


print(mochila(200,[20,50,300,80,27,48,23,1,39,20]))

def subsecuenciaCreciente(numeros):
    mejorSolucion = [[]]
    def backtrack(numeritos, start):
        if len(numeritos) > len(mejorSolucion[0]):
            mejorSolucion[0] = numeritos
        for i in range(start, len(numeros)):
            if not numeritos or numeros[i] > numeritos[-1]:
                backtrack(numeritos + [numeros[i]], i + 1)
    for i in range(len(numeros)):
        backtrack([numeros[i]], i + 1)
    return mejorSolucion[0]

print(subsecuenciaCreciente([ 5, 1, 2, 3, 100, 20, 17, 8, 19, 21]))

def subconjuntoSuma(numeros, valor):
    mejorSolucion = [[]]
    def backtrack(valor, parcial,start):
        if parcial == valor: 
            mejorSolucion[0] = True
            return
        if parcial > valor: return
        for i in range(start, len(numeros)):
            backtrack(valor, parcial+numeros[i], i+1)
    backtrack(valor, 0,0)
    return mejorSolucion[0] if mejorSolucion[0] == True else False

print(subconjuntoSuma([11, 6, 5, 1, 7, 13, 12],15))