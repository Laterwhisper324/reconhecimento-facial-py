s1,s2 = map(str, input().split())

try:
    # Lê a primeira linha e a segunda linha separadamente
    s1 = input()
    s2 = input()

    num1 = int(s1)
    num2 = int(s2)

    print(num1 + num2)

except ValueError:
    print("Erro de Conversao: Entrada Invalida")
