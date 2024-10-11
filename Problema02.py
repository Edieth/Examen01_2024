# import external libraries
import random
# store  value into cube
def iniCubo(cb, semanas):
    for fil in range(len(cb)):
        for col in range(6):
            for pro in range(semanas):
                cb[fil][col][pro] = random.randint(1, 12)
#Print the cube of worked hours with format
def impCubo(cb, empleados, semanas):
    dias = ["L", "K", "M", "J", "V", "S"]

    for pro in range(semanas):
        print(f"Semana {pro + 1}")
        for col in range(6):
            print(f"Nombre, {dias[col]}\t", end="")
        print()

        for fil in range(len(cb)):
            print(f"{empleados[fil]}\t", end="")
            for col in range(6):
                print(f"{cb[fil][col][pro]:02}\t", end="")
            print()
        print('=====================================')

# Calculate the monthly salary of each employee
def calcularSalarios(cb, empleados, salarios, semanas, Horas_Laboradas):
    print("Nómina de empleados")
    print("Empleado\tHoras\tSalario bruto\tHoras extra\tSalario extra\tSalario total")

    for fil in range(len(cb)):
        total_horas = 0
        for col in range(6):
            for pro in range(semanas):
                total_horas += cb[fil][col][pro]

        horas_semanales_normales = 8 * 6
        horas_totales_normales = horas_semanales_normales * semanas

        horas_extra = max(Horas_Laboradas[fil] - horas_totales_normales, 0)

        salario_normal = min(total_horas, horas_totales_normales) * salarios[fil]
        salario_extra = horas_extra * salarios[fil] * 1.5
        salario_total = salario_normal + salario_extra


        print(f"{empleados[fil]}\t{total_horas}\t{salario_normal:.2f}\t\t{horas_extra}\t\t{salario_extra:.2f}\t\t{salario_total:.2f}")



def solicitarDatos():
    num_empleados = int(input("¿Cuántos empleados componen la planilla? "))
    empleados = []
    salarios = []
    Horas_Laboradas = []

    for i in range(num_empleados):
        nombre = input(f"Ingrese el nombre del empleado {i + 1}: ")
        empleados.append(nombre)
        salario = float(input(f"Ingrese el salario por hora de {nombre}: "))
        salarios.append(salario)
        Horas = float(input(f"Ingrese las horas laboradas por {nombre}: "))
        Horas_Laboradas.append(Horas)
    semanas = int(input("¿Cuántas semanas tiene el mes (4 o 5)? "))

    return empleados, salarios, semanas, Horas_Laboradas


def main():
    empleados, salarios, semanas, Horas_Laboradas = solicitarDatos()

    cubo = [[[0 for _ in range(semanas)] for _ in range(6)] for _ in range(len(empleados))]

    iniCubo(cubo, semanas)
    impCubo(cubo, empleados, semanas)
    calcularSalarios(cubo, empleados, salarios, semanas, Horas_Laboradas)


if __name__ == "__main__":
    main()
