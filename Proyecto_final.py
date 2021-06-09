#importar librerías
import json

#función para registro
def registro(Usuarios):
    nuevo_usuario = []
    #Se solicita nombre y apellido
    Nombre_y_apellido = input("Digita tu(s) nombre(s) y apellido(s): ")
    nuevo_usuario.append(Nombre_y_apellido)
    #Identificar que el Id sea nuevo
    lista_de_Ids = []
    #Añadir Ids a la lista 
    for fila in Usuarios:
        lista_de_Ids.append(fila[1])
    #Intentar convertir a entero
    while True:
        try:
            Id = int(input("Digite su número de identificación: "))
            #Verificar que Id no exista
            while Id in lista_de_Ids:
                print("Este Id ya existe")
                Id = int(input("Digite su número de identificación: "))
            break
        except:
            print("Debes digitar un Id válido")
    nuevo_usuario.append(Id)
    #Solicitar el tipo de usuario
    Tipo_de_usuario = input("Escribe si eres Estudiante, Profesor o Personal Administrativo: ")
    while Tipo_de_usuario != "Estudiante" and Tipo_de_usuario != "Profesor" and Tipo_de_usuario != "Personal Administrativo":
        print("Digita bien tu rol en la PUJ")
        Tipo_de_usuario = input("Escribe si eres Estudiante, Profesor o Personal Administrativo: ")
    nuevo_usuario.append(Tipo_de_usuario)
    #Solicitar Placa
    Placa = input("Digita la placa de tu vehículo: ")
    nuevo_usuario.append(Placa)
    #Solicitar Tipo de vehículo
    Tipo_de_vehiculo = input("Digita el tipo de vehículo que manejas; Automóvil, Eléctrico, Motocicleta, Discapacitado :")
    while Tipo_de_vehiculo != "Automóvil" and Tipo_de_vehiculo != "Eléctrico" and Tipo_de_vehiculo != "Motocicleta" and Tipo_de_vehiculo != "Discapacitado":
        print("Digite bien el tipo de vehículo")
        Tipo_de_vehiculo = input("Digita el tipo de vehículo que manejas; Automóvil, Eléctrico, Motocicleta, Discapacitado :")
    nuevo_usuario.append(Tipo_de_vehiculo)
    #Solicitar plan de pago
    Plan_de_pago = input("¿Desea pagar por Mensualidad o Diaro?: ")
    while Plan_de_pago != "Mensualidad" and Plan_de_pago != "Diario":
        print("Digite bien su plan de pago")
        Plan_de_pago = input("¿Desea pagar por Mensualidad o Diaro?: ")
    nuevo_usuario.append(Plan_de_pago)
    #añadir nuevo usuario a matriz de usuarios
    Usuarios.append(nuevo_usuario)
    #Devolver matriz de usuarios YA CON EL NUEVO USUARIO AÑADIDO
    return Usuarios

#función para entrar al parqueadero
def entrada(Usuarios,lista_de_parqueados,piso_1,piso_2,piso_3,piso_4,piso_5,piso_6,piso_1_ocupacion,piso_2_ocupacion,piso_3_ocupacion,piso_4_ocupacion,piso_5_ocupacion,piso_6_ocupacion):
    print("Bienvenido al parqueadero de la PUJ")
    #Solicitar placa y revisar si esta registrada o no
    placa = input("Digite la placa de su vehículo: ")
    #ver que placa no esté en la lista de los que ya están adentro
    lista_de_placas_parqueadas = []
    for fila in lista_de_parqueados:
        lista_de_placas_parqueadas.append(fila[3])
    if placa in lista_de_placas_parqueadas:
        print("Este vehículo ya está dentro del parqueadero")
        return lista_de_parqueados, None,None
    #ver si la placa es de alguien registrado en el sistema o si es visitante
    lista_de_placas = []
    for fila in Usuarios:
        lista_de_placas.append(fila[3])
    #Caso donde la placa sí estaba registrada
    if placa in lista_de_placas:
        posicion_placa = lista_de_placas.index(placa)
        Tipo_de_vehiculo = Usuarios[posicion_placa][4]
        lista_de_parqueados.append(Usuarios[posicion_placa])
    #caso donde es visitante
    else:
        Tipo_de_vehiculo = input("Digita el tipo de vehículo que manejas; Automóvil, Eléctrico, Motocicleta, Discapacitado :")
        while Tipo_de_vehiculo != "Automóvil" and Tipo_de_vehiculo != "Eléctrico" and Tipo_de_vehiculo != "Motocicleta" and Tipo_de_vehiculo != "Discapacitado":
            print("Digite bien el tipo de vehículo")
            Tipo_de_vehiculo = input("Digita el tipo de vehículo que manejas; Automóvil, Eléctrico, Motocicleta, Discapacitado :")
        lista_de_parqueados.append([None,None,"Visitante",placa,Tipo_de_vehiculo,"Diario"])
    #Mostrar cantidad de disponibles por piso
    lista_de_pisos_disponibles = []
    disponibles_piso_1 = contar_disponibles_de_piso(piso_1,piso_1_ocupacion,Tipo_de_vehiculo)
    disponibles_piso_2 = contar_disponibles_de_piso(piso_2,piso_2_ocupacion,Tipo_de_vehiculo)
    disponibles_piso_3 = contar_disponibles_de_piso(piso_3,piso_3_ocupacion,Tipo_de_vehiculo)
    disponibles_piso_4 = contar_disponibles_de_piso(piso_4,piso_4_ocupacion,Tipo_de_vehiculo)
    disponibles_piso_5 = contar_disponibles_de_piso(piso_5,piso_5_ocupacion,Tipo_de_vehiculo)
    disponibles_piso_6 = contar_disponibles_de_piso(piso_6,piso_6_ocupacion,Tipo_de_vehiculo)
    
    #Caso donde no hay disponibles en el piso 1
    if disponibles_piso_1 == 0:
        print("No hay parqueaderos disponibles en el Piso 1")
    #caso donde sí hay disponibles en el piso 1
    else:
        print("La cantidad de disponibles en el Piso 1 es de " + str(disponibles_piso_1))
        lista_de_pisos_disponibles.append("1")
    
    #Caso donde no hay disponibles en el piso 2
    if disponibles_piso_2 == 0:
        print("No hay parqueaderos disponibles en el Piso 2")
    #caso donde sí hay disponibles en el piso 2
    else:
        print("La cantidad de disponibles en el Piso 2 es de " + str(disponibles_piso_2))
        lista_de_pisos_disponibles.append("2")
    
    #Caso donde no hay disponibles en el piso 3
    if disponibles_piso_3 == 0:
        print("No hay parqueaderos disponibles en el Piso 3")
    #caso donde sí hay disponibles en el piso 3
    else:
        print("La cantidad de disponibles en el Piso 3 es de " + str(disponibles_piso_3))
        lista_de_pisos_disponibles.append("3")

    #Caso donde no hay disponibles en el piso 4
    if disponibles_piso_4 == 0:
        print("No hay parqueaderos disponibles en el Piso 4")
    #caso donde sí hay disponibles en el piso 4
    else:
        print("La cantidad de disponibles en el Piso 4 es de " + str(disponibles_piso_4))
        lista_de_pisos_disponibles.append("4")
    
    #Caso donde no hay disponibles en el piso 5
    if disponibles_piso_5 == 0:
        print("No hay parqueaderos disponibles en el Piso 5")
    #caso donde sí hay disponibles en el piso 5
    else:
        print("La cantidad de disponibles en el Piso 5 es de " + str(disponibles_piso_5))
        lista_de_pisos_disponibles.append("5")
    
    #Caso donde no hay disponibles en el piso 6
    if disponibles_piso_6 == 0:
        print("No hay parqueaderos disponibles en el Piso 6")
    #caso donde sí hay disponibles en el piso 6
    else:
        print("La cantidad de disponibles en el Piso 6 es de " + str(disponibles_piso_6))
        lista_de_pisos_disponibles.append("6")
    
    #el Usuario escoge el piso donde quiere parquear
    piso_deseado = input("Digita el número piso en el que deseas parquear: ")
    while piso_deseado not in lista_de_pisos_disponibles:
        print("Recuerda que en este piso no hay parqueaderos disponibles")
        piso_deseado = input("Digita el número piso en el que deseas parquear: ")
    #Casos de que escoja los pisos - se pide que escoja la posición donde quiere parquear
    if piso_deseado == "1":
        #Se muestra el piso de las 2 formas
        mostrar_piso_deseado(piso_1,piso_1_ocupacion)
        #Se pide la posición donde quiere parquear y se valida que sea válida
        piso_1_ocupacion,lista_de_parqueados = posicion_parqueo(lista_de_parqueados,piso_deseado,piso_1,piso_1_ocupacion,Tipo_de_vehiculo)
        return lista_de_parqueados, piso_1_ocupacion, piso_deseado
    if piso_deseado == "2":
        #Se muestra el piso de las 2 formas
        mostrar_piso_deseado(piso_2,piso_2_ocupacion)
        #Se pide la posición donde quiere parquear y se valida que sea válida
        piso_2_ocupacion,lista_de_parqueados = posicion_parqueo(lista_de_parqueados,piso_deseado,piso_2,piso_2_ocupacion,Tipo_de_vehiculo)
        return lista_de_parqueados, piso_2_ocupacion, piso_deseado
    if piso_deseado == "3":
        #Se muestra el piso de las 2 formas
        mostrar_piso_deseado(piso_3,piso_3_ocupacion)
        #Se pide la posición donde quiere parquear y se valida que sea válida
        piso_3_ocupacion,lista_de_parqueados = posicion_parqueo(lista_de_parqueados,piso_deseado,piso_3,piso_3_ocupacion,Tipo_de_vehiculo)
        return lista_de_parqueados, piso_3_ocupacion, piso_deseado
    if piso_deseado == "4":
        #Se muestra el piso de las 2 formas
        mostrar_piso_deseado(piso_4,piso_4_ocupacion)
        #Se pide la posición donde quiere parquear y se valida que sea válida
        piso_4_ocupacion,lista_de_parqueados = posicion_parqueo(lista_de_parqueados,piso_deseado,piso_4,piso_4_ocupacion,Tipo_de_vehiculo)
        return lista_de_parqueados, piso_4_ocupacion, piso_deseado
    if piso_deseado == "5":
        #Se muestra el piso de las 2 formas
        mostrar_piso_deseado(piso_5,piso_5_ocupacion)
        #Se pide la posición donde quiere parquear y se valida que sea válida
        piso_5_ocupacion,lista_de_parqueados = posicion_parqueo(lista_de_parqueados,piso_deseado,piso_5,piso_5_ocupacion,Tipo_de_vehiculo)
        return lista_de_parqueados, piso_5_ocupacion, piso_deseado
    if piso_deseado == "6":
        #Se muestra el piso de las 2 formas
        mostrar_piso_deseado(piso_6,piso_6_ocupacion)
        #Se pide la posición donde quiere parquear y se valida que sea válida
        piso_6_ocupacion,lista_de_parqueados = posicion_parqueo(lista_de_parqueados,piso_deseado,piso_6,piso_6_ocupacion,Tipo_de_vehiculo)
        return lista_de_parqueados, piso_6_ocupacion, piso_deseado

#función para pedir posición de parqueo
def posicion_parqueo(lista_de_parqueados,piso_deseado,Piso,Piso_ocupacion,Tipo_de_vehiculo):
    print("")
    fila_de_parqueo = int(input("Escribe el número de fila donde quieres parquear: "))
    columna_de_parqueo = int(input("Escribe el número de columna donde quieres parquear: "))
    #verificar que la posición sí sea válida
    validacion = validar_posicion(Piso, Piso_ocupacion, fila_de_parqueo,columna_de_parqueo, Tipo_de_vehiculo)
    while validacion == False:
        print("La posición de parqueo no es válida")
        fila_de_parqueo = int(input("Escribe el número de fila donde quieres parquear: "))
        columna_de_parqueo = int(input("Escribe el número de columna donde quieres parquear: "))
        validacion = validar_posicion(Piso, Piso_ocupacion, fila_de_parqueo,columna_de_parqueo, Tipo_de_vehiculo)
    #se añade al usuario la posición donde parqueó
    lista_de_parqueados[len(lista_de_parqueados)-1].append(piso_deseado)
    lista_de_parqueados[len(lista_de_parqueados)-1].append(fila_de_parqueo)
    lista_de_parqueados[len(lista_de_parqueados)-1].append(columna_de_parqueo)
    #se coloca una X donde parquea
    Piso_ocupacion[fila_de_parqueo][columna_de_parqueo] = "X"
    print("Su parqueo fue exitoso")
    return Piso_ocupacion,lista_de_parqueados

#función para mostrar piso deseado
def mostrar_piso_deseado(Piso,Piso_ocupacion):
    print("")
    print("Aquí puedes ver los parqueaderos donde tu vehículo puede parquear")
    print("Recuerda que: 1: Automovil, 2: Automovil eléctrico, 3: Motocicleta, 4: Discapacitado \n")
    imprimir_matriz(Piso)
    print("Aquí puedes ver la disponibilidad de piso deseado\n")
    imprimir_matriz(Piso_ocupacion)

#función para ver si la posición de parqueo es válifa
def validar_posicion(Piso, Piso_ocupacion, fila_de_parqueo, columna_de_parqueo, Tipo_de_vehiculo):
    casilla_de_parqueo_ocupacion = Piso_ocupacion[fila_de_parqueo][columna_de_parqueo]
    #validar que no sea X
    if casilla_de_parqueo_ocupacion == "X":
        return False
    #Validar que el número coreesponda con el tipo de vehículo
    casilla_de_parqueo = Piso[fila_de_parqueo][columna_de_parqueo]
    if Tipo_de_vehiculo == "Automóvil" and casilla_de_parqueo == 1:
        return True
    elif Tipo_de_vehiculo == "Eléctrico" and (casilla_de_parqueo == 2 or casilla_de_parqueo == 1):
        return True
    elif Tipo_de_vehiculo == "Motocicleta" and casilla_de_parqueo == 3:
        return True
    elif Tipo_de_vehiculo == "Discapacitado" and (casilla_de_parqueo == 4 or casilla_de_parqueo == 1):
        return True
    else:
        return False

#función para contar disponibles por piso
def contar_disponibles_de_piso(Piso,Piso_ocupacion,Tipo_de_vehiculo):
    #Se verifica la cantidad de números que corresponden con el tipo de vehículo
    if Tipo_de_vehiculo == "Automóvil":
        contador_de_disponibles = 0
        for i in range(len(Piso)):
            for j in range(len(Piso[0])):
                if Piso[i][j] == 1 and Piso_ocupacion[i][j] == 0:
                    contador_de_disponibles += 1
    elif Tipo_de_vehiculo == "Eléctrico":
        contador_de_disponibles = 0
        for i in range(len(Piso)):
            for j in range(len(Piso[0])):
                if (Piso[i][j] == 2 or Piso[i][j] == 1) and Piso_ocupacion[i][j] == 0:
                    contador_de_disponibles += 1
    elif Tipo_de_vehiculo == "Motocicleta":
        contador_de_disponibles = 0
        for i in range(len(Piso)):
            for j in range(len(Piso[0])):
                if Piso[i][j] == 3 and Piso_ocupacion[i][j] == 0:
                    contador_de_disponibles += 1
    elif Tipo_de_vehiculo == "Discapacitado":
        contador_de_disponibles = 0
        for i in range(len(Piso)):
            for j in range(len(Piso[0])):
                if (Piso[i][j] == 4 or Piso[i][j] == 1) and Piso_ocupacion[i][j] == 0:
                    contador_de_disponibles += 1

    return contador_de_disponibles

#función de retirar vehículo
def retirar(lista_de_parqueados,piso_1_ocupacion,piso_2_ocupacion,piso_3_ocupacion,piso_4_ocupacion,piso_5_ocupacion,piso_6_ocupacion):
    Placa = input("Digita la placa de tu vehículo: ")
    lista_de_placas = []
    #Se verifica que la placa sí esté en al lista de parqueados
    for i in range(len(lista_de_parqueados)):
        lista_de_placas.append(lista_de_parqueados[i][3])
    if Placa not in lista_de_placas:
        print("Esta placa no está registrada")
        return lista_de_parqueados,None,None
    #se solicita el número de horas que estuvo
    while True:
        try: 
            num_de_horas = float(input("Cuántas horas estuvo parqueado, digite un número: "))
            break
        except:
            print("Escribe el número de horas como un número")
    #Obtener el tipo de pago y el tipo de usuario a partir de la plca
    posicion_placa = lista_de_placas.index(Placa)
    tipo_de_pago = lista_de_parqueados[posicion_placa][5]
    tipo_de_usuario = lista_de_parqueados[posicion_placa][2]
    #se cobra segun la información obtenida
    if tipo_de_pago == "Mensualidad":
        print("No debe realizar ningún pago")
    else:
        if tipo_de_usuario == "Estudiante":
            print("Debes pagar $" + str(num_de_horas * 1000))
        elif tipo_de_usuario == "Profesor":
            print("Debes pagar $" + str(num_de_horas * 2000))
        elif tipo_de_usuario == "Personal Administrativo":
            print("Debes pagar $" + str(num_de_horas * 1500))
        else:
            print("Debes pagar $" + str(num_de_horas * 3000))
    #cambiar X por 0 de donde se fue 
    piso_de_parqueo = lista_de_parqueados[posicion_placa][len(lista_de_parqueados[posicion_placa])-3]
    fila_de_parqueo = lista_de_parqueados[posicion_placa][len(lista_de_parqueados[posicion_placa])-2]
    columna_de_parqueo = lista_de_parqueados[posicion_placa][len(lista_de_parqueados[posicion_placa])-1]
    if piso_de_parqueo == "1":
        piso_1_ocupacion[fila_de_parqueo][columna_de_parqueo] = 0
        #sacar persona que se fue de la lista de parqueados
        lista_de_parqueados.remove(lista_de_parqueados[posicion_placa])
        return lista_de_parqueados,piso_1_ocupacion,piso_de_parqueo
    
    if piso_de_parqueo == "2":
        piso_2_ocupacion[fila_de_parqueo][columna_de_parqueo] = 0
        #sacar persona que se fue de la lista de parqueados
        lista_de_parqueados.remove(lista_de_parqueados[posicion_placa])
        return lista_de_parqueados,piso_2_ocupacion,piso_de_parqueo
    
    if piso_de_parqueo == "3":
        piso_3_ocupacion[fila_de_parqueo][columna_de_parqueo] = 0
        #sacar persona que se fue de la lista de parqueados
        lista_de_parqueados.remove(lista_de_parqueados[posicion_placa])
        return lista_de_parqueados,piso_3_ocupacion,piso_de_parqueo

    if piso_de_parqueo == "4":
        piso_4_ocupacion[fila_de_parqueo][columna_de_parqueo] = 0
        #sacar persona que se fue de la lista de parqueados
        lista_de_parqueados.remove(lista_de_parqueados[posicion_placa])
        return lista_de_parqueados,piso_4_ocupacion,piso_de_parqueo

    if piso_de_parqueo == "5":
        piso_5_ocupacion[fila_de_parqueo][columna_de_parqueo] = 0
        #sacar persona que se fue de la lista de parqueados
        lista_de_parqueados.remove(lista_de_parqueados[posicion_placa])
        return lista_de_parqueados,piso_5_ocupacion,piso_de_parqueo
    
    if piso_de_parqueo == "6":
        piso_6_ocupacion[fila_de_parqueo][columna_de_parqueo] = 0
        #sacar persona que se fue de la lista de parqueados
        lista_de_parqueados.remove(lista_de_parqueados[posicion_placa])
        return lista_de_parqueados,piso_6_ocupacion,piso_de_parqueo
    
#función de reporte para vehículos parqueados según tipo de usuario
def reporte_1 (lista_de_parqueados):
    filename = str(input("Indica el nombre del archivo donde deseas ver el reporte de la cantidad de vehículos parqueados según el tipo de usuario (sin formato): "))
    filename = filename + ".txt"
    file  =  open (filename,  "w" )
    file.write( "Reporte de cantidad de vehículos según tipo de Usuario: \n \n" )
    contador_estudiantes = 0
    contador_profesores = 0
    contador_personal_administrativo = 0
    contador_visitantes = 0
    for usuario in lista_de_parqueados:
        tipo_de_usuario = usuario[2]
        if tipo_de_usuario == "Estudiante":
            contador_estudiantes += 1
        elif tipo_de_usuario == "Profesor":
            contador_profesores += 1
        elif tipo_de_usuario == "Personal Administrativo":
            contador_personal_administrativo += 1
        elif tipo_de_usuario == "Visitante":
            contador_visitantes += 1
    file.write("La cantidad de Estudiantes parqueados es de: " + str(contador_estudiantes) + "\n")
    file.write("La cantidad de Profesores parqueados es de: " + str(contador_profesores) + "\n")
    file.write("La cantidad de Personal Administrativos parqueados es de: " + str(contador_personal_administrativo) + "\n")
    file.write("La cantidad de Visitantes parqueados es de: " + str(contador_visitantes) + "\n")
    file.close ()
    print("Se ha generado el archivo " + str(filename) + " con la información solicitada \n")

#función de reporte para vehículos parqueados según tipo de usuario
def reporte_2 (lista_de_parqueados):
    filename = str(input("Indica el nombre del archivo donde deseas ver el reporte de la cantidad de vehículos parqueados según el tipo de Vehículo (sin formato): "))
    filename = filename + ".txt"
    file  =  open (filename,  "w" )
    file.write( "Reporte de cantidad de vehículos según tipo de Vehículo: \n \n" )
    contador_auto = 0
    contador_elec = 0
    contador_moto = 0
    contador_disc = 0
    for usuario in lista_de_parqueados:
        tipo_de_vehiculo = usuario[4]
        if tipo_de_vehiculo == "Automóvil":
            contador_auto += 1
        elif tipo_de_vehiculo == "Eléctrico":
            contador_elec += 1
        elif tipo_de_vehiculo == "Motocicleta":
            contador_moto += 1
        elif tipo_de_vehiculo == "Discapacitado":
            contador_disc += 1
    file.write("La cantidad de Automóviles parqueados es de: " + str(contador_auto) + "\n")
    file.write("La cantidad de Automóviles eléctricos parqueados es de: " + str(contador_elec) + "\n")
    file.write("La cantidad de Motocicletas parqueados es de: " + str(contador_moto) + "\n")
    file.write("La cantidad de Discapacitados parqueados es de: " + str(contador_disc) + "\n")
    file.close ()
    print("Se ha generado el archivo " + str(filename) + " con la información solicitada \n")

def reporte_3 (lista_de_parqueados):
    filename = str(input("Indica el nombre del archivo donde deseas ver el reporte del porcentaje de ocupación del parqueadero (sin formato): "))
    filename = filename + ".txt"
    file  =  open (filename,  "w" )
    file.write( "Reporte de porcentaje de ocupación del parqueadero: \n \n" )
    porcentaje_global = 0
    porcentaje_piso_1 = 0
    porcentaje_piso_2 = 0
    porcentaje_piso_3 = 0
    porcentaje_piso_4 = 0
    porcentaje_piso_5 = 0
    porcentaje_piso_6 = 0
    for usuario in lista_de_parqueados:
        piso_de_parqueo = usuario[6]
        if piso_de_parqueo == "1":
            porcentaje_piso_1 += 1
        elif piso_de_parqueo == "2":
            porcentaje_piso_2 += 1
        elif piso_de_parqueo == "3":
            porcentaje_piso_3 += 1
        elif piso_de_parqueo == "4":
            porcentaje_piso_4 += 1
        elif piso_de_parqueo == "5":
            porcentaje_piso_5 += 1
        elif piso_de_parqueo == "6":
            porcentaje_piso_6 += 1
    porcentaje_global = len(lista_de_parqueados) / 550 * 100
    porcentaje_piso_6 = porcentaje_piso_6 / 50 * 100
    file.write("El porcentaje de ocupación global es de: " + str(porcentaje_global) + "% \n")
    file.write("El porcentaje de ocupación del piso 1 es de:" + str(porcentaje_piso_1) + "% \n")
    file.write("El porcentaje de ocupación del piso 2 es de:" + str(porcentaje_piso_2) + "% \n")
    file.write("El porcentaje de ocupación del piso 3 es de:" + str(porcentaje_piso_3) + "% \n")
    file.write("El porcentaje de ocupación del piso 4 es de:" + str(porcentaje_piso_4) + "% \n")
    file.write("El porcentaje de ocupación del piso 5 es de:" + str(porcentaje_piso_5) + "% \n")
    file.write("El porcentaje de ocupación del piso 6 es de:" + str(porcentaje_piso_6) + "% \n")
    file.close ()
    print("Se ha generado el archivo " + str(filename) + " con la información solicitada \n")

#función de imprimir matriz por filas
def imprimir_matriz(matriz):
    print("")
    for fila in matriz:
        print(fila)
    print("")

#Leer archivo de estacionamiento
with open('tiposParqueaderos.json') as file:
    estacionamiento = json.load(file)

#Definir pisos
piso_1 = estacionamiento["Piso1"][:]
#definir pisos con 0s
piso_1_ocupacion = []
for i in range(len(piso_1)):
    piso_1_ocupacion.append([])
    for j in range(10):
        piso_1_ocupacion[i].append(0)

piso_2 = estacionamiento["Piso2"][:]
#definir pisos con 0s
piso_2_ocupacion = []
for i in range(10):
    piso_2_ocupacion.append([])
    for j in range(10):
        piso_2_ocupacion[i].append(0)

piso_3 = estacionamiento["Piso3"][:]
#definir pisos con 0s
piso_3_ocupacion = []
for i in range(10):
    piso_3_ocupacion.append([])
    for j in range(10):
        piso_3_ocupacion[i].append(0)

piso_4 = estacionamiento["Piso4"][:]
#definir pisos con 0s
piso_4_ocupacion = []
for i in range(10):
    piso_4_ocupacion.append([])
    for j in range(10):
        piso_4_ocupacion[i].append(0)

piso_5 = estacionamiento["Piso5"][:]
#definir pisos con 0s
piso_5_ocupacion = []
for i in range(10):
    piso_5_ocupacion.append([])
    for j in range(10):
        piso_5_ocupacion[i].append(0)

piso_6 = estacionamiento["Piso6"][:]
#definir pisos con 0s
piso_6_ocupacion = []
for i in range(5):
    piso_6_ocupacion.append([])
    for j in range(10):
        piso_6_ocupacion[i].append(0)

#Leer archivo de usuarios
with open('usuarios.json') as file:
    usuarios = json.load(file)
#Definir matriz de usuarios
Usuarios = usuarios["usuarios"][:]

#definir matriz de personas parqueadas
lista_de_parqueados = []

while True:
    print("")
    #script para menú
    print("Bienvenido al software del parqueadero de PUJ")
    print("¿Qué desea hacer? \n")
    print("1. Registrarse")
    print("2. Entrar al parqueadero")
    print("3. Salir al parqueadero")
    print("4. Generar reporte de vehículos parqueados según el tipo de usuario")
    print("5. Generar reporte de vehículos parqueados según el tipo de vehículo")
    print("6. Generar reporte de porcentaje de ocupación")
    print("7. Salir del programa \n")

    opcion = input("Digita el número de la opción que deseas ejecutar: ")
    if opcion == "1":
        print("OPCIÓN DE REGISTRO \n")
        Usuarios = registro(Usuarios)
    elif opcion == "2":
        print("OPCIÓN DE ENTRADA \n")
        lista_de_parqueados,piso_ocupacion,piso_deseado = entrada(Usuarios,lista_de_parqueados,piso_1,piso_2,piso_3,piso_4,piso_5,piso_6,piso_1_ocupacion,piso_2_ocupacion,piso_3_ocupacion,piso_4_ocupacion,piso_5_ocupacion,piso_6_ocupacion)
        if piso_deseado == "1":
            piso_1_ocupacion = piso_ocupacion
        elif piso_deseado == "2":
            piso_2_ocupacion = piso_ocupacion
        elif piso_deseado == "3":
            piso_3_ocupacion = piso_ocupacion
        elif piso_deseado == "4":
            piso_4_ocupacion = piso_ocupacion
        elif piso_deseado == "5":
            piso_5_ocupacion = piso_ocupacion
        elif piso_deseado == "6":
            piso_6_ocupacion = piso_ocupacion
        
    elif opcion == "3":
        print("OPCIÓN DE SALIDA \n")
        lista_de_parqueados,piso_ocupacion,piso_deseado = retirar(lista_de_parqueados,piso_1_ocupacion,piso_2_ocupacion,piso_3_ocupacion,piso_4_ocupacion,piso_5_ocupacion,piso_6_ocupacion)
        if piso_deseado == "1":
            piso_1_ocupacion = piso_ocupacion
        elif piso_deseado == "2":
            piso_2_ocupacion = piso_ocupacion
        elif piso_deseado == "3":
            piso_3_ocupacion = piso_ocupacion
        elif piso_deseado == "4":
            piso_4_ocupacion = piso_ocupacion
        elif piso_deseado == "5":
            piso_5_ocupacion = piso_ocupacion
        elif piso_deseado == "6":
            piso_6_ocupacion = piso_ocupacion
    elif opcion == "4":
        reporte_1(lista_de_parqueados)
    elif opcion == "5":
        reporte_2(lista_de_parqueados)
    elif opcion == "6":
        reporte_3(lista_de_parqueados)
    elif opcion == "7":
        print("Gracias por utilizar el sistema \n")
        break
    else:
        print("Debes escoger una opción válida")