'''
Esercizio 2

Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

with Timer():

    time.sleep(1)

time elapsed: 1.00000

in questo esempio il tempo passato non sarà mai uguale a 1'''

from datetime import datetime

class Timer:
    def __init__(self):
        self.start = 0
        self.end = 0
    
    def __enter__(self):
        self.start = datetime.now()
    
    def __exit__(self, a, b, c):
        self.end = datetime.now()
        time_elapsed = self.end - self.start
        print(f"ime elapsed: {time_elapsed}")

with Timer():

    for i in range(1, 99999999):
        pass