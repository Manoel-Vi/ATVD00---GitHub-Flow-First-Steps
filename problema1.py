print("Dadas duas variaveis, a e b, ambos com o valor inicial 1, encontre o resultado da expressão:")
print("[(a+b)**2 + 3a - b] / (a + b + 1)")
print("Entretanto você não pode usar o operador de potência, nem constantes matemáticas (pi ou e). Deve usar apenas operadores aritimetricos.")
a = 1
b = 1
potencia = a+b
numerador = ((a+b)*potencia) + (3*a) - b
denomminador = a + b + 1
valorFinal = numerador/denomminador
print(f'O valor final é {valorFinal}')