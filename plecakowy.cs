using System;

class Algorytmy
{
    // Funkcja rozwiązująca problem plecaka (Knapsack) metodą dynamicznego programowania
    static int Knapsack(int capacity, int[] weights, int[] values, int n)
    {
        // Tablica dp, która przechowuje maksymalną wartość dla danego przedmiotu i pojemności plecaka
        int[,] dp = new int[n + 1, capacity + 1];

        // Wypełnianie tablicy dp
        for (int i = 0; i <= n; i++)
        {
            for (int w = 0; w <= capacity; w++)
            {
                // Jeśli nie ma przedmiotów lub pojemność plecaka jest zerowa, wartość to 0
                if (i == 0 || w == 0)
                {
                    dp[i, w] = 0;
                }
                else if (weights[i - 1] <= w)
                {
                    // Maksymalna wartość, uwzględniając bieżący przedmiot
                    dp[i, w] = Math.Max(
                        values[i - 1] + dp[i - 1, w - weights[i - 1]], // Z uwzględnieniem przedmiotu
                        dp[i - 1, w] // Bez uwzględnienia przedmiotu
                    );
                }
                else
                {
                    // Nie można wziąć przedmiotu, więc wartość pozostaje taka sama jak dla mniejszej pojemności
                    dp[i, w] = dp[i - 1, w];
                }
            }
        }

        // Zwrócenie maksymalnej wartości, którą można uzyskać
        return dp[n, capacity];
    }

    // Metoda główna programu
    static void Main()
    {
        // Przykładowe dane: wartości i wagi przedmiotów
        int[] values = { 60, 100, 120 };
        int[] weights = { 2, 3, 5 };
        int capacity = 10; // Pojemność plecaka
        int n = values.Length; // Liczba przedmiotów

        // Wywołanie funkcji Knapsack, aby obliczyć maksymalny zysk
        int maxProfit = Knapsack(capacity, weights, values, n);

        // Wyświetlenie wyniku
        Console.WriteLine($"Maksymalna wartość przedmiotów w plecaku: {maxProfit}");
    }
}
