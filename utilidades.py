def imprimir_menu():
    menu = " selecciona"
    [1] "registrar alumno"
    [2] "listar todos los alumnos"
    [3] "buscar alumnos por nivel"
    [4] "calcular promedio general"
    [5] "salir del programa"

    print(menu,end="")

    def validar_numeracion(menor,mayor):
        while True:
            try:
                op = int(input)

                if op>=menor and op<=mayor
                    return op
                else:
                    raise value error
            except:
                print("ingresa un numero valido",end="")
    def registrar_alumnos():
        try:
            nombre = input("ingrese el nombre del alumno:")
            apellido = input("ingrese el apellido del alumno")
            edad = int(input("ingrese la edad del alumno"))
            nivel = input("ingrese el nivel de el alumno(ejemplo: 1,2,3):")
            notas = [ramdom.randint(1,10)for _ in range(5)]
        
                
        

