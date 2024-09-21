from .exercise import Exercise

class Session:
    def __init__(self, name):
        self._name = name
        self._exercises = []
    
    def change_name(self, new_name: str):
        self._name = new_name
    
    def add_exercise(self, exercise: Exercise):
        self._exercises.append(exercise)
    
    def remove_exercise(self, exercise_index: int):
        return self._exercises.pop(exercise_index)
    
    def __str__(self) -> str:
        workout_str = f"WORKOUT SESSION: {self._name}\n"
        for i in range(len(self._exercises)):
            workout_str += f"{i+1}. {(self._exercises[i])}\n"
        return  workout_str