# -----------------------------------
# declaring local arrayList
# -----------------------------------
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

def FullOuterJoin():
    out = []
    for act in vec2:
        a = vec1[0]
        control = [act in vec1]
        if control != act:
            out.append(act)
    return out

# -----------------------------------
# Executing joins functions
# -----------------------------------
print(Join())
print('')
print(FullJoin())
print()
print(FullOuterJoin())
