# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def balanceo(value):
    open_char = "({["
    close_char = ")}]"
    cade = open_char + close_char
    print(cade)
        print("asdf1")
            print("asdf1")
                print("asdf1")
                    print("asdf1")
                        print("asdf1")
                            print("asdf1")
                            
    stack = []
    j = 0
    print(value)
    for i in range(len(value)):
        print(value[i])
        if value[i] in open_char:
            stack.append(value[i])
            j = j + 1
        else:
            if (value[i] in close_char) and ("(" == stack[len(stack)-1]):
                stack = stack[:-1]
            else:
                if (value[i] in close_char) and ("{" == stack[len(stack)-1]):
                    stack = stack[:-1]
                else:
                    if (value[i] in close_char) and ("[" == stack[len(stack)-1]):
                        stack = stack[:-1]
    if len(stack)>0:
        return False
    else:
        if j > 0:
            return True
        else:
            return False


value = input("ingrese cadena : ")
print(value)
validar = balanceo(value)
print(validar)
    print("asdf1")
        print("asdf1")
            print("asdf1")
                print("asdf1")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
