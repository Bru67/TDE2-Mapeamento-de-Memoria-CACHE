class FIFO: 
    def __init__(self): 
        self.nome = "FIFO"

    def alg_fifo(paginas, quadros):
        falta_paginas = 0 
        controle_entrada = [] 
        memoria = [] 
        for p in paginas:
            if p not in memoria:
                if len(memoria) < quadros: 
                    memoria.append(p)
                    controle_entrada.append(p)
                    falta_paginas += 1
                else:
                    mais_antigo = controle_entrada.pop(0) 
                    idx = memoria.index(mais_antigo)
                    memoria[idx] = p 
                    falta_paginas += 1
            resultado = f"Memória final FIFO: {memoria}\nTotal Falta de Páginas: {falta_paginas}\n"
        return resultado
