class Exercise:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weights = [weight]
    
    def change_name(self, new_name):
        self.name = new_name
    
    def add_weight(self, weight):
        self.weights.append(weight)

    def __str__(self):
        return f"{self.name} : {self.weights[-1]}"
    
    def progress(self):
        weight_str = ""
        for i in range(len(self.weights)):
            if (i != len(self.weights)-1):
                weight_str += f"{self.weights[i]}, "
            else:
                weight_str += f"{self.weights[i]}"
        
        return weight_str