technologies = {
    "Python",
    "Html", 
    "Css",
    "Git",
    "Python", 
    "Html"   
}

technologies.add("JavaScript") # para agregar

technologies.remove("Css") # para eliminar  pero puede dar error si no esta en la lista

if "Git" in technologies:
    print("Git Found")

technologies.discard("React") #esta tambien elimina pero evita el error en caso de que no exista

backend = {
    "Python",
    "Git",
    "SQL",
    "Docker"
}

frontend = {
    "HTML",
    "CSS",
    "JavaScript",
    "Git"
}
common = backend & frontend # busca lo que esta en comun y crea un set
all_technologies = backend | frontend # crea un set con todos los elementos de ambos sin repetir nada 
backend_only = backend - frontend # este devuelve el resultado del primero y elimina las comparaciones en este caso es el "backend"
frontend_only = frontend - backend # misma operacion que el anterior pero diferente resultado
different = backend ^ frontend # este une los 2 sets pero no une los elementos repetidos 

def compare_sets(a, b):
    new = {}
    new["common"] = a & b
    new["all"] = a | b
    new["only_a"] = a - b 
    new["different"] = a ^ b 

    return new

def unique_items(items):
    new = set(items)    
    return new

def count_unique(items):
    new = set(items)
    new = len(new)

    return new 

def common_items(list_a, list_b):
    new = set(list_a) & set(list_b)

    return new

def all_unique_items(list_a, list_b):
    new = set(list_a) | set(list_b)

    return new

def only_in_first(list_a, list_b):
    new = set(list_a) - set(list_b)

    return new

def different_items(list_a, list_b):
    new = set(list_a) ^ set(list_b)

    return new 

def has_common_items(list_a, list_b):
        if set(list_b) & set(list_a): # return bool(set(list_a) & set(list_b)) 
                                    # esta es otra forma para usar menos lineas 
            return True
        else:
            return False

def count_common_items(list_a, list_b):
    common = set(list_a) & set(list_b)
    new = len(common)
    
    return new 

def analyze_lists(list_a, list_b):
    lists = {}

    lists["common_count"] = count_common_items(list_a, list_b) 
    lists["all_unique_count"] = len(all_unique_items(list_a, list_b))
    lists["only_first"] = only_in_first(list_a, list_b)
    lists["different"] = different_items(list_a, list_b)

    return lists

def permission_report(user_a, user_b):
    new = {}

    new["shared"] = common_items(user_a, user_b)
    new["only_a"] = only_in_first(user_a, user_b)
    new["only_b"] = only_in_first(user_b, user_a)
    new["all_permissions"] = all_unique_items(user_a, user_b)

    return new