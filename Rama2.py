# Rama 2: Ejercicio de interseccion de Lenguajes
#Grupo A // Lenguas y Atomatas // 2025
# Elaborado por Ethan Torres a base de consultas y cooperacion con otros ejercicios 

def interseccion_lenguajes(L1, L2):
    """Calcula la intersección de dos lenguajes (conjuntos)."""
    return L1.intersection(L2)

def interseccion_multiple(*lenguajes):
    """Calcula la intersección de múltiples lenguajes."""
    if not lenguajes:
        return set()
    inter = lenguajes[0]
    for lang in lenguajes[1:]:
        inter = inter.intersection(lang)
    return inter

def main():
    # Definición de los lenguajes dados
    L1 = {"a", "b", "ab", "ba"}
    L2 = {"b", "c", "bc", "cb"}
    L3 = {"a", "b", "c"}
    L4 = {"ab", "ac"}
    L5 = {"b", "bc", "ca", "c"}

    # 1. L1 ∩ L2
    inter_1_2 = interseccion_lenguajes(L1, L2)
    print("L1 ∩ L2 =", inter_1_2)

    # 2. L1 ∩ L3
    inter_1_3 = interseccion_lenguajes(L1, L3)
    print("L1 ∩ L3 =", inter_1_3)

    # 3. L2 ∩ L3
    inter_2_3 = interseccion_lenguajes(L2, L3)
    print("L2 ∩ L3 =", inter_2_3)

    # 4. L4 ∩ L5
    inter_4_5 = interseccion_lenguajes(L4, L5)
    print("L4 ∩ L5 =", inter_4_5)

    # 5. L1 ∩ L2 ∩ L3
    inter_1_2_3 = interseccion_multiple(L1, L2, L3)
    print("L1 ∩ L2 ∩ L3 =", inter_1_2_3)

    # 6. Lenguajes A y B con cadenas binarias
    A_bin = {"01", "10", "11"}
    B_bin = {"10", "00", "1"}
    inter_bin = interseccion_lenguajes(A_bin, B_bin)
    print("A ∩ B (binarios) =", inter_bin)

    # 7. Lenguajes A y B con cadenas de letras
    A_abc = {"x", "y", "z"}
    B_abc = {"m", "n", "z"}
    inter_abc = interseccion_lenguajes(A_abc, B_abc)
    print("A ∩ B (letras) =", inter_abc)

    # 8. Comprobar si "a" pertenece a L1 ∩ L2
    pertenece_a = "a" in inter_1_2
    print('¿La palabra "a" pertenece a L1 ∩ L2?', pertenece_a)

    # 9. Comprobar si "b" pertenece a L4 ∩ L5
    pertenece_b = "b" in inter_4_5
    print('¿La palabra "b" pertenece a L4 ∩ L5?', pertenece_b)

    # 10. Ejemplo adicional usando la función interseccion_lenguajes
    ejemplo1 = {"hello", "world", "python"}
    ejemplo2 = {"python", "java", "c++"}
    inter_ejemplo = interseccion_lenguajes(ejemplo1, ejemplo2)
    print("Ejemplo adicional: Intersección =", inter_ejemplo)

if __name__ == "__main__":
    main()
