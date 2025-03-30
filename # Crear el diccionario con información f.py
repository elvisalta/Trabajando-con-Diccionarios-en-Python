# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y modificar la ciudad
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para la profesión (ya está presente, pero por si se requiere cambiar)
informacion_personal["profesion"] = "Arquitecto"

# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
