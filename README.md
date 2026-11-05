# Clase Básica de Python: Guía y Ejemplos Prácticos

Bienvenido a la guía introductoria de Python. Este documento reúne todas las explicaciones teóricas, sintaxis y buenas prácticas correspondientes a la clase básica, sirviendo como manual de referencia para el archivo de código ejecutable [`basic_python_class.py`](./basic_python_class.py).

---

## 🚀 Cómo ejecutar los ejemplos

Para ejecutar el archivo con todos los ejemplos prácticos en la terminal:

```bash
python3 basic_python_class.py
```

---

## 📚 Índice de Contenidos

1. [Variables, Tipos de Datos y Conversión](#1-variables-tipos-de-datos-y-conversión)
2. [Operadores Aritméticos, Relacionales y Lógicos](#2-operadores-aritméticos-relacionales-y-lógicos)
3. [Control de Flujo: Condicionales (`if`, `elif`, `else`)](#3-control-de-flujo-condicionales)
4. [Bucles e Iteraciones (`while`, `for`, `range`)](#4-bucles-e-iteraciones)
5. [Estructuras de Datos: Diccionarios, Listas, Tuplas y Sets](#5-estructuras-de-datos)
   - [Diccionarios en Detalle](#a-diccionarios-dict)
   - [Listas](#b-listas-list)
   - [Tuplas](#c-tuplas-tuple)
   - [Conjuntos / Sets](#d-conjuntos-set)
6. [Funciones (`def`, parámetros y retorno)](#6-funciones)
7. [Proyecto Práctico Integrador](#7-proyecto-práctico-integrador)

---

## 1. Variables, Tipos de Datos y Conversión

### ¿Qué es una variable?
Una variable es un contenedor en la memoria del ordenador para almacenar un dato identificado por un nombre. En Python:
- **Tipado dinámico**: No necesitas indicar el tipo de dato al declarar la variable; Python lo detecta automáticamente.
- **Sensible a mayúsculas**: `edad` y `Edad` son dos variables distintas.
- **Nomenclatura**: Por convención (PEP 8), se utiliza `snake_case` (letras minúsculas separadas por guion bajo: `nombre_completo`).

### Tipos de datos primitivos
| Tipo | Nombre técnico | Descripción | Ejemplo |
|---|---|---|---|
| Entero | `int` | Números sin decimales | `42`, `-5`, `0` |
| Flotante / Decimal | `float` | Números reales con coma decimal | `3.14`, `-0.001` |
| Cadena de texto | `str` | Texto delimitado por comillas (`'` o `"`) | `"Hola Mundo"` |
| Booleano | `bool` | Valores de verdad | `True`, `False` |

### Inspección y Conversión de Tipos (*Type Casting*)
- `type(variable)`: Devuelve el tipo de dato de una variable.
- `int("10")`: Convierte texto a entero.
- `float("19.99")`: Convierte texto a flotante.
- `str(123)`: Convierte cualquier dato a cadena de texto.

### Entrada y Salida
- **Salida (`print`)**: Muestra información en pantalla. Con **f-strings** (`f"Hola {nombre}"`) podemos interpolar variables de forma clara y legible.
- **Entrada (`input`)**: Captura texto introducido por el usuario desde el teclado.
  > **Nota Importante**: `input()` **siempre** devuelve una cadena (`str`). Si necesitas realizar cálculos numéricos con lo introducido, debes convertirlo explícitamente usando `int()` o `float()`.

---

## 2. Operadores Aritméticos, Relacionales y Lógicos

### Operadores Aritméticos
| Operador | Operación | Ejemplo | Resultado |
|---|---|---|---|
| `+` | Suma | `10 + 3` | `13` |
| `-` | Resta | `10 - 3` | `7` |
| `*` | Multiplicación | `10 * 3` | `30` |
| `/` | División real (con decimales) | `10 / 3` | `3.3333...` |
| `//` | División entera (trunca el resultado) | `10 // 3` | `3` |
| `%` | Módulo (resto de la división) | `10 % 3` | `1` (clave para calcular pares/impares) |
| `**` | Exponenciación / Potencia | `10 ** 3` | `1000` |

### Operadores Relacionales (Comparación)
Siempre devuelven un valor booleano (`True` o `False`):
- `==` : Igual a
- `!=` : Distinto de
- `<` / `>` : Menor que / Mayor que
- `<=` / `>=` : Menor o igual que / Mayor o igual que

### Operadores Lógicos
Permiten combinar múltiples expresiones booleanas:
- **`and`**: Devuelve `True` solo si **ambas** expresiones son verdaderas.
- **`or`**: Devuelve `True` si **al menos una** de las expresiones es verdadera.
- **`not`**: Invierte el valor de verdad (`not True` es `False`).

---

## 3. Control de Flujo: Condicionales

Las estructuras condicionales dirigen el flujo de ejecución del programa según se cumplan o no determinadas condiciones:

```python
if condicion_1:
    # Se ejecuta si condicion_1 es True
elif condicion_2:
    # Se ejecuta si condicion_1 fue False y condicion_2 es True
else:
    # Se ejecuta si ninguna de las condiciones anteriores fue True
```

### Regla fundamental: La Indentación
En Python, los bloques de código no se abren con llaves `{}` ni palabras como `begin`/`end`. Se delimitan mediante **sangrado/indentación** (habitualmente 4 espacios). Si la indentación es incorrecta, Python generará un error `IndentationError`.

---

## 4. Bucles e Iteraciones

Los bucles permiten repetir una serie de instrucciones varias veces.

### 1. Bucle `while`
Se repite **mientras** una condición sea verdadera.
```python
contador = 1
while contador <= 3:
    print(contador)
    contador += 1
```
*Atención*: Si la condición nunca pasa a ser falsa y no usamos `break`, el bucle se ejecutará de forma infinita.

### 2. Bucle `for` y `range()`
Recorre elementos de una secuencia (colección de datos o un rango numérico).
- `range(stop)`: Genera números de `0` a `stop - 1`.
- `range(start, stop)`: Genera números de `start` a `stop - 1`.
- `range(start, stop, step)`: Permite indicar el paso o incremento (ej. `range(0, 10, 2)` para pares).

### 3. Sentencias de control: `break` y `continue`
- `break`: Termina inmediatamente el bucle.
- `continue`: Salta la iteración actual y pasa a la siguiente.

### 4. Función `enumerate()`
Permite recorrer un elemento iterable obteniendo a la vez su índice (posición numérica) y el valor.

---

## 5. Estructuras de Datos

Python incluye cuatro estructuras de datos nativas esenciales:

### A. DICCIONARIOS (`dict`) ⭐

Un diccionario es una colección no secuencial de elementos organizados en pares **clave: valor** (*key: value*).
- **Claves únicas**: Cada clave debe ser única e inmutable (habitualmente strings o enteros).
- **Acceso ultra-rápido**: Permite buscar valores por su clave instantáneamente.

#### Operaciones habituales con Diccionarios:
1. **Creación**:
   ```python
   alumno = {
       "id": 101,
       "nombre": "Carlos Gómez",
       "curso": "Python Básico",
       "calificaciones": [8.5, 9.0]
   }
   ```
2. **Acceso**:
   - `alumno["nombre"]` : Acceso directo. Lanza error `KeyError` si la clave no existe.
   - `alumno.get("ciudad", "Desconocida")` : Acceso seguro. Si la clave no existe, devuelve el valor por defecto sin fallar.
3. **Modificar y Agregar**:
   - `alumno["curso"] = "Python Avanzado"` (actualiza si existe).
   - `alumno["email"] = "carlos@email.com"` (añade nueva clave si no existe).
4. **Eliminar**:
   - `valor_eliminado = alumno.pop("email")` : Elimina la clave y devuelve su valor.
   - `del alumno["id"]` : Elimina la clave directamente.
5. **Métodos de inspección e iteración**:
   - `alumno.keys()` : Obtiene una vista de las claves.
   - `alumno.values()` : Obtiene una vista de los valores.
   - `alumno.items()` : Obtiene pares de `(clave, valor)` para iterar:
     ```python
     for clave, valor in alumno.items():
         print(f"{clave} -> {valor}")
     ```
6. **Diccionarios anidados**:
   Un valor dentro de un diccionario puede ser otro diccionario, permitiendo representar datos complejos (como registros de una base de datos o JSONs de APIs).

---

### B. LISTAS (`list`) — *El equivalente a los Arrays en Python*

> 💡 **¿Y los Arrays en Python?**
> En otros lenguajes como JavaScript, Java, C o PHP se utiliza el término **Array** (arreglo o vector). En Python, **la estructura equivalente nativa y estándar es la Lista (`list`)**.
> 
> - **Lista de Python (Array dinámico)**: Es la forma habitual de trabajar con arrays en el 99% de los casos. A diferencia de los arrays de C o Java, las listas de Python son dinámicas (crecen o decrecen solas) y pueden mezclar tipos de datos diferentes (enteros, texto, etc.).
> - **Módulo `array` nativo**: Python incluye una librería estándar `import array` para crear arrays homogéneos (todos los elementos del mismo tipo numérico: solo enteros o solo floats) para optimizar memoria.
> - **NumPy Arrays (`numpy.ndarray`)**: En análisis de datos e inteligencia artificial, se usa la biblioteca externa `numpy`, que proporciona arrays multidimensionales ultra-rápidos.

#### Operaciones principales con Listas / Arrays en Python:
- `lista.append(x)`: Añade un elemento al final (equivalente a `push`).
- `lista.insert(pos, x)`: Inserta un elemento en una posición específica.
- `lista.pop()`: Extrae y elimina el último elemento.
- `lista.remove(x)`: Elimina la primera aparición del valor `x`.
- `len(lista)`: Número de elementos (longitud).
- **Acceso por índice**: `lista[0]` (primer elemento), `lista[-1]` (último elemento).
- **Slicing**: `lista[inicio:fin]` obtiene una sublista desde el índice `inicio` hasta `fin - 1`.

---

### C. TUPLAS (`tuple`)
Colección ordenada de elementos que es **inmutable** (no se puede modificar, añadir o borrar una vez creada).
- **Sintaxis**: con paréntesis `coordenadas = (41.3851, 2.1734)` (o incluso sin paréntesis separados por coma).
- **Desempaquetado (*unpacking*)**: Extraer sus elementos a variables individuales de forma directa:
  ```python
  lat, lon = coordenadas
  ```

#### ❓ ¿Cuándo usar Tuplas en lugar de Listas?
> **Regla de oro**: Usa **Listas** para datos que van a cambiar y **Tuplas** para datos fijos que no deben alterarse.

Úsalas principalmente para:
1. **Proteger datos constantes**: Evitar modificaciones por error (ej. coordenadas `(lat, lon)`, colores RGB `(255, 0, 0)`).
2. **Devolver varios valores en una función**: `return min_val, max_val` genera una tupla.
3. **Claves de diccionarios**: Las tuplas sí pueden ser claves (`tablero[(0, 1)] = "peon"`), mientras que las listas no.
4. **Eficiencia**: Ocupan menos memoria y son más rápidas que las listas.

---

### D. CONJUNTOS (`set`)
Colección no ordenada de elementos **únicos** (elimina duplicados automáticamente).
- Sintaxis: `lenguajes = {"Python", "JavaScript", "Python"}` -> Queda solo `{"Python", "JavaScript"}`.
- Operaciones matemáticas de conjuntos:
  - `conjunto_a.intersection(conjunto_b)`: Elementos comunes a ambos.
  - `conjunto_a.union(conjunto_b)`: Todos los elementos de ambos conjuntos.

---

## 6. Funciones

Una función es un bloque de código reutilizable y parametrizable diseñado para resolver una tarea concreta.

### Sintaxis y Componentes:
```python
def calcular_area_rectangulo(base, altura=1.0):
    """
    Calcula el área de un rectángulo dados su base y altura.
    (Esto es un docstring: documentación oficial de la función).
    """
    area = base * altura
    return area
```
- **`def`**: Palabra reservada para definir funciones.
- **Parámetros**: Variables de entrada. Pueden tener valores por defecto (`altura=1.0`).
- **`return`**: Devuelve uno o más valores al código que invocó la función. Si no se indica, devuelve `None`.
- **Ámbito / Scope**: Las variables definidas dentro de una función son **locales** y no existen fuera de ella.

---

## 7. Proyecto Práctico Integrador

En la sección final de [`basic_python_class.py`](./basic_python_class.py), se implementa un **Gestor de Alumnos y Calificaciones** que unifica todos los conceptos:
- Modelado de cada alumno mediante **diccionarios**.
- Colección de registros almacenada en una **lista**.
- **Funciones** para dar de alta alumnos, mostrar listados tabulares y calcular métricas grupales (media de notas, % de aprobados y suspensos).
