from pathlib import Path

games_path = Path("games.csv") # Path establece la ruta
if games_path.exists():       # pregunta si existe 
    print("File found")
else:
    print("File not found")

if games_path.is_file():          # pregunta si es archivo
    print(("It is a file"))
else:
    print(("It is not a file"))

folder_path = Path("data")
if folder_path.is_dir():            # pregunta si es carpeta
    print("It is a folder")
else:
    print("It is not a folder")

new_folder = Path("data/reports")             # crea la ruta 
new_folder.mkdir(parents=True, exist_ok=True)  # con mkdir se crean las carpetas y con parents se crea la primera carpeta si es necesario
 # con exist_ok le decimos que si la carpeta ya esta creada la deje y sino que la cree
report_path = new_folder / "sales.txt"
print(report_path)

print(report_path.name) # imprime nombre completo del archivo
print(report_path.stem) # el nombre sin la extencion "csv o txt" o cualquiera que se use
print(report_path.suffix) # imprime la extencion 
print(report_path.parent) # muestra la carpeta que lo coniene 

report_path.touch()                       # con este se crea el archivo 
if report_path.exists():
    print("Report created")
else:
    print("Report not created")

for item in new_folder.iterdir(): # sirve para recorrer una carpeta y ver su contenido
    print(item.name)

file_path = new_folder / "notes.txt" 
file_path.touch()
file_path = new_folder / "summary.csv"
file_path.touch()

for item in new_folder.glob("*.txt"): # este busca coincidencia dentro de la carpeta 
    print(item.name)

for item in folder_path.rglob("*.txt"): # este busca coincidencias dentro de todas la carpeta y subcarpetas
    print(item.name)

old_name = new_folder / "notes.txt"
new_name = new_folder / "python_notes.txt"
old_name.rename(new_name) 

file_path = new_folder / "summary.csv"
if file_path.exists():
    file_path.unlink()
    print("File deleted")
else:
    print("File not found")

test_folder = Path("temporary")
test_folder.mkdir(exist_ok=True)
if test_folder.is_dir():
    test_folder.rmdir()
    print("Folder deleted")

current_folder = Path.cwd()
print(current_folder)

print(report_path.resolve()) 

file_path = Path("data / report.txt")

