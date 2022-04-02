from pickle import TRUE
import time
import threading


# variáveis
contador = 0
max_for = 10000000
paralelo = True # FALSE - desativado o modo paralelo (thread)

lock = threading.Lock()

# função principal da thread
def somar():
    # temos que colocar como global para q a função pegue o contador de fora
    global contador
    for i in range(0, max_for):
        lock.acquire() # nesse processo estamos aguardando que um thread ande com o processo
        # enquanto a outra espera, aguardando ser liberada pelo GIL
        contador += 1
        lock.release() # aqui o GIL faz a liberação da execução, e outra thread fica impossibilitada
        # de ser executada. Então as duas funcionam em paralelo.
        
        
start_time = time.time()

if paralelo:
    t1 = threading.Thread(target=somar)
    t2 = threading.Thread(target=somar)
    
    # executa o script
    t1.start()
    t2.start()
    
    # bloqueia a execução do script
    t2.join()
    t2.join()
else: 
    somar()
    somar()
    
# calculo do tempo de execução    
end_time = time.time() - start_time
print("TEMPO DE EXECUÇÃO SERIAL: ", end_time)
print("CONTADOR: ", contador)

# TEMPO DE EXECUÇÃO SERIAL:  1.5638959407806396

"""PRIMEIRO, SEGUNDO E TERCEIRO TEMPO DE EXECUÇÃO PARALELO:
TEMPO DE EXECUÇÃO PARALELO:  1.5850887298583984
TEMPO DE EXECUÇÃO PARALELO:  1.69040846824646
TEMPO DE EXECUÇÃO PARALELO:  1.8356800079345703
"""

# checagem - verificar se o contador é igual ao max_for * 2 com o paralelo ativado
"""não retorna mensagem de erro, pois a asserção é verdadeira"""
assert contador == max_for * 2

"""Essa asserção é falsa se ativarmos o modo paralelo (com thread) não retorn aum resultado bom

TEMPO DE EXECUÇÃO SERIAL:  1.8621747493743896
"""

# Quando vemos o contador: CONTADOR:  13750960

# Quando usamos paralelimos e usando lock para aguardar a outra thread ser feita:

"""TEMPO DE EXECUÇÃO SERIAL:  10.649341821670532
CONTADOR:  20000000"""
