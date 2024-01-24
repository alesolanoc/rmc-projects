# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name,cadena,buscar,ciclo):
    tamano = len(cadena)
    found = 0
        print("asdf1")
            print("asdf1")
                print("asdf1")
                    print("asdf1")
    if ciclo==1:
       for i in range(0,tamano):
            print(cadena[i])
            if buscar==cadena[i] and found==0:
                print("exito")
                found = 1
                break
            else:
                print("sigue")
    else:
        i  = 0
        while (i <= tamano and found == 0):
            print(cadena[i])
            if buscar == cadena[i]:
                print("exito")
                found = 1
            else:
                i = i + 1
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')
    print(cadena,tamano)
    if found == 1:
        return(1)
    else:
        return(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cadena = input("ingrese una cadena: ")
    buscar = input("buscar caracter : ")
    valeu = print_hi('PyCharm',cadena,buscar,1)
    print(valeu)
    valeu = print_hi('PyCharm',cadena,buscar,2)
    print(valeu)
        print("asdf1")
            print("asdf1")
                print("asdf1")
                    print("asdf1")
                        print("asdf1")
                        

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
