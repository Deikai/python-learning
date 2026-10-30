file = open("student.txt", "r") # read version larga
content = file.read()
print(content)
file.close()                  # se usa para cerrar

with open("student.txt", "r") as file: # con with no es necesario cerrar porque el programa ya lo hace en automatico
    content = file.read()
    print(content)

with open("languages.txt", "r") as file: 
    language1 = file.readline() # es para leer solo una linea 
    language2 = file.readline()
    print(language1, language2)

with open("languages.txt") as file: # para leer cada linea y recorrerlo con un for
    lines = file.readlines()
    for line in lines:
        print(line)

with open("goal.txt", "w") as file:             # W crea un archivo si no existe y agrega el texto de abajo
    file.write("Become a software developer")

with open("goal.txt", "a") as file:            # "a" es de append y es para agregar al txt que se creo antes 
    file.write("\nLearn Python well")          # "\n" es para agregar un salto de linea en el txt 


goals = [
    "Learn Python",
    "Learn Django",
    "Get a developer job"
]
with open("goals.txt", "w") as file:
    new_goals = []
    for goal in goals:
        new_goals = new_goals + [goal + "\n"]
        # otra forma de resolverlo
        #new_goals.append(goal + "\n")
    
    file.writelines(new_goals)

with open("goals.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

with open("goals.txt", "a") as file:
    file.write("\nLearn Django REST Framework")

