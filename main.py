from tkinter import Tk
# Serie
# Ds = D1 * D2 * ... * Dn

# Parallel
# Dp = 1 - (1 - Ds) ^ n
i = -1
a = 1
list_serie = []
list_parallel = []
while i != 0:
    i = int(input("0 - Sair\n1 - Adicionar\n2 - Calcular\n->"))
    if i == 1:
        op = int(input("1 - Série\n2 - Paralelo\n->"))
        
        if op == 1:
            list_serie.append(float(input("Disponibilidade X = ")))
            a += 1
        elif op == 2:
            list_parallel.append(float(input("Disponibilidade X = ")))
            a += 1
        else:
            print("Erro. Opção Inválida.")
    if i == 2 and (len(list_serie) > 0 or len(list_parallel) > 0):
        if len(list_serie) > 0:
            size = 0
            Ds = list_serie[0]
            while size < len(list_serie):
                Ds = Ds * list_serie[size]
                size += 1
            print(f"Ds = {Ds}")
        else:
            size = 0
            Ds = list_parallel[0]
            while size < len(list_parallel):
                Ds = Ds * list_parallel[size]
                size += 1 
    else:
        print("Erro. Nenhuma disponibilidade foi adicionada.")
