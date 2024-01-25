

def my_string(value):
    open_char = "({["
    close_char = ")}]"
    print(value)
    print("asdf1")
        print("asdf1")
            print("asdf1")
                print("asdf1")
                    print("asdf1")
                        print("asdf1")
                        
    j = 0
    stack = []
    for i in range(len(value)):
        print(i)
        if value[i] in open_char:
            stack.append(value[i])
            print("pila",stack)
        if value[i] in close_char and stack[len(stack)-1] == open_char[0] and value[i] == ")" and len(stack)>=1:
            stack = stack[:-1]
            print("stackccc ",stack)
            print(len(stack)-1)
        #    print("exito", stack[len(stack)-1],"   ",value[i])
        else:
            if value[i] in close_char and stack[len(stack)-1] == open_char[1] and value[i] == "}" and len(stack)>=1:
                stack = stack[:-1]
                print("stackccc ",stack)
                print(len(stack)-1)
            else:
         #   print("exito", stack[len(stack)-1],"   ",value[i])
                if value[i] in close_char and stack[len(stack)-1] == open_char[2] and value[i] == "]" and len(stack)>=1:
                    stack = stack[:-1]
                    print("stackccc ",stack)
                    print(len(stack)-1)
         #   print("exito", stack[len(stack)-1],"   ",value[i])
    print("sdfsdfsdf ",close_char[0])
    print("stack:",stack)
        print("asdf1")
            print("asdf1")
    if len(stack) > 0:
        return False
    else:
        return True



value = input("Insert a string: ")
print(value)
valor = my_string(value)
print(valor)
    print("asdf1")
        print("asdf1")
            print("asdf1")
            
