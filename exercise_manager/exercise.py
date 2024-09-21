class Exercise:
    def __init__(self, name):
        self.name = name
        self.weights = []
    
    def change_name(self, new_name):
        self.name = new_name
    
    def add_weight(self, weight):
        self.weights.append(weight)

    def __str__(self):
        if len(self.weights) == 0:
            return f"{self.name} : No Weights"
        return f"{self.name}: {self.weights[-1]}"
    
    def progress(self):
        weight_str = f"{self.name} progress: "
        if (len(self.weights) == 0): #checks if there are any weights added
            return f"{self.name} : No Added Weights!"
        
        for i in range(len(self.weights)): #loops through the weights and formats them in a printable way
            if (i != len(self.weights)-1):
                weight_str += f"{self.weights[i]}, "
            else:
                weight_str += f"{self.weights[i]}"
        
        return weight_str