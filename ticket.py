incidente = {"id_incidente":1,
                  "fecha":"2026-07-12",
                  "ip_origen":"192.168.17.83",
                  "tipo_ataque":"Phishing",
                  "nivel_riesgo":2,
                  "puerto_afectado":123,
                  "resuelto":False
                  }

print(type(incidente))

evidencias = ["Tráfico inusual a las 03:14","Servidor 123 ha estado fuera de red por 15 minutos","Se tuvo que dar un reinicio al sistema"]

print(type(evidencias))

incidente["evidencias"] = evidencias ## Agregar la lista evidencias al diccionario

print(incidente)

sistemas_comprometidos = {"Avalon","Valhalla","Cosmos"}
print(type(sistemas_comprometidos))

incidente["sistemas_comprometidos"] = sistemas_comprometidos
## Agregar el set al diccionario

print(incidente)

coordenadas_red = ("192.168.1.0","255.255.255.1")
print(type(coordenadas_red))

incidente["coordenadas_red"] = coordenadas_red ##Agregar la tupla al diccionario
print(incidente)

print(incidente["ip_origen"])
print(incidente["tipo_ataque"])
print(incidente["evidencias"][0])
print(incidente["sistemas_comprometidos"])

incidente["resuelto"] = True
print(incidente["resuelto"])

analista_cierre = "lie_sanchez"

incidente["analista_cierre"] = analista_cierre
print(incidente)

incidente["evidencias"].append("Acceso no autorizado detectado en puerto 123")

print(incidente)
