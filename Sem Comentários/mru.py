class MRU:
    def __init__(self): 
        self.nome = "MRU"

    def alg_mru(paginas, quadros):
        falta_paginas = 0 
        memoria = [] 
        uso = []  
        for p in paginas:
            if p in memoria:
                uso.remove(p)
                uso.append(p) 
            elif len(memoria) < quadros: 
                memoria.append(p)
                uso.append(p)
                falta_paginas += 1
            else:
                ultimo_usado = uso.pop(-1)  
                idx = memoria.index(ultimo_usado)
                memoria[idx] = p 
                uso.append(p)
                falta_paginas += 1
            resultado = f"Memória final MRU: {memoria}\nTotal Falta de Páginas: {falta_paginas}\n"
        return resultado