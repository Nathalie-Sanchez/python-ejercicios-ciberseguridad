logs = [
  {"ip": "192.168.1.10", "usuario": "admin", "estado": "exitoso", "hora": 9},
  {"ip": "192.168.1.10", "usuario": "admin", "estado": "fallido", "hora": 9},
  {"ip": "45.33.32.156", "usuario": "root", "estado": "fallido", "hora": 3},
  {"ip": "45.33.32.156", "usuario": "root", "estado": "fallido", "hora": 3},
  {"ip": "45.33.32.156", "usuario": "root", "estado": "fallido", "hora": 3},
  {"ip": "10.0.0.5", "usuario": "nath", "estado": "exitoso", "hora": 14},
  {"ip": "10.0.0.5", "usuario": "nath", "estado": "exitoso", "hora": 23},
  {"ip": "172.16.0.99", "usuario": "invitado","estado": "fallido", "hora": 2},
  {"ip": "172.16.0.99", "usuario": "invitado","estado": "fallido", "hora": 2},
  {"ip": "10.0.0.5", "usuario": "nath", "estado": "fallido", "hora": 23},
]

## ACCEDER A CADA DICCIONARIO DE LA LISTA
##print(logs[0])

## ACCEDER A UN DATO EN ESPECÍFICO
##print(logs[0]["ip"])

## CREAR UNA FUNCIÓN PARA EXTRAER LOS DATOS NECESARIOS Y LLENAR EL DICCIONARIO

def contador_fallos(logs):
    conteo = {}  ## Creamos un nuevo diccionario vacío

    for registro in logs:    ## Recorre la lista logs completa. En cada vuelta, registro es un diccionario individual.
        if registro["estado"] == "fallido": ## De ese diccionario, accede al valor de la clave "estado" y pregunta si es igual a "fallido". Si es "exitoso", ignora ese registro y pasa al siguiente. Solo nos interesan los fallos.
            ip = registro["ip"]  ## Si pasó el filtro anterior, extrae el valor de la clave "ip" y lo guarda en una variable llamada ip

            if ip in conteo:  ## Este es el contador, verifica si la ip ya existen como clave dentro del diccionario conteo.
                conteo[ip] += 1 ## Si la ip ya existía dentro del diccionario se le suma 1 aa su vaalor actual.
            else:
                conteo[ip] = 1 ## De lo contrario, si aún no existe la guarda en el diccionario con valor 1, porque es el primer intento fallido.
    return conteo 

## CREAR UNA FUNCIÓN PARA REGISTRAR LOS INTENTOS DE ACCESO SOSPECHOSOS

def accesos_sospechosos(conteo, limite):
    filtro = [] ## Creamos una nueva lista llamada filtro para guardar las IPS con intentos de ingreso sospechosos, mayores a 2

    for clave, valor in conteo.items():  ## Verificamos cada clave y valor dentro de cada item del diccionario 
        if valor > limite:  ## Revisa si el valor de cada clave es mayor a 2 
            filtro.append(clave) ## Si lo anterior es correcto agregamos a la nueva listra filtro la clave correspondiente al valor comparado
    return filtro 

## CREAR UNA FUNCIÓN PARA REGISTRAR LOS ACCESOS FUERA DE LOS HORARIOS

def accesos_nocturnos(logs):
    fuera_de_horario = [] ## Creamos una nueva lista

    for registro in logs: ## Verifica cada diccionario dentro de la lista logs
        if registro["hora"] < 6 or registro["hora"] > 22:  ## Si el valor de la clave "hora" que se encuentra en cada registro es menor a 6 o mayor a 22 entonces:
            fuera_de_horario.append(registro) ## Agrega ese registro dentro de una lista nueva 
    return fuera_de_horario


## CREAR UNA FUNCIÓN GENERAR LOS REPORTES EN PANTALLA

def generar_reportes(logs, limite): 
    conteo = contador_fallos(logs) 
    sospechosas = accesos_sospechosos(conteo, limite)
    nocturnos = accesos_nocturnos(logs)

    print("===== REPORTE DE SEGURIDAD =====")
    print(f"Total de registros analizados: {len(logs)}") ## Mostramos en pantalla el total de registros analizados
    
    print("\nIPs sospechosas (más de 2 intentos fallidos):") 
    for ip in sospechosas:  ## Creamos un for que recorra cada ip dentro de la lista de accesos sospechosos
        print(f"  - {ip} → {conteo[ip]} intentos fallidos") ## imprimimos esa ip y el número de veces que intentó acceder
    
    print("\nAccesos fuera de horario (antes 6h o después 22h):")
    for registro in nocturnos:  ## Creamos un for que recorra cada registro dentro de la lista de accesos fuera de horario
        print(f"  - IP: {registro['ip']} | Usuario: {registro['usuario']} | Hora: {registro['hora']}")  ## Imprimimos los valores relacionados a IP, usuario y hora
    
    print("================================")

generar_reportes(logs, 2) # Llamamos la función y ponemos los parámetros





            








