# -----------------------------------
# declaring local arrayList
# -----------------------------------
from http.cookiejar import join_header_words

vec1 = [5, 1, 7, 4, 9]
vec2 = [6, 8, 2, 5, 4, 3, 1]
# -----------------------------------
# Declaring a joins functions
# -----------------------------------
def Join():
    salida = []
    for act in vec1:
        control = act in vec2
    if control:
        salida.append(act)
    return salida
def FullJoin():
    salida2 = vec1
    for act in vec2:
        control = act in salida2
    if not control:
        salida2.append(act)
    return salida2
#Cada elemento de los vectores se comparan para almacenar solo aquellos que no tienen en común
def FullOuterJoin():
    out = []
    for var in vec1:
        if var not in vec2:
            out.append(var)
    for element in vec2:
        if element not in vec1:
            out.append(element)
    return out
#Elementos de vec1 que no están en vec2
def RightJoin():
    guardar = []
    for element in vec1:
        if element not in vec2:
            guardar.append(element)
    return guardar
# -----------------------------------
# Executing joins functions
# -----------------------------------
print('Join')
print(Join())
print('FullJoin')
print(FullJoin())
print('FullOuterJoin')
print(FullOuterJoin())
print('RightJoin')
print(RightJoin())
