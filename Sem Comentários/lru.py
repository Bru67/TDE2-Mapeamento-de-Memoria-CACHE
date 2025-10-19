class LRU:
    def __init__(self): 
        self.nome = "LRU"

    def alg_lru(paginas, quadros):
        falta_paginas = 0 
        uso_recente = [] 
        memoria = [] 
        for p in paginas:
            if p in memoria:
                uso_recente.remove(p)
                uso_recente.append(p)
            else:
                if len(memoria) < quadros:
                    memoria.append(p)
                    uso_recente.append(p)
                    falta_paginas += 1
                else:
                    ultimo_usado = uso_recente.pop(0)
                    idx = memoria.index(ultimo_usado)
                    memoria[idx] = p 
                    uso_recente.append(p)
                    falta_paginas += 1
            resultado = f"Memória final LRU: {memoria}\nTotal Falta de Páginas: {falta_paginas}\n"
        return resultado
