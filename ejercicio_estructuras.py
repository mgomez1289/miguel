accion_uno = "Ya estoy en la entrada del evento"
accion_dos = "Me estoy registrando"

#Estrcutura de control (condicional if o si)
#Permite continuar un flujo (realizar algo) si se cumple una condicion
#Y en ese caso de no cumplirse, se puede o no continuar con otro flujo (hacer otra cosa)
#Esta sentencia (condicional if) va acompañado de los operadores de comparacion
"""
if estructura_datos_uno < estructura_datos_dos
if estructura_datos_uno <= estructura_datos_dos
if estructura_datos_uno > estructura_datos_dos
if estructura_datos_uno >= estructura_datos_dos
if estructura_datos_uno == estructura_datos_dos
if estructura_datos_uno != estructura_datos_dos
"""

#Hay varias maneras de utilizar la sentencia if 
# if simple, if compuesto, if anidado
dato_comparacion = 18
edad = 11
"""
if edad >= dato_comparacion
    print("ingresar, disfrute el evento")
"""

#if compuesto
"""
if edad >= dato_comparacion:
    print("ingresar, disfrutar del evento")
else: 
    print("no ingresar")
"""
boleta = False
#if anidado
if edad >= dato_comparacion and boleta:
    print("ingresar, disfrute el evento")
else:
    print("no ingresar")


opciones = """
localidades
1- VIP
2- Preferencial
3- General
4-Baja
"""
print (opciones)

op = int (input ("escoja una localidad"))

if op is 1:
    print("$500")

elif op is 2:
    print("$400")

elif op is 3:
    print("$200")

elif op is 4:
    print ("$100")


