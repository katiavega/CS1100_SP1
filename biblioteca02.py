fecha01 = input()
fecha02=input()

cont = 1
if (fecha01[cont] == " "):
    dia01= int(fecha01[cont-1])
    cont = 3
elif (fecha01[cont + 1] == " "):
    dia01= int(fecha01[cont-1]+fecha01[cont])
    cont = 4

if (fecha01[cont] == " "):
    mes01= int(fecha01[cont-1])
    cont = cont + 1
elif (fecha01[cont + 1] == " "):
    mes01= int(fecha01[cont-1]+fecha01[cont])
    cont = cont + 2

anho01= int(fecha01[cont]+fecha01[cont+1]+fecha01[cont+2]+fecha01[cont+3])

cont = 1
if (fecha02[cont] == " "):
    dia02= int(fecha02[cont-1])
    cont = 3
elif (fecha02[cont + 1] == " "):
    dia02= int(fecha02[cont-1]+fecha02[cont])
    cont = 4

if (fecha02[cont] == " "):
    mes02= int(fecha02[cont-1])
    cont = cont + 1
elif (fecha02[cont + 1] == " "):
    mes02= int(fecha02[cont-1]+fecha02[cont])
    cont = cont + 2

anho02= int(fecha02[cont]+fecha02[cont+1]+fecha02[cont+2]+fecha02[cont+3])


if (anho01 > anho02):
    print(10000)
elif (anho01 == anho02):
    if mes01 > mes02:
        print(500*(mes01-mes02))
    elif mes01 == mes02 and dia01 > dia02:
        print (15*(dia01-dia02))
    elif mes01 <= mes02 and dia01 <=dia02:
        print(0)
