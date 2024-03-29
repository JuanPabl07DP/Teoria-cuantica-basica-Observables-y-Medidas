import numpy as np
import numpy as np
from Vectores_matrices import *
import matplotlib.pyplot as plt
from scipy import constants

def prob(ket, pos):
    norm = np.linalg.norm(ket) ** 2
    ket[pos][0] = np.linalg.norm(ket[pos][0]) ** 2 / norm
    return round(ket[pos][0].real, 2)


def prob2(ket, eigv):
    mult = np.inner(ket, eigv)
    return np.linalg.norm(mult) ** 2


def bra(ket):
    return ket.transpose().conjugate()


def transitionProb(ket, ket2):
    ket2Dagger = bra(ket2)
    result = np.dot(ket2Dagger, ket)
    return round(np.linalg.norm(result) ** 2, 2)


def expected(obs, ket):
    mult = np.matmul(obs, ket)  # Multiplication between observable and ket
    expected = np.dot(mult.transpose().conjugate(), ket)[0][0]
    return expected


def deltaOp(obs, mat):
    return obs - mat


def variance(obs, ket):
    exp = expected(obs, ket)
    mult = exp * np.identity(len(obs))  # Multiplication between expected and indentity matrix
    delta = deltaOp(obs, mult)
    mult2 = np.matmul(delta, delta)  # Multiplication between delta and delta
    var = expected(mult2, ket).real
    return var


def measures(obs):
    return np.linalg.eig(obs)[0]


def finalStates(obs):
    return np.linalg.eig(obs)[1]


def finalStateDin(ket, transformations):
    finalState = ket
    for i in range(len(transformations)):
        finalState = np.matmul(transformations[i], finalState)
    return finalState


transformations = np.array([np.array([[(1 + 1j)/2, (1 - 1j)/2], [(1 - 1j)/2, (1 + 1j)/2]]),
                            np.array([[1, 0], [0, 1j]])])
ket = np.array([1j, 2j])

print(finalStateDin(ket,transformations))

""" Punto 4.3.1"""
def posiblesProbabilidad(posicion, index):
    estados = [[(0,1),(1,0)],[(0,-1),(1,0)],[(1,0),(1,0)],[(-1,0),(1,0)],[(0,0),(1,0)],[(1,0),(0,0)]]
    resultado = []
    for i in range((index*2)-2,index*2):
        if probabilidad(posicion,estados[i])!= 0.0:
            resultado = resultado + estados[i]
    return resultado

""" Punto 4.3.2 """
def probabilidadValoresPropios(posicion, index):
    matrices = [[[(1,0),(0,0)],[(0,0),(-1,0)]],[[(0,0),(0,-1)],[(0,1),(0,0)]],[[(0,0),(1,0)],[(1,0),(0,0)]]]
    valoresPropios = []
    aux = posiblesProbabilidad(posicion, index)
    pro= []
    resultado = 0
    for i in range(3):
        valores,no = np.linalg.eig(matrices[i])
        valoresPropios+=valores
    for i in range(len(aux)):
        pro+=probabilidad(posicion, aux[i])
    for i in range(2):
        ressultado+=(probabilidad[i]*valoresPropios[indice][i])
    return resultado

""" Punto 4.4.1"""
def verificarUnitarias():
    U1 = [[(0,0),(1,0)],[(1,0),(0,0)]]
    U2 = [[((2**(1/2))/2,0),((2**(1/2))/2,0)],[((2**(1/2))/2,0),(-(2**(1/2))/2,0)]]
    if Uni(U1) and Uni(U2):
        resultado = producto_matrices_reales(U1,U2)
        return Uni(resultado)

""" Punto 4.4.2 """
def ExperimentoCanicas(vectorEstado,canicas,nclicks):
    for i in range(nclicks):
        vectorEstado = vectormatrizReal(vectorEstado,canicas)
    return vectorEstado
