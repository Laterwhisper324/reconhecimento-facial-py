insta = input()
cons = float(input())

if insta == "R" and cons <= 500:
    print(f"Valor a pagar: R$ {cons * 0.40:.2f}")
elif insta == "C" and cons <= 1000:
    print(f"Valor a pagar: R$ {cons * 0.55:.2f}")
elif insta == "R" and cons > 500:
    print(f"Valor a pagar: R$ {cons * 0.65:.2f}")
elif insta == "C" and cons > 1000:
    print(f"Valor a pagar: R$ {cons * 0.60:.2f}")