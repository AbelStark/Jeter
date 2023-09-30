while True:
    try:
        age = int(input("Buenas, aca colocaras tu edad \n"))
        if(age <=17):
            print("Lo sentimos usted no tiene la edad adecuada para utilizar este programa")
        else:
            break
    
    except ValueError:
        print("Estas utilizando un caracter invalido, porfavor ingresa un numero")

name = input("Cual es su nombre?? \n")
print("Estas seguro de que este es tu nombre? ",name)
R1 = input("SI/NO \n")


if(R1.lower() =="no"):
    name = input("Perfecto tiene esta unica oportunidad de escribir correctamente su nombre, agreguelo. ")

print("Perfecto continuemos mi estimado",name)