# Rama 3: Ejercicio de concatenacion de Lenguajes
#Grupo A // Lenguas y Atomatas // 2025
# elaborada por Nicolas Ballesteros y a base de retroalimentacion de anteriores ejercicios



def concatenacion_lenguajes(L1, L2):
    
  # Calcula la concatenación de dos lenguajes L1 y L2.
    
    # por concatenar una cadena de L1 con una cadena de L2.
    
    resultado = set()
    for s1 in L1:
        for s2 in L2:
            resultado.add(s1 + s2)
    return resultado

def main():
    # Definición de los lenguajes dados
    L1 = {"a", "b", "ab", "ba"}
    L2 = {"b", "c", "bc", "cb"}
    L3 = {"a", "b", "c"}
    L4 = {"ab", "ac"}
    L5 = {"b", "bc", "ca", "c"}

    # 1. L1 · L3
    concat_1_3 = concatenacion_lenguajes(L1, L3)
    print("L1 · L3 =", concat_1_3)

    # 2. L3 · L1
    concat_3_1 = concatenacion_lenguajes(L3, L1)
    print("L3 · L1 =", concat_3_1)

    # 3. L4 · L5
    concat_4_5 = concatenacion_lenguajes(L4, L5)
    print("L4 · L5 =", concat_4_5)

    # 4. L5 · L4
    concat_5_4 = concatenacion_lenguajes(L5, L4)
    print("L5 · L4 =", concat_5_4)

    # 5. L1 · L2
    concat_1_2 = concatenacion_lenguajes(L1, L2)
    print("L1 · L2 =", concat_1_2)

    # 6. Lenguajes A y B con cadenas "a","b" y "a","c"
    A = {"a", "b"}
    B = {"a", "c"}
    concat_A_B = concatenacion_lenguajes(A, B)
    print("A · B =", concat_A_B)

    # 7. Lenguajes A y B con cadenas "0","1" y epsilon (cadena vacía), "00"
    A_bin = {"0", "1"}
    B_bin = {"", "00"}  # epsilon es cadena vacía ""
    concat_bin = concatenacion_lenguajes(A_bin, B_bin)
    print("A · B (binarios con epsilon) =", concat_bin)

    # 8. Comprobar si "aba" pertenece a L1 · L2
    pertenece_aba = "aba" in concat_1_2
    print('¿La palabra "aba" pertenece a L1 · L2?', pertenece_aba)

    # 9. Comprobar si "cab" pertenece a L3 · L4
    concat_3_4 = concatenacion_lenguajes(L3, L4)
    pertenece_cab = "cab" in concat_3_4
    print('¿La palabra "cab" pertenece a L3 · L4?', pertenece_cab)

    # 10. Ejemplo adicional usando la función concatenacion_lenguajes
    ejemplo1 = {"x", "yz"}
    ejemplo2 = {"a", "b"}
    concat_ejemplo = concatenacion_lenguajes(ejemplo1, ejemplo2)
    print("Ejemplo adicional: concatenación =", concat_ejemplo)

if __name__ == "__main__":
    main()
