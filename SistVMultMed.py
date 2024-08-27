from datetime import date

class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=date.today()
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMedicamento(self,historia, nom_med):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                lista = masc.verLista_Medicamentos()
                for med in lista:
                    if med.verNombre() == nom_med:
                        lista.remove(med)
                        return True
        return False
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 

def verificar_existencia_medicamento_en_lista(lista, nombre_med):
    for m in lista:
        if m.verNombre() == nombre_med:
            return True
    return False

def main():
    servicio_hospitalario = sistemaV()
    
    med1 = Medicamento()
    med1.asignarNombre("Acetaminofen")
    med1.asignarDosis(2)
    
    med2 = Medicamento()
    med2.asignarNombre("Ibuprofeno")
    med2.asignarDosis(2)
    
    med3 = Medicamento()
    med3.asignarNombre("Dolex")
    med3.asignarDosis(2)
    
    listam1 = [med1, med2]
    listam2 = [med2, med1, med3]
    
    mascota1 = Mascota()
    mascota1.asignarHistoria(123)
    mascota1.asignarNombre("Lupita")
    mascota1.asignarPeso(32)
    mascota1.asignarTipo("canino")
   # mascota1.asignarFecha(date.today)
    mascota1.asignarLista_Medicamentos(listam1)
    
    mascota2 = Mascota()
    mascota2.asignarHistoria(1235)
    mascota2.asignarNombre("Rocky")
    mascota2.asignarPeso(32)
    mascota2.asignarTipo("felino")
    #mascota2.asignarFecha(date.today)
    mascota2.asignarLista_Medicamentos(listam2)
    
    print(mascota1.verFecha)
    
    servicio_hospitalario.ingresarMascota(mascota1)
    servicio_hospitalario.ingresarMascota(mascota2)
    
    # sistma=sistemaV()
    while True:
        menu=int(input(f'''
                       \n Número de mascotas en el servicio: {servicio_hospitalario.verNumeroMascotas()}
                       \nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento de mascota 
                       \n7- Salir
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                #fecha=date.today()
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = input(f"Ingrese el nombre del medicamento {i+1}: ")
                    while (verificar_existencia_medicamento_en_lista(lista_med, nombre_medicamentos)):
                        
                        print("Ya existe este medicamento en la lista de la mascota...")
                        nombre_medicamentos = input(f"Ingrese el nombre del medicamento {i+1}: ")
                    
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)                     
                    lista_med.append(medicamento)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                #mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de historia clínica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print(f"La fecha de ingreso de la mascota es: {fecha}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        
        from datetime import date

class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=date.today()
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMedicamento(self,historia, nom_med):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                lista = masc.verLista_Medicamentos()
                for med in lista:
                    if med.verNombre() == nom_med:
                        lista.remove(med)
                        return True
        return False
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 

def verificar_existencia_medicamento_en_lista(lista, nombre_med):
    for m in lista:
        if m.verNombre() == nombre_med:
            return True
    return False

def main():
    servicio_hospitalario = sistemaV()
    
    med1 = Medicamento()
    med1.asignarNombre("Acetaminofen")
    med1.asignarDosis(2)
    
    med2 = Medicamento()
    med2.asignarNombre("Ibuprofeno")
    med2.asignarDosis(2)
    
    med3 = Medicamento()
    med3.asignarNombre("Dolex")
    med3.asignarDosis(2)
    
    listam1 = [med1, med2]
    listam2 = [med2, med1, med3]
    
    mascota1 = Mascota()
    mascota1.asignarHistoria(123)
    mascota1.asignarNombre("Lupita")
    mascota1.asignarPeso(32)
    mascota1.asignarTipo("canino")
   # mascota1.asignarFecha(date.today)
    mascota1.asignarLista_Medicamentos(listam1)
    
    mascota2 = Mascota()
    mascota2.asignarHistoria(1235)
    mascota2.asignarNombre("Rocky")
    mascota2.asignarPeso(32)
    mascota2.asignarTipo("felino")
    #mascota2.asignarFecha(date.today)
    mascota2.asignarLista_Medicamentos(listam2)
    
    print(mascota1.verFecha)
    
    servicio_hospitalario.ingresarMascota(mascota1)
    servicio_hospitalario.ingresarMascota(mascota2)
    
    # sistma=sistemaV()
    while True:
        menu=int(input(f'''
                       \n Número de mascotas en el servicio: {servicio_hospitalario.verNumeroMascotas()}
                       \nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento de mascota 
                       \n7- Salir
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                #fecha=date.today()
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = input(f"Ingrese el nombre del medicamento {i+1}: ")
                    while (verificar_existencia_medicamento_en_lista(lista_med, nombre_medicamentos)):
                        
                        print("Ya existe este medicamento en la lista de la mascota...")
                        nombre_medicamentos = input(f"Ingrese el nombre del medicamento {i+1}: ")
                    
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)                     
                    lista_med.append(medicamento)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                #mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de historia clínica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print(f"La fecha de ingreso de la mascota es: {fecha}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        
        elif menu == 6: # Eliminar medicamento de mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            if servicio_hospitalario.verificarExiste(historia=q):
                medicamento = servicio_hospitalario.verMedicamento(q)
                if medicamento:
                    print("Los medicamentos suministrados son: ")
                    for m in medicamento:   
                        print(f"\n- {m.verNombre()}")
                    m = input("Ingrese nombre del medicamento a eliminar o ingrese 0(cero) para salir: ")
                    while m != "0" and not verificar_existencia_medicamento_en_lista(medicamento, m):
                        print("No existe este medicamento asignado...")
                        m = input("Ingrese nombre del medicamento a eliminar o ingrese 0(cero) para salir: ")

                    if m != "0":
                        if servicio_hospitalario.eliminarMedicamento(q, m):
                            print("Se eliminó el medicamento")
                        else:
                            print("No se pudo eliminar el medicamento")
                else:
                    print("No hay medicamentos para esta mascota.")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
  
        
        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

   
            
            






            

                

