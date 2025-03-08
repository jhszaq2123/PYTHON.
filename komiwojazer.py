import random

# Stałe
SIZE = 100
MIN_DISTANCE = 10
MAX_DISTANCE = 100

# Losowa inicjalizacja macierzy odległości
distances = [[0] * SIZE for _ in range(SIZE)]

# Funkcja do generowania losowej macierzy odległości
def generate_random_matrix():
    for i in range(SIZE):
        for j in range(SIZE):
            if i == j:
                distances[i][j] = 0
            else:
                distances[i][j] = random.randint(MIN_DISTANCE, MAX_DISTANCE)

# Funkcja do tasowania tablicy
def shuffle(array):
    random.shuffle(array)

# Funkcja do mutacji (inwersja części trasy)
def invert_mutation(array):
    a = random.randint(0, SIZE - 1)
    b = random.randint(0, SIZE - 1)
    if a > b:
        a, b = b, a
    array[a:b+1] = reversed(array[a:b+1])

# Funkcja do obliczania długości trasy
def calculate_distance(path):
    total_distance = 0
    for i in range(SIZE - 1):
        total_distance += distances[path[i]][path[i + 1]]
    total_distance += distances[path[SIZE - 1]][path[0]]
    return total_distance

def main():
    # Generowanie losowej macierzy odległości
    generate_random_matrix()
    
    # Inicjalizacja trasy (od 0 do SIZE-1)
    parent = list(range(SIZE))
    shuffle(parent)

    # Obliczanie początkowej odległości
    best_distance = calculate_distance(parent)
    
    epochs = 0
    while epochs < 100000:
        # Tworzenie dziecka jako kopii rodzica
        child = parent[:]
        invert_mutation(child)

        # Obliczanie odległości dla dziecka
        child_distance = calculate_distance(child)
        
        # Jeśli dziecko jest lepsze, zamieniamy rodzica
        if child_distance < best_distance:
            parent = child
            best_distance = child_distance
        
        epochs += 1
    
    # Wyświetlanie najlepszego wyniku
    print(f'Najkrótsza znaleziona trasa: {best_distance}')

# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()
