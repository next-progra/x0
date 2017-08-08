'''
Created on 28 jul. 2017

@author: Sandoval_Santos
'''
from pip._vendor.distlib.compat import raw_input
"""frase=input("escribir un numero: ") 



def palindromo(frase):
   # frase=frase.replace(' ', '')
    if frase==frase[::-1]:
        print("es palindromo " + frase)
    else:
        print("no es palindrono "+ frase)


print(palindromo(frase))"""

"""resp="si"
while (resp!="no"):
    print("ingresa el nombre del alumno: ")
    nom=input()
    num_cal=int(input("cuatas calificaciones vas a promediar: "))
    suma=0
    for i in range (1,int(num_cal+1)):
        calificacion=raw_input("ingresa la "+str(i)+"a calificacion: ")
        calificacion=float(calificacion)
        suma+=calificacion
    promedio=suma/num_cal
    if promedio>=7:
        print("alumno aprobado "+promedio)
    else:
        print("el alumno reprobo "+str(promedio))
    resp=raw_input("deseas agregar otro alumno: (si/no)? ")"""
    
print("calculo del indice de masa corporal")
peso=float(input("cuanto pesa en (Kg): "))
altura=float(input("cuanto mide en (metros): "))
altura2=altura*altura
respuesta=peso/altura2
if respuesta<=18:
    print("peso: bajo desnutricion, su IMC es "+str(respuesta))
elif 18<respuesta<24.9:
    print("peso: normal, su IMC es "+str(respuesta))
elif 25<respuesta<27:
    print("peso: obesidad, su IMC es "+str(respuesta))
elif 27>=respuesta<29.9:
    print("peso: obesidad grado I Riesgo relativo alto, su IMC es "+str(respuesta))
elif 30<respuesta<39.9:
    print("peso: obesidad grado II Riesgo relativo muy alto, su IMC es "+str(respuesta))
elif respuesta>40:
    print("peso : obesidad grado III Riesgo relativo extremadamente alto, su IMC es "+str(respuesta))
#funciona todo

    
    
    

