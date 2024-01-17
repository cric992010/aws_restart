"""
Your module description
numero1 = int(input("Ingresa un numero "))

numero2 = int(input("Ingresa el siguiente numero "))

total = numero1 + numero2
print(f"el resultado es {total}")
"""




peliculas = [
    "Titanic",
    "Avatar",
    "El Padrino",
    "Pulp Fiction",
    "Forrest Gump",
    "Matrix",
    "Interestelar",
    "Jurassic Park",
    "La La Land",
    "Star Wars: Episodio IV - Una nueva esperanza",
    "Harry Potter y la piedra filosofal",
    "Los Vengadores",
    "Gladiador",
    "El Señor de los Anillos: La Comunidad del Anillo",
    "El Rey León",
    "Batman: El Caballero de la Noche",
    "E.T. el Extraterrestre",
    "Toy Story",
    "Mad Max: Furia en la carretera",
    "Inception",
    "El Resplandor",
    "El Silencio de los Corderos",
    "Coco",
    "Rocky",
    "La La Land",
    "Buscando a Nemo"
]
print(peliculas[2])

numero1 = int(input("Ingresa un numero al azar :v y te dare una pelicula del 1 al 30  "))
numero1 -= 1
tupelicula = peliculas[numero1] 

print(tupelicula)