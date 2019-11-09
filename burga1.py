#calculadora nro1
#esta calculadora realiza el calculo de la velocidad

#declaracion de variables
distancia,tiempo,velocidad=0.0,0.0,0.0

#calculadora
distancia=30
tiempo=6
velocidad=int(distancia/tiempo)

#mostrar datos
print("distancia = ",distancia)
print("tiempo = ",tiempo)
print("velocidad = ", velocidad)

#verificador 1
velocidad_reducidad=( velocidad < 2)
print("la velocidad es reducida  :",velocidad_reducidad)
