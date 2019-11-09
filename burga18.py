#calculadora nro18
#esta calculadora realiza calculo de la sumatoria de una serie

#declaracion de datos
primer_sumando,ultimo_sumando,nro_de_sumandos,sumatoria_serie=0.0,0.0,0.0,0.0

#calculadora
primer_sumando=2
ultimo_sumando=38
nro_de_sumandos=10
sumatoria_serie=((primer_sumando+ultimo_sumando)*nro_de_sumandos)/2
#mostrar datos
print("primer sumando= ",primer_sumando)
print("ultimo sumando= ",ultimo_sumando)
print("numero de sumandos= ",nro_de_sumandos)
print("sumatoria de la serie= ",sumatoria_serie)
#verificador 1
sumatoria_serie_aumentada=( sumatoria_serie>123)
print("la sumatotia de la serie es aumentada? :",sumatoria_serie_aumentada)
