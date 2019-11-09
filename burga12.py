#calculadora nro12
#esta calculadora realiza calculo de la potencia entregada

#declaracion de datos
potencia_util,potencia_perdida,potencia_entregada=0.0,0.0,0.0

#calculadora
potencia_util=234.3
potencia_perdida=24.6
potencia_entregada=(potencia_util+potencia_perdida)
#mostrar datos
print("potenia util= ",potencia_util)
print("potencia perdida= ",potencia_perdida)
print("potencia entregada= ",potencia_entregada)
#verificador
potencia_entregada_disminuida=( potencia_entregada <456 )
print("la potencia de un maquina es disminuida ? :",potencia_entregada_disminuida)
