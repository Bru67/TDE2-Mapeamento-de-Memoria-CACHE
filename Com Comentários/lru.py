class LRU:
    def __init__(self): #iniciando classe
        self.nome = "LRU"

    # Código para algorítimo LRU (Least Recently Used):
    def alg_lru(paginas, quadros):
        falta_paginas = 0 
        uso_recente = [] #armazena o uso das páginas
        memoria = [] #armazena a sequência final
        for p in paginas:
            if p in memoria:
                # se o numero ja estiver na lista ele é removido e volta para a ultima posicao na lista de usos recentes
                uso_recente.remove(p)
                uso_recente.append(p)
            else:
                if len(memoria) < quadros:
                    memoria.append(p)
                    uso_recente.append(p)
                    falta_paginas += 1
                else:
                    #remove o menos recentemente usado (primeiro da lista "recente")
                    ultimo_usado = uso_recente.pop(0)
                    idx = memoria.index(ultimo_usado)
                    memoria[idx] = p #substitui na posição do menos usado
                    uso_recente.append(p)
                    falta_paginas += 1
            # print(memoria, falta de paginas)
            resultado = f"Memória final LRU: {memoria}\nTotal Falta de Páginas: {falta_paginas}\n"
        return resultado
