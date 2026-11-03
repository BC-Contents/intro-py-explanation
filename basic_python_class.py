"""
PYTHON BASICS CLASS — CODE SUMMARY
Full theory and explanations in: README.md
Run: python3 basic_python_class.py
"""

# 1. VARIABLES, TIPOS Y CONVERSIÓN
name = "Ana"            # str (texto)
age = 25                # int (entero)
height = 1.68           # float (decimal)
is_active = True        # bool (True / False)

print(f"Hello {name}, you are {age} years old and {height}m tall.")
future_age = int("30") + 5    # Conversión de texto (str) a número (int)
print(f"Converted text to number: {future_age}")


# 2. CONDICIONALES (if / elif / else)
grade = 8.5
if grade >= 9:
    print("Outstanding 🌟")
elif grade >= 5:
    print("Passed 👍")
else:
    print("Failed ❌")


# 3. BUCLES (for y while)
print("\nFor loop (from 1 to 3):")
for i in range(1, 4):
    print(f"  Step {i}")

print("While loop (countdown):")
counter = 3
while counter > 0:
    print(f"  {counter}...")
    counter -= 1


# 4. ESTRUCTURAS DE DATOS

# A. Listas (los Arrays de Python: ordenadas y mutables)
fruits = ["apple", "banana"]
fruits.append("kiwi")          # Añade al final
fruits.pop(0)                  # Elimina por índice ('apple')
print(f"\nFruit list: {fruits}")

# B. Diccionarios (pares clave: valor)
student = {
    "name": "Carlos",
    "course": "Python",
    "grade": 9.0
}
student["email"] = "carlos@email.com"              # Añade nueva clave
print(f"Student: {student['name']} | Grade: {student['grade']}")
print(f"City (safe .get): {student.get('city', 'Not provided')}")

# C. Tuplas (inmutables: datos fijos que no deben alterarse)
coordinates = (41.3851, 2.1734)
lat, lon = coordinates         # Desempaquetado (unpacking)
print(f"Fixed tuple: Lat {lat}, Lon {lon}")

# D. Conjuntos / Sets (elementos únicos, sin duplicados)
languages = {"Python", "Java", "Python"}
print(f"Set without duplicates: {languages}")


# 5. FUNCIONES
def calculate_average(grade_list):
    """Returns the average of a list of numbers."""
    return sum(grade_list) / len(grade_list)

my_grades = [8.5, 9.0, 7.5]
print(f"\nAverage grade for {my_grades}: {calculate_average(my_grades):.2f}")


# 6. MINI-EJEMPLO INTEGRADOR (Listas + Diccionarios + Funciones)
students = [
    {"name": "Eva", "grade": 8.5},
    {"name": "Luis", "grade": 4.0},
    {"name": "Marta", "grade": 7.0}
]

print("\n--- Student status ---")
for student_data in students:
    status = "Passed ✔️" if student_data["grade"] >= 5.0 else "Failed ❌"
    print(f"{student_data['name']:<8} -> {student_data['grade']} ({status})")
