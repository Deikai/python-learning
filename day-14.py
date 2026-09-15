# Day 14 - Python Lists

languages = ["Python", "JavaScript", "HTML", "CSS"]

# Access elements
print(languages[0])    # Python
print(languages[2])    # HTML
print(languages[-1])   # CSS
print(languages[-2])   # HTML

# Change an element
languages[1] = "Flask"
print(languages)

# Add elements
languages.append("JavaScript")
print(languages)

# Remove by value
languages.remove("HTML")
print(languages)

# Remove the last element
languages.pop()
print(languages)

# Remove by position
languages.pop(1)
print(languages)

# Save the removed element
languages = ["Python", "HTML", "CSS", "JavaScript"]

removed_language = languages.pop()

print(removed_language)
print(languages)

for language in languages:
    print(language)
# aqui importante: o for percorre a lista e imprime cada elemento individualmente.


names = ["Sebastian", "Genesis", "Carlos"]

for name in names:
    print("Hello", name)
#aqui imprime "Hello" seguido del nombre de cada elemento en la lista names.

numbers = [2, 4, 6, 8]

for number in numbers:
    print(number * 2)
# aqui imprime el resultado de multiplicar cada elemento de la lista numbers por 2.

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)
# aqui imprime solo los números pares de la lista numbers, ya que verifica si el residuo de dividir el número entre 2 es igual a 0.

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 != 0:
        print(number)
# aqui imprime solo los números impares de la lista numbers, 
# ya que verifica si el residuo de dividir el número entre 2 no es igual a 0.

languages = ["Python", "HTML", "CSS", "JavaScript"]

print(len(languages))
# aqui imprime la longitud de la lista languages, es decir, el número de elementos que contiene.

languages = ["Python", "HTML", "CSS", "JavaScript"]

if len(languages) >= 4:
    print("You are learning several technologies.")
# aqui verifica si la longitud de la lista languages es mayor o igual a 4. Si es así, 
# imprime el mensaje "You are learning several technologies."

languages = ["Python", "HTML", "CSS", "JavaScript"]

if "Python" in languages:
    print("Python is in the list.")
# aqui verifica si "Python" está en la lista languages. Si es así, 
# imprime el mensaje "Python is in the list."

languages = ["Python", "HTML", "CSS", "JavaScript"]

if "Flask" in languages:
    print("Flask is in the list.")
else:
    print("Flask is not in the list.")
# aqui verifica si "Flask" está en la lista languages. Si es así, 
# imprime el mensaje "Flask is in the list." De lo contrario, imprime "Flask is not in the list."

languages = ["Python", "HTML", "CSS", "JavaScript"]

languages[1:3]  # HTML, CSS
languages[0:2]  # Python, HTML
languages[2:4]  # CSS, JavaScript
languages[:2]   # Python, HTML
languages[2:]   # CSS, JavaScript
# solo se muestran los elementos de la lista según el rango especificado. 
# Por ejemplo, languages[1:3] devuelve los elementos en las posiciones 1 y 2 (HTML y CSS), 
# mientras que languages[:2] devuelve los elementos desde el inicio hasta la posición 1 (Python y HTML).
# hay que agregar print() para que se muestren los resultados en la consola.
# ejemplo: print(languages[1:3]) HTML, CSS

#languages[start:end]
#languages[:2]   # desde el inicio hasta antes de 2
#languages[2:]   # desde 2 hasta el final

numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)
# aqui ordena la lista numbers en orden ascendente y luego imprime la lista ordenada.
# tambien funciona con las palabras, por ejemplo: 
# languages.sort() ordena la lista languages alfabéticamente.

languages = ["Python", "HTML", "CSS", "Python", "JavaScript", "Python"]
languages.count("Python")
# aqui cuenta cuántas veces aparece "Python" en la lista languages.

numbers = [1, 2, 2, 3, 4, 2, 5]

print(numbers.count(2))
# aqui cuenta cuántas veces aparece el número 2 en la lista numbers y luego imprime el resultado.

# sort()    ordena la lista
# count()   cuenta cuántas veces aparece un valor
# reverse() invierte el orden de los elementos en la lista

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)
# aqui invierte el orden de los elementos en la lista numbers y luego imprime la lista invertida.

languages = ["Python", "HTML", "CSS", "JavaScript", "Python"]

print(len(languages))
print(languages.count("Python"))
languages.sort()
for language in languages:
    print(language)
