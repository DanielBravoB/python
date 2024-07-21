# if else
edad = 18
'''
------------------------
OPERADORES COMPARATIVOS |
------------------------
>= --- Mayor o igual que
<= --- Menor o igual que
<  --- Menor que
>  --- Mayor que
=  --- Igual que
!= --- Diferente que
'''

if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

# if elif else
if edad >= 18:
    print("Es mayor de edad")
elif edad == 15:
    print("Es igual a 15")
else:
    print("No es mayor de edad")

'''
-------------------
OPERADORES LOGICOS |
-------------------
and | y
or | o
not | no (Negacion)

if edad == 17 and edad >= 18
'''

# Inputs
edad2 = int(input("Inserte su edad: "))
if edad2 >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")