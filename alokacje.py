class Processor:
    def __init__(self, id):
        self.id = id
        self.load = 0
        self.tasks = []

def main():
    tasks = [15, 10, 20, 30, 5, 25, 10, 35]
    processor_count = 3
    processors = [Processor(i) for i in range(processor_count)]

    # Sortowanie zadań malejąco i przypisanie ich do procesorów
    for task in sorted(tasks, reverse=True):
        # Znalezienie procesora z najmniejszym obciążeniem
        least_loaded_processor = min(processors, key=lambda p: p.load)
        least_loaded_processor.tasks.append(task)
        least_loaded_processor.load += task

    # Wyświetlenie wyników
    for processor in processors:
        print(f"Procesor {processor.id}: Obciążenie = {processor.load}, Zadania = {', '.join(map(str, processor.tasks))}")

if __name__ == "__main__":
    main()
