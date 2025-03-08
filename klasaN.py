class PowerGenerator:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.current = 0  # Indeks potęgi
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        result = self.a ** self.current
        self.current += 1
        return result

# Przykładowe użycie
gen = PowerGenerator(2, 5)
for val in gen:
    print(val)  # Wypisze: 1, 2, 4, 8, 16