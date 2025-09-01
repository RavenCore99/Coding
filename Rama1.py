
# Rama 1: Ejercicio de Union de Lenguajes
#Grupo A // Lenguas y Atomatas // 2025
# Ejercicio hecho en conjunto

def union_lenguajes(lang1, lang2):
   # "Función para calcular la unión de dos lenguaje
    return lang1.union(lang2)

# Definición de los lenguajes dados
L1 = {"a", "b", "ab", "ba"}
L2 = {"b", "c", "bc", "cb"}
L3 = {"a", "b", "c"}
L4 = {"ab", "ac"}
L5 = {"b", "bc", "ca", "c"}

# Cálculo de uniones
union_L1_L2 = union_lenguajes(L1, L2)
union_L1_L3 = union_lenguajes(L1, L3)
union_L2_L3 = union_lenguajes(L2, L3)
union_L4_L5 = union_lenguajes(L4, L5)
union_L1_L2_L3 = union_lenguajes(union_L1_L2, L3)

# Lenguajes finitos A y B
A = {"cad", "aca", "ad"}
B = {"a", "d", "c"}
union_A_B = union_lenguajes(A, B)

# Lenguajes finitos A, B y C
A2 = {"10", "01", "11"}
B2 = {"0", "1"}
C = {"00", "10"}
union_A_B_C = union_lenguajes(union_lenguajes(A2, B2), C)

# Lenguaje finito D
D = {"x", "y", "z"}

# Comprobaciones
pertenece_abc = "abc" in union_L1_L2
pertenece_a = "a" in union_L4_L5

# Resultados
print("Unión L1 ∪ L2:", union_L1_L2)
print("Unión L1 ∪ L3:", union_L1_L3)
print("Unión L2 ∪ L3:", union_L2_L3)
print("Unión L4 ∪ L5:", union_L4_L5)
print("Unión L1 ∪ L2 ∪ L3:", union_L1_L2_L3)
print("Unión A ∪ B:", union_A_B)
print("Unión A ∪ B ∪ C:", union_A_B_C)
print(f"La palabra 'abc' pertenece a L1 ∪ L2: {pertenece_abc}")
print(f"La palabra 'a' pertenece a L4 ∪ L5: {pertenece_a}")

# Ejemplo de prueba adicional //proporcionados por el usuario
def entrada_usuario():
    lang_input1 = input("Ingresa el primer lenguaje (separado por comas): ")
    lang_input2 = input("Ingresa el segundo lenguaje (separado por comas): ")
    
    lang1 = set(lang_input1.split(","))
    lang2 = set(lang_input2.split(","))
    
    resultado_union = union_lenguajes(lang1, lang2)
    print("Unión del lenguaje ingresado:", resultado_union)
    
    # Indicar a qué unión pertenecen
    if lang1 == L1 and lang2 == L2:
        print("Esta unión corresponde a L1 ∪ L2.")
    elif lang1 == L1 and lang2 == L3:
        print("Esta unión corresponde a L1 ∪ L3.")
    elif lang1 == L2 and lang2 == L3:
        print("Esta unión corresponde a L2 ∪ L3.")
    elif lang1 == L4 and lang2 == L5:
        print("Esta unión corresponde a L4 ∪ L5.")
    elif lang1 == A and lang2 == B:
        print("Esta unión corresponde a A ∪ B.")
    elif lang1 == A2 and lang2 == B2:
        print("Esta unión corresponde a A2 ∪ B2.")
    elif lang1 == B2 and lang2 == C:
        print("Esta unión corresponde a B2 ∪ C.")
    else:
        print("Esta unión no corresponde a las uniones predefinidas.")

def entrada_usuario_multiple():
    lenguajes = []
    for i in range(3):
        lang_input = input(f"Ingresa el lenguaje {i+1} (separado por comas): ")
        lang = set(lang_input.split(","))
        lenguajes.append(lang)
    
    # Calcular la unión de todos los lenguajes ingresados
    resultado_union = lenguajes[0]
    for lang in lenguajes[1:]:
        resultado_union = union_lenguajes(resultado_union, lang)
    
    print("Unión de los lenguajes ingresados:", resultado_union)

# Llamar a la función de entrada del usuario
entrada_usuario()
entrada_usuario_multiple()
