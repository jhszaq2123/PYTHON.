import numpy as np
import multiprocessing as mp
import math

def compute_function(x):
    return math.cos(x) + math.log(x + 1)

if '__name__' == "_main_":  # Poprawna konstrukcja
    x_values = np.arange(0, 1e6, 0.01)  # Duży zestaw wartości z krokiem 0.01
    pool = mp.Pool(mp.cpu_count())  # Tworzymy pulę procesów
    
    results = pool.map(compute_function, x_values)  # Równoległe przetwarzanie wartości
    
    pool.close()
    pool.join()
    
    print("Obliczenia zakończone.")