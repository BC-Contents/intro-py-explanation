"""
CLASE BÁSICA DE PYTHON — RESUMEN DE CÓDIGO
Teoría completa y explicaciones en: README.md
Ejecutar: python3 clase_basica_python.py
"""

# 1. VARIABLES, TIPOS Y CONVERSIÓN
nombre = "Ana"         # str (texto)
edad = 25              # int (entero)
altura = 1.68          # float (decimal)
activo = True          # bool (True / False)

print(f"Hola {nombre}, tienes {edad} años y mides {altura}m.")
edad_futura = int("30") + 5    # Conversión de texto (str) a número (int)
print(f"Texto convertido a número: {edad_futura}")


# 2. CONDICIONALES (if / elif / else)
nota = 8.5
if nota >= 9:
    print("Sobresaliente 🌟")
elif nota >= 5:
    print("Aprobado 👍")
else:
    print("Suspenso ❌")


# 3. BUCLES (for y while)
print("\nBucle for (del 1 al 3):")
for i in range(1, 4):
    print(f"  Paso {i}")

print("Bucle while (cuenta atrás):")
contador = 3
while contador > 0:
    print(f"  {contador}...")
    contador -= 1


# 4. ESTRUCTURAS DE DATOS

# A. Listas (los Arrays de Python: ordenadas y mutables)
frutas = ["manzana", "plátano"]
frutas.append("kiwi")          # Añade al final
frutas.pop(0)                  # Elimina por índice ('manzana')
print(f"\nLista de frutas: {frutas}")

# B. Diccionarios (pares clave: valor)
alumno = {
    "nombre": "Carlos",
    "curso": "Python",
    "nota": 9.0
}
alumno["email"] = "carlos@email.com"              # Añade nueva clave
print(f"Alumno: {alumno['nombre']} | Nota: {alumno['nota']}")
print(f"Ciudad (con .get seguro): {alumno.get('ciudad', 'No indicada')}")

# C. Tuplas (inmutables: datos fijos que no deben alterarse)
coordenadas = (41.3851, 2.1734)
lat, lon = coordenadas         # Desempaquetado (unpacking)
print(f"Tupla fija: Lat {lat}, Lon {lon}")

# D. Conjuntos / Sets (elementos únicos, sin duplicados)
lenguajes = {"Python", "Java", "Python"}
print(f"Set sin duplicados: {lenguajes}")


# 5. FUNCIONES
def calcular_media(lista_notas):
    """Devuelve la media de una lista de números."""
    return sum(lista_notas) / len(lista_notas)

mis_notas = [8.5, 9.0, 7.5]
print(f"\nPromedio de notas {mis_notas}: {calcular_media(mis_notas):.2f}")


# 6. MINI-EJEMPLO INTEGRADOR (Listas + Diccionarios + Funciones)
alumnos = [
    {"nombre": "Eva", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0}
]

print("\n--- Estado de alumnos ---")
for al in alumnos:
    estado = "Aprobado ✔️" if al["nota"] >= 5.0 else "Suspenso ❌"
    print(f"{al['nombre']:<8} -> {al['nota']} ({estado})")
