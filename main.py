
# Dicho codigo esta hecho en forma de "Script" para ejecutar las demas ramas de acuerdo
# a la solicitud del usuario. Basta con descargar los archivos correspondientes y ejecutar
# este codigo asegurandose que esten descargados todos los archivos en la misma carpeta ##
            # elaborado por Nicolas Ballesteros ## 


                                            # main.py
from Rama1 import union_lenguajes
from Rama2 import interseccion_lenguajes
from Rama3 import concatenacion_lenguajes

def parsear_lenguaje(texto: str) -> set[str]:
    
    # Convierte un texto 'a,b,01' en un conjunto {'a','b','01'}.
     # Soporta ε/epsilon/eps como cadena vacía.
    
    elementos = [t.strip() for t in texto.split(",") if t.strip()]
    return {"" if e in {"ε", "epsilon", "eps"} else e for e in elementos}

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1) Unión de lenguajes (A ∪ B)")
        print("2) Intersección de lenguajes (A ∩ B)")
        print("3) Concatenación de lenguajes (A · B)")
        print("4) Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            A = parsear_lenguaje(input("Ingresa el lenguaje A (ej: a,b,01): "))
            B = parsear_lenguaje(input("Ingresa el lenguaje B (ej: b,c,ε): "))
            resultado = union_lenguajes(A, B)
            print("Resultado A ∪ B =", resultado)

        elif opcion == "2":
            A = parsear_lenguaje(input("Ingresa el lenguaje A: "))
            B = parsear_lenguaje(input("Ingresa el lenguaje B: "))
            resultado = interseccion_lenguajes(A, B)
            print("Resultado A ∩ B =", resultado)

        elif opcion == "3":
            A = parsear_lenguaje(input("Ingresa el lenguaje A: "))
            B = parsear_lenguaje(input("Ingresa el lenguaje B: "))
            resultado = concatenacion_lenguajes(A, B)
            print("Resultado A · B =", resultado)

        elif opcion == "4":
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción no válida, intenta otra vez.")

if __name__ == "__main__":
    menu()
