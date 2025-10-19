class MRU:
    def __init__(self): # Inciciando classe
        self.nome = "MRU"

    # Código do algorítmo MRU (Most Recently Used):
    def alg_mru(paginas, quadros):
        falta_paginas = 0 
        memoria = [] #armazena o a sequência final
        uso = []  #controla a ordem de uso
        for p in paginas:
            if p in memoria:
                #se o numero ja estiver na lista ele e removido e volta para a ultima posicao, mantem os recentes sempre pro fim
                uso.remove(p)
                uso.append(p)
            #se a quantidade de números em "memoria" for menor q o numero de quadros ele adiciona em ambas as listas 
            elif len(memoria) < quadros: 
                memoria.append(p)
                uso.append(p)
                falta_paginas += 1
            else:
                # remove o mais recentemente usado (último da lista "uso")
                ultimo_usado = uso.pop(-1)  # remove o mais recente
                idx = memoria.index(ultimo_usado)
                memoria[idx] = p #substitui na posição do mais usado
                uso.append(p)
                falta_paginas += 1
            # print(memoria)
            resultado = f"Memória final MRU: {memoria}\nTotal Falta de Páginas: {falta_paginas}\n"
        return resultado