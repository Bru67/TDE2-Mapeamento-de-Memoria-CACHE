page_faults = 0

def alg_fifo(paginas, quadros):
    page_faults = 0 
    memoria = []
    for p in paginas:
        if p not in memoria:
            if len(memoria) < quadros:
                memoria.append(p)
                page_faults += 1
            else:
                memoria.pop(0) 
                memoria.append(p)
                page_faults += 1
        string = f"Memória final FIFO: {memoria}\nTotal Page Faults: {page_faults}\n"
    return string


def alg_lru(paginas, quadros):
    page_faults = 0 
    memoria = []
    for p in paginas:
        if p in memoria:
            memoria.append(p)
        else:
            if len(memoria) >= quadros:
                memoria.pop(0)
            memoria.append(p)
            page_faults += 1
        string = f"Memória final LRU: {memoria}\nTotal Page Faults: {page_faults}\n"
    return string


def alg_mru(paginas, quadros):
    page_faults = 0 
    memoria = []
    for p in paginas:
        if p in memoria:
            memoria.remove(p)
            memoria.append(p)
        elif len(memoria) < quadros:
            memoria.append(p)
            page_faults += 1
        else:
            memoria.pop(-1)  
            memoria.append(p)
            page_faults += 1
        string = f"Memória final MRU: {memoria}\nTotal Page Faults: {page_faults}\n"
    return string


def testar_sequencia(sequencia, quadros, nome):
    fifo = alg_fifo(sequencia, quadros)
    lru = alg_lru(sequencia, quadros)
    mru = alg_mru(sequencia, quadros)

    print(f"\n=-=-=-=-= Resultados sequencia {nome} =-=-=-=-=")
    print(fifo)
    print(lru)
    print(mru)

quadros = 8

seq_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
seq_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
seq_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]

testar_sequencia(seq_a, quadros, "A")
testar_sequencia(seq_b, quadros, "B")
testar_sequencia(seq_c, quadros, "C")