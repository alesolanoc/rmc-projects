


print('hola')
mensaje = input('ingrese mensaje')
print(mensaje)
numero = int(input('ingrese numero'))
print(numero)
val = numero + 1
print(val)
    print("asdf1")
        print("asdf1")
            print("asdf1")
                print("asdf1")
                
if (val==1):
    print(val)
else:
    print('error')

list=[]
list.append(1)
print(list)
list.append(2)
print(list)
list.append('asdf')
print(list)
for x in list:
    if (x==2):
        print(x)
i=0
while i<10:
    print(i)
    i=i+1
print(len(list))

def sumna(a,b):
    if a>b:
        print('a es menor q b')
    else:
        print('b es mayor q a')
    t=a+b
    return t

a= int(input('ingrese a'))
b=int(input('ingrese b'))
c=sumna(a,b)
print(c)

list=[1,2,3,4,5]
for element in list:
    print(element)
for elem in range(2,3):
    print(elem)

ii=0
while ii<10:
    print(ii)
    if ii==3:
        break
    ii=ii+1

jj=0
while jj<10:
    print(jj)
    jj=jj+1
    if jj==7:
        continue
    print(jj)

kk=0
while kk<10:
    print(kk)
    kk+=1
else:
    print('ter,imo')

values = range(4)

# iterate from i = 0 to i = 3
for i in values:
    print(i)
else:
    print('termino')

for i in range(10,20):
    print(i)
else:
    print('terminosd')

lista=[1,2,3,4,5,6,7,8]
i=1
for ele in lista:
    if (i % 2) == 0:
        print('par')
        print(lista[i-1])
    i+=1

def cadena(cadena,cad1,cad2,num):
    print('cadena %s %s %s %i'%(cadena,cad1,cad2,num))
cadena('alejo','asdf','dfgggg',12)

cade=[1,2,3,4,5,6,7]
i=0
while i<len(cade):
    print(cade[i])
    if i==0:
        first=cade[i]
    if i==len(cade)-1:
        last=cade[i]
    i += 1
cade[0]=last
cade[i-1]=first
print(cade)

list=[4,6,2,7,9,1,5]
i=0
while i<len(list):
    j=i+1
    while j<len(list):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
        j=j+1
    i=i+1
print(list)
    print("asdf1")
        print("asdf1")
            print("asdf1")
            

list1=[4,6,2,2,9,1,9]
i=0
while i<len(list1):
    j=i+1
    while j<len(list1):
        if list1[i]>list1[j]:
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
        j=j+1
    i=i+1
i=0
j=0
print('sfe')
print(list1)
lista=[]
lista.append(list1[i])
while i<len(list1):

    if list1[i]!=lista[j]:
        lista.append(list1[i])
        j = j + 1

    i = i +1
 #   i=i+1
print(lista)



list1=[4,6,2,2,9,1,9]
i=0
while i<len(list1):
    j=i+1
    while j<len(list1):
        if list1[i]>list1[j]:
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
        j=j+1
    i=i+1
i=0
j=0
print('solo repetidos')
print(list1)
lista=[]
while i<len(list1)-1:
   if list1[i]==list1[i+1]:
        lista.append(list1[i])
   i = i +1
 #   i=i+1
print(lista)
    print("asdf1")
        print("asdf1")
            print("asdf1")
                print("asdf1")
                


print('invierte lista')
list1=[4,6,2,2,9,1,9]
i=0
lista2=[]
tam=len(list1)-1
while i<len(list1):
    lista2.append(list1[tam])
    tam = tam -1
    i=i +1
print(lista2)

print('invierte frase')
cadena='hola mi nombre es juan'
oracion=[]
i=0
while i<len(cadena):
    j=i
    subcadena=[]
    while cadena[j]!=' ' and j<len(cadena):
        subcadena.append(cadena[j])
        j = j +1
        i = j
        if j==len(cadena):
            break
    print(subcadena)
    t=0
    tamano=len(subcadena)-1
    subcadena1=[]
    while t<len(subcadena):
        subcadena1.append(subcadena[tamano])
        tamano = tamano-1
        t+=1
    i=i +1
    oracion.append(subcadena1)
print(oracion)
i=0
stri=""
while i<len(oracion):
  #  stri = stri+oracion[i]
    print(oracion[i])
    j=0
    while j<len(oracion[i]):
        stri=stri+oracion[i][j]
        print(oracion[i][j])
        j=j+1
    stri = stri + " "
    i=i+1
print(stri)


class person:
    name='juan'
p1=person
print(p1.name)


class person1:
    def __init__(self,name,edge):
        self.name=name
        self.edge=edge
p1 = person1('juan',12)
print(p1.name," ",p1.edge)
print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

class person2:
    def __init__(self,name,edge):
        self.name = name
        self.edge = edge
    def func1(self):
        print('hola, soy ',self.name)
p1=person2('jan',324)
p1.func1()


class person2:
    def __init__(self,name,edge):
        self.name = name
        self.edge = edge
    def func1(self):
        print('hola, soy ',self.name)
p1=person2('jan',324)
p1.edge=4
print(p1.edge)


class person3:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname)
class doctor(person3):
    pass
p1 = person3("jasdf","aaa")
p1.printname()
doc = person3("jose","perez")
doc.printname()



