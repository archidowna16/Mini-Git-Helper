import os

def ejecutar_comando(comando):
    print(f"\n👉 Ejecutando: {comando}\n")
    os.system(comando)

def menu():
    while True:
        print("""
========= MINI GIT HELPER =========
1. Inicializar repositorio
2. Añadir archivos
3. Hacer commit
4. Crear y cambiar de rama
5. Conectar con remoto
6. Push al remoto
7. Ver estado
8. Ver historial
0. Salir
""")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejecutar_comando("git init")
        elif opcion == "2":
            ejecutar_comando("git add .")
        elif opcion == "3":
            msg = input("Mensaje del commit: ")
            ejecutar_comando(f'git commit -m "{msg}"')
        elif opcion == "4":
            rama = input("Nombre de la nueva rama: ")
            ejecutar_comando(f"git branch {rama}")
            ejecutar_comando(f"git checkout {rama}")
        elif opcion == "5":
            url = input("URL del repositorio remoto: ")
            ejecutar_comando(f"git remote add origin {url}")
        elif opcion == "6":
            ejecutar_comando("git push -u origin main")
        elif opcion == "7":
            ejecutar_comando("git status")
        elif opcion == "8":
            ejecutar_comando("git log --oneline")
        elif opcion == "0":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción no válida")

if __name__ == "__main__":
    menu()