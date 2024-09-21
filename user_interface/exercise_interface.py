from exercise_manager import Exercise

class ExerciseInterface:
    def __init__(self, exercise: Exercise) -> None:
        self._exercise = exercise

    def start(self) -> None:
        print(f"CURRENT EXERCISE> {self._exercise}\n")
        while (True):
            print("**EXERCISE VIEWER & EDITOR**")
            print(f"*CURRENT EXERCISE*: {self._exercise}")
            print("\nEditing Commands")
            print("1) Change Exercise Name")
            print("2) Add current weight level")
            print("3) Weight progress")
            print("x) Close\n")

            entry = input("Enter Command: ")

            if (entry == "x"): #stop exercise editor
                break

            elif(entry == "1"): #change exercise name
                new_name = input("Enter New Name for Exercise: ")
                self._exercise.set_name(new_name)
                print("Name has been set")
            
            elif(entry == "2"): #add new weight benchmark 
                print(f"{self._exercise}\n")
                new_weight = int(input("Enter new weight: "))
                self._exercise.add_weight(new_weight)
                print("New weight mark has been added")
            
            elif(entry == "3"):
                print(f"{self._exercise.progress()}\n")