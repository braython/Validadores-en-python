#calculadora nro20
#esta calculadora realiza calculo del tiempo de encuentro

#declaracion de datos
distancia,velocidad_inicial,velocidad_final,tiempo_de_encuentro=0.0,0.0,0.0,0.0
#calculadora
distancia=98
velocidad_inicial=24
velocidad_final=54
tiempo_de_encuentro=(distancia/(velocidad_inicial+velocidad_final))
#mostrar datos
print("distancia= ",distancia)
print(" velocidad inicial= ",velocidad_inicial)
print("velocidad final=",velocidad_final)
print("tiempo de encuentro= ",tiempo_de_encuentro)
#verificador
tiempo_encuentro_disminuido=( tiempo_de_encuentro <8852)
print("el tiempo de encuetro es disminuido ? :",tiempo_encuentro_disminuido)

