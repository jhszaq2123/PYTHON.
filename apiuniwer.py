import requests
import threading

COUNTRIES = ["USA", "Canada"]  # Lista 20 krajów (dla przykładu tylko 2)

def fetch_universities(country):
    url = f"http://universities.hipolabs.com/search?country={country}"
    response = requests.get(url)
    data = response.json()
    
    print(f"{country}: {[uni['name'] for uni in data[:5]]}")  # Wyświetlamy pierwsze 5 uniwersytetów

# Tworzenie i uruchamianie wątków
threads = []
for country in COUNTRIES:
    thread = threading.Thread(target=fetch_universities, args=(country,))
    threads.append(thread)
    thread.start()

# Oczekiwanie na zakończenie wszystkich wątków
for thread in threads:
    thread.join()