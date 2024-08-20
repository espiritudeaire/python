# Construir un sistema que permita almacenar datos de pacientes, los pacientes 
# tienen datos de Nombre,cedula,genero y servicio. el sistema debe permitir 
# 1.ingresar un paciente nuevo, 2.ver todos los datos de un paciente existente
# 3.ver numero de pacientes en el sistema. 4.salir


class Paciente:
    def __init__(self, nombre, cedula, genero, servicio):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__genero = genero
        self.__servicio = servicio

    def ver_cedula(self):
        return self.__cedula

    def ver_datos(self):
        return f"Nombre: {self.__nombre}, Cédula: {self.__cedula}, Género: {self.__genero}, Servicio: {self.__servicio}"

    

class Sistema:
    def __init__(self):
        self.__lista_pacientes = []

    def ingresar_paciente(self, paciente):
        for p in self.__lista_pacientes:
            if p.ver_cedula() == paciente.ver_cedula():
                print("Error: Ya existe un paciente con esta cédula.")
                return False
        self.__lista_pacientes.append(paciente)
        return True

    def ver_datos_paciente(self, c):
        for p in self.__lista_pacientes:
            if c == p.ver_cedula():
                return p                                   # Si encuentra el paciente lo retorna
        return None

    def ver_numero_de_pacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes")
        
        
def main():
   
    servicios_validos = [
        "Ayudas diagnósticas", "Cuidados intensivos", "Urgencias", "Odontología",
        "Cirugía", "Hospitalización", "Laboratorio"
    ]
    
    menu = """
    Menú:
    ---------------
    
    1. Ingresar nuevo paciente
    2. Buscar y ver Paciente
    3. Ver número total de pacientes
    4: Salir
    
    Ingrese el número: """
    
    sis = Sistema()
    while True:
        opcion = int(input(menu))
        if opcion == 1:
            print("Formulario de Paciente Nuevo")
            nombre = input("Ingrese nombre: ")
            while True:
                cedula = input("Ingrese cédula: ")
                if len(cedula) == 10 and cedula.isdigit():
                    cedula = int(cedula)
                    break
                else:
                    print("Error: La cédula debe ser un número de 10 dígitos.")
            while True:      
                genero = input("Ingrese género(M/F o Masculino/Femenino): ").lower()
                if genero in ["m", "f", "masculino", "femenino"]:
                    if genero == "m" or genero == "masculino":
                        genero = "Masculino"
                    elif genero == "f" or genero == "femenino":
                        genero = "Femenino"
                    break
                else:
                    print("Error: Género no válido. Debe ser M, F, Masculino o Femenino.")
                
            while True:
                servicio = input("Ingrese servicio: ").lower()
                if servicio in servicios_validos:
                    servicio = servicio.capitalize()
                    break
                else:
                    print(f"Error: Servicio no válido. Servicios válidos son: {', '.join(servicios_validos)}")
            
            pac = Paciente(nombre, cedula, genero, servicio)     # se crea un objeto llamado paciente
            if sis.ingresar_paciente(pac):
                print("Paciente ingresado con éxito.\n")
            else:
                print("No se pudo ingresar el paciente debido a que ya existe una cédula registrada.\n")
       
        elif opcion == 2:
            c = int(input("Ingrese la cédula a buscar: "))
            p = sis.ver_datos_paciente(c)
            if p:
                print("Datos del paciente:")
                print(p.ver_datos())
            else:
                print("Paciente no encontrado.\n")
               
        elif opcion == 4:
            print("Saliendo del sistema.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.\n")
            
if __name__ == "__main__":
    main()