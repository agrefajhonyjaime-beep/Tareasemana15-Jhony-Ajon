# Tarea: colecciones de datos
# Agenda de contactos creada con un diccionario
 
contactos = {
    "Ana López": "0991112233",
    "Carlos Pérez": "0982223344",
    "María Torres": "0973334455",
    "Luis García": "0964445566",
    "Sofía Ramírez": "0955556677"
}
 
 
def agregar_contacto():
    nombre = input("Ingrese el nombre: ").strip()
    telefono = input("Ingrese el teléfono: ").strip()
 
    if nombre == "" or telefono == "":
        print("Error: el nombre y el teléfono son obligatorios.")
    elif nombre in contactos:
        print("Ese nombre ya está registrado.")
    else:
        contactos[nombre] = telefono
        print("Contacto agregado correctamente.")
 
 
def mostrar_contactos():
    print("\n--- CONTACTOS REGISTRADOS ---")
 
    if len(contactos) == 0:
        print("No hay contactos registrados.")
        return
 
    for nombre, telefono in contactos.items():
        print(f"{nombre}: {telefono}")
 
 
def buscar_contacto():
    nombre = input("Ingrese el nombre que desea buscar: ").strip()
 
    if nombre in contactos:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {contactos[nombre]}")
    else:
        print("No se encontró ese contacto.")
 
 
def eliminar_contacto():
    nombre = input("Ingrese el nombre que desea eliminar: ").strip()
 
    if nombre in contactos:
        del contactos[nombre]
        print("Contacto eliminado correctamente.")
    else:
        print("No se encontró ese contacto.")
 
 
def main():
    while True:
        print("\n===== AGENDA DE CONTACTOS =====")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
 
        opcion = input("Seleccione una opción: ").strip()
 
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Escriba un número del 1 al 5.")
 
 
if __name__ == "__main__":
    main ()
