#la empresa de panelitas adriana y caro sas quieren saber cual es el porcentaje de ganancias
# sabiendo que producir 1 unidad es 100 pesos, la entrada es el numero de unidades vendidas y el valor de venta
#la salide debe ser formateada y debe decirnos el porcentaje de ganancia(o perdida)
unidadesVendidas = int(input("Ingrese unidades vendidas de panelitas: "))
valorVenta = int(input("Ingrese valor de panelitas ala venta: "))
costo = 100
# costo total= multiplicar las unidades vendidas * costo
costo_total = unidadesVendidas * costo

# ganancia = multiplicar unidades vendidas * valor de venta
ganancia = unidadesVendidas * valorVenta

# ganancia - costo total
ganancia_efectiva = ganancia - costo_total

# porcentaje=  costo total *100 / ganancia
porcentaje = (ganancia_efectiva/costo_total) *100


print(f"el porcentaje obtenido es: {porcentaje}%")
print(f"el dinero restante es: {ganancia_efectiva}")
