from .exercise import Exercise

class Session:
    def __init__(self, name):
        self._name = name
        self._exercises = []
    
    def set_name(self, new_name: str):
        self._name = new_name
    
    def get_name(self):
        return self._name
    
    def add_exercise(self, exercise: Exercise):
        self._exercises.append(exercise)
    
    def get_exercises(self):
        return self._exercises
    
    def remove_exercise(self, exercise_index: int):
        try:
            return self._exercises.pop(exercise_index)
        except:
            return False #returns false if can't access
    
    def __str__(self, extend=False) -> str:
        if(not extend):
           return self._name
        
        workout_str = f"WORKOUT SESSION: {self._name}\nEXERCISE LIST->"

        if(not self.has_exercises()):
            workout_str += "\nNo Workouts Added!"
        for i in range(len(self._exercises)):
            workout_str += f"\n{i+1}. {(self._exercises[i])}"
        return  workout_str
    
    def has_exercises(self) -> bool:
        return (len(self._exercises) > 0)
    
    def get_exercise(self, exercise_index):
        try:
            return self._exercises[exercise_index]
        except:
            return False #returns false if can't access