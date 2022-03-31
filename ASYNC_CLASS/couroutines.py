from collections import deque

""" CORROTINAS - forma de escrever aplicações assincronas.
ENTENDENDO AS CORROTINAS
----------------------------------------------------------
CONTROLE DE FLUXOS E GERADORES MELHORADOS
"""

"""
def coro():
    print("Started")
    
    while True:
        value = yield
        yield value + 10


c = coro()

print("------", next(c)) # printed value = None

print("------", c.send(10)) # printed value = 20

print("=-"*20)

def coro2():
    print("Started")
    
    while True:
        values = yield
        yield values

c_value = coro2()

print("------", coro2) # <function coro2 at 0x7f85130880d0>
print("------", next(c_value)) # None

print(c_value.send([1,2,3,4,5]))
print(next(c_value))
"""

# controlador de fluxo

def count(stop):
    cont = 1
    
    while cont <= stop
        yield cont
        cont +=1
        
def regressive_count(start):
    while start >= 1:
        yield start
        start -= 1

class Scheduler:
    def __init__(self):
        self.queue = deque()


    def add_new(self, coro):
        self.queue.append(coro)
        
    def run(self):
        while self.queue:
            task = self.queue.popleft()
            
            try:
                result = next(task)
                print(f"{task=}: {result=}")
                self.queue.append(task)
                
            except StopIteration:
                pass
            
            
s = Scheduler()
s.add_new(count(10))
s.add_new(regressive_count(15))
# ------------------

