from fifo import FIFO
from lru import LRU
from mru import MRU

def testar_sequencia(sequencia, quadros, nome): 
    fifo = FIFO.alg_fifo(sequencia, quadros)
    lru = LRU.alg_lru(sequencia, quadros)
    mru = MRU.alg_mru(sequencia, quadros)

    print(f"\n=-=-=-=-= Resultados Sequência {nome} =-=-=-=-=")
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