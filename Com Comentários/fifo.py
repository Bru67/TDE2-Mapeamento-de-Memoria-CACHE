class FIFO: 
    def __init__(self): #iniciando classe
        self.nome = "FIFO"

    # Código para o algorítmo FIFO (First In, First Out):
    def alg_fifo(paginas, quadros):
        falta_paginas = 0 
        controle_entrada = [] #armazena a ordem de entrada (histórico)
        memoria = [] #armazena a sequência final
        for p in paginas:
            if p not in memoria:
                if len(memoria) < quadros: # se o número de itens na lista "memoria" for menor q o número de quadros, ele adiciona
                    memoria.append(p)
                    controle_entrada.append(p)
                    falta_paginas += 1
                else:
                    mais_antigo = controle_entrada.pop(0) #remove o mais antigo (que esta na posição 0)
                    idx = memoria.index(mais_antigo)
                    memoria[idx] = p #substitui a pagina no quadro em que estava a pagina mais antiga (primeira que foi adicionada na memoria)
                    controle_entrada.append(p)
                    falta_paginas += 1
            # print(memoria, faltas de pagina)
            resultado = f"Memória final FIFO: {memoria}\nTotal Falta de Páginas: {falta_paginas}\n"
        return resultado
