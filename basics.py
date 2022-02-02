###### Print
# name = "Robbie"
# print(name)

####################
###### Get data type
####################

# print(type("Robbie"))
# print(type(123))
# print(type(1.23))
# print("Hola" + "Robbie")

##################
###### Conversions
#################

# base = 6
# height = 3
# area = (base * height) / 2
# print("The area is: " + str(area))

################
###### Functions
################

# def saludo(name):
#     print("Hola " + name)

# saludo("Robbie")


# def convertirSegundos(segundos):
#     horas = segundos // 3600
#     minutos = (segundos - horas * 3600) // 60
#     restante = segundos - horas * 3600 - minutos * 60
#     return horas, minutos, restante

# horas, minutos, segundos = convertirSegundos(5000)
# print(horas, minutos, segundos)

# def lenNombre(nombre):
#     if len(nombre) < 3:
#         print(nombre)
#     elif len(nombre) < 5:
#         print(nombre + str(len(nombre)))
#     else:
#         print("Muy grande")

# lenNombre("Robbie")

############
###### Loops
############

# x = 0
# while x < 5:
#     print("Aun no, x= " + str(x))
#     x += 1
# print("x = " + str(x))

# for x in range(1, 10, 2):
#     print(x)

# friends = ['Robbie', 'Joseph', 'Annie']
# for friend in friends:
#     print(friend)

# for left in range(7):
#     for right in range(left, 7):
#         print("[" + str(left) + "|" + str(right) + "]", end=" ")
#     print()

# teams = ['gryffindor', 'slytheryn', 'ravenclaw', 'huffelpuff']
# for casa in teams:
#     for visita in teams:
#         if casa != visita:
#             print(casa + " vs " + visita)

###############
##### Strings
###############

# name = "Robbie"
# print(name[0])
# print(name[-1])
# print(name[1:4])
# print(name[:4])
# print(name[4:])

# frase = "Me gustan los taquitos de suadero :)"
# print(frase.index(":"))
# print("suadero" in frase)

# def reemplazarDominio(email, nuevoDominio, viejoDominio):
#     if "@" + viejoDominio in email:
#         index = email.index("@" + viejoDominio)
#         nuevoCorreo = email[:index] + "@" + nuevoDominio
#         return nuevoCorreo
#     return email

# nombre = " Robbie "
# numero = "123456789"
# print(nombre.upper())
# print(nombre.lower())
# print(nombre.strip())
# print(nombre.lstrip())
# print(nombre.rstrip())
# print(nombre.count("b"))
# print(nombre.endswith("bie "))
# print(nombre.isnumeric())
# print(int("1") + 3)

# print(" ".join(["Unidos", "con", "un", "join", "separados", "por", "espacios"]))
# print("Esta es una frase convertida en array".split())

# name = "Robbie"
# number = len(name) * 3.123456
# print("Hello {}, your lucky number is {}".format(name, number))
# print("Hello {}, your lucky number is {:.2f}".format(name, number))

# def celsius(x):
#     return (x-32)*5/9

# for x in range(0,101,10):
#     print("{:>3} F | {:>6.2f} C".format(x, celsius(x)))


#############
##### Listas
#############

# x = ["Hola", "soy", "Robbie"]
# print(x)
# print(len(x))
# print("soy" in x)
# print(x[2])
# print(x[0:2])
# print(x[1:])

# x[2] = "Annie"
# x.append("Fer")
# x.insert(1, "yo")
# x.remove("Hola")
# x.pop(1)
# print(x)

#############
##### Tuplas
#############

# id = ('123', '456', '789')
# uno, dos, tres = id
# print(type(id))
# print(uno)
# print(type(uno))

###################
##### Iterar listas
###################

# animales = ['Leon', 'Zebra', 'Mapache', 'Perro', 'Gato']
# for index, animal in enumerate(animales):
#     print("{} - {}".format(index + 1, animal))

########################
##### List comprehension
########################

# multiples = [x*7 for x in range(1,11)]
# print(multiples)

# languages = ["python", "perl", "ruby", "go", "java", "c"]
# lengths = [len(language) for language in languages]
# print(lengths)

# z = [x for x in range(0,101) if x % 3 == 0]
# print(z)

#################
##### Dictionary
#################

# files = {"jpg":10, "txt":14, "csv":2, "py":23}
# print(files)
# files["txt"] = 8
# print(files["txt"])
# files["cfg"] = 10
# print(files)
# del files["py"]
# print(files)

# for extension in files:
#     print(extension)

# for extension, amount in files.items(): #items for key and item
#     print("{} on {}".format(amount, extension))

# print(files.keys())
# print(files.values())

# def contar(text):
#     result = {}
#     for letter in text:
#         if letter not in result:
#             result[letter] = 0
#         result[letter] += 1
#     return result

# print(contar("Hola, soy Robbie y me gustan los taquitos"))

# ropero = {"shirt":["red","blue","white"], "jeans":["blue","black"]}

# for prenda, colores in ropero.items():
#     for color in colores:
#         print("{} {}".format(color, prenda))


##################
###### Python POO
##################

# print(dir("")) # Print all de methods of the class
# help("") # This works to

# class Apple:
#     color = ""
#     flavor = ""

# golden = Apple()
# golden.color = "yellow"
# golden.flavor = "sweet"
# print(golden.color)

# class Pig:
#     name = "Piggy"
#     def speak(self):
#         print("{} says: oink oink".format(self.name))

# hamlet = Pig()
# hamlet.name = "Hamlet"
# hamlet.speak()

# class Apple:
#     def __init__(self, color, flavor):
#         """ Initialize an Apple by color and flavor """
#         self.color = color
#         self.flavor = flavor
#     def __str__(self):
#         """ If this does not exist the program prints the memory location of the function """
#         return "This is a {} apple and is {}".format(self.color, self.flavor)

# golden = Apple("Yellow", "sweet")
# print("{}, {}".format(golden.color, golden.flavor))
# print(golden)
# help(Apple)

###################
###### Inheritance
###################

# class Fruit:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor

# class Apple(Fruit):
#     pass

# golden = Apple("yellow", "sweet")
# print(golden.flavor)

##############
##### Modules
##############

# import random
# ran = random.randint(1, 10)
# print(ran)

# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now.year)