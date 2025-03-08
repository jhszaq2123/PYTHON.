# Funkcja rozwiązująca problem plecaka (Knapsack) metodą dynamicznego programowania
def knapsack(capacity, weights, values, n):
    # Tablica dp, która przechowuje maksymalną wartość dla danego przedmiotu i pojemności plecaka
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Wypełnianie tablicy dp
    for i in range(n + 1):
        for w in range(capacity + 1):
            # Jeśli nie ma przedmiotów lub pojemność plecaka jest zerowa, wartość to 0
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                # Maksymalna wartość, uwzględniając bieżący przedmiot
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],  # Z uwzględnieniem przedmiotu
                    dp[i - 1][w]  # Bez uwzględnienia przedmiotu
                )
            else:
                # Nie można wziąć przedmiotu, więc wartość pozostaje taka sama jak dla mniejszej pojemności
                dp[i][w] = dp[i - 1][w]

    # Zwrócenie maksymalnej wartości, którą można uzyskać
    return dp[n][capacity]

# Metoda główna programu
def main():
    # Przykładowe dane: wartości i wagi przedmiotów
    values = [60, 100, 120]
    weights = [2, 3, 5]
    capacity = 10  # Pojemność plecaka
    n = len(values)  # Liczba przedmiotów

    # Wywołanie funkcji knapsack, aby obliczyć maksymalny zysk
    max_profit = knapsack(capacity, weights, values, n)

    # Wyświetlenie wyniku
    print(f'Maksymalna wartość przedmiotów w plecaku: {max_profit}')

# Uruchomienie programu
if __name__ == "__main__":
    main()
