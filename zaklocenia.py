class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.zeros(input_size)
        self.bias = 0
        self.learning_rate = learning_rate
        
    def activation(self, x):
        """Funkcja aktywacji (Step function)"""
        return 1 if x >= 0 else 0
    
    def predict(self, inputs):
        """Dokonuje predykcji na podstawie wejścia"""
        summation = np.dot(inputs, self.weights) + self.bias
        return self.activation(summation)
    
    def train(self, inputs, labels, epochs=10):
        """Trenuj perceptron na podstawie danych wejściowych"""
        for epoch in range(epochs):
            for x, label in zip(inputs, labels):
                prediction = self.predict(x)
                error = label - prediction
                # Aktualizacja wag
                self.weights += self.learning_rate * error * x
                self.bias += self.learning_rate * error
