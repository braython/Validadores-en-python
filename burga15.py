#calculadora nro15
#esta calculadora realiza calculo del peso especifico

#declaracion de datos
peso,volumen,peso_espesifico=0.0,0.0,0.0

#calculadora
peso=45
volumen=12
peso_espesifico=(peso/volumen)
#mostrar datos
print("peso= ",peso)
print("volumen= ",volumen)
print("peso especifico= ",peso_espesifico)
#verificador
peso_especifico_reducido=( peso_espesifico <456 )
print("el peso especifico de un cuerpo es reducido ? :",peso_especifico_reducido)
