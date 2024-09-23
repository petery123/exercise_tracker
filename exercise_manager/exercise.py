class Exercise:
    def __init__(self, name):
        self._name = name
        self._weights = []
    
    def set_name(self, new_name):
        self._name = new_name
    
    def get_name(self):
        return self._name
    
    def set_weights(self, weights):
        self._weights = weights
    
    def get_weights(self):
        return self._weights
    
    def add_weight(self, weight):
        self._weights.append(weight)

    def __str__(self):
        if len(self._weights) == 0:
            return f"{self._name} : No Weights"
        return f"{self._name}: {self._weights[-1]}"
    
    def progress(self):
        weight_str = f"{self._name} progress: "
        if (len(self._weights) == 0): #checks if there are any weights added
            return f"{self._name} : No Added Weights!"
        weight_str += ", ".join(map(str, self._weights))
        
        return weight_str