#calculadora nro10
#esta calculadora realiza calculo del campo electrico

#declaracion de datos
fuerza_electrica,carga_electrica,campo_electrico=0.0,0.0,0.0

#calculadora
fuerza_electrica=85
carga_electrica=3
campo_electrico=(fuerza_electrica/carga_electrica)
#mostrar datos
print("fuerza electrica= ",fuerza_electrica)
print("carga electrica= ", carga_electrica)
print("campo electrico= ",campo_electrico)
#verificador
campo_electrico_aumentado=( campo_electrico>45 )
print("el campo electrico es umentado ?:",campo_electrico_aumentado)
