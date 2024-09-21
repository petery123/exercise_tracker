from exercise_manager import Exercise
from .exercise_interface import ExerciseInterface

class SessionInterface:
    def __init__(self, session):
        self._session = session

    def start(self):
        print(f"{self._session.__str__(True)}\n")
        while (True):
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("**SESSION VIEWER & EDITOR**")
            print(f"*CURRENT SESSION*: {self._session}")
            print("\nEditing Commands")
            print("1) Change Session Name")
            print("2) Add Exercise")
            print("3) Delete Exercise")
            print("4) View / edit specific Exercise")
            print("x) Close\n")

            entry = input("Enter Command: ")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

            if (entry == "x"): #stop session editor
                break

            elif(entry == "1"): #change exercise name
                new_name = input("Enter New Name for Session: ")
                self._session.set_name(new_name)
                print("Name has been set")
            
            elif(entry == "2"): #add exercise
                print(f"{self._session.__str__(True)}\n")
                exercise_name = input("Enter name of exercise: ")
                self._session.add_exercise(Exercise(exercise_name))
                print("Exercise has been added")
            
            elif(entry == "3"): #delete exercise
                if (not self._session.has_exercises()):
                    print("No exercises to delete")
                else:
                    print(f"{self._session.__str__(True)}\n")
                    exercise_index = int(input("Enter the number you want to delete: ")) - 1
                    removed_exercise = self._session.remove_exercise(exercise_index)
                    if (removed_exercise):
                        print(f"{removed_exercise} has been removed from this self._session.\n")
                    else:
                        print("Removal Error!\nNot in range, going back!")
            
            elif(entry == "4"): #view / edit sepcific exercise
                print("Here are your Exercises")
                print(f"{self._session.__str__(True)}\n")

                exercise_index = input("Which Exercise will you like to view / edit: ")
                print(" ")

                exercise_index = int(exercise_index) - 1
                exercise = self._session.get_exercise(exercise_index)

                if (exercise): #checking if a session has been properly accessed   
                    ExerciseInterface(exercise).start() #start up exercise interface
                else:
                    print("Access Error!\nNot in range, going back!")
            
            else:
                print("Command not valid!\n")