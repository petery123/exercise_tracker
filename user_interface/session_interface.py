from exercise_manager import Exercise
from .workout_interface import WorkoutInterface

class SessionInterface:
    def __init__(self, sessions):
        self._sessions = sessions

    def start(self):
        print("--WELCOME TO THE WORKOUT SESSION VIEWER AND EDITOR--")

        while(True):
            print("**SESSION VIEWER & EDITOR**")
            print("Here are your Sessions")
            print(self._sessions)
            print("x: to exit")

            session_index = input("Which Session will you like to view / edit: ")
            print(" ")

            if (session_index == "x"):
                break

            session_index = int(session_index) - 1
            session = self._sessions.get_session(session_index)

            if (session): #checking if a session has been properly accessed       
                print(session.__str__(True))
                while (True):
                    print(f"*CURRENT SESSION*: {session}")
                    print("\nEditing Commands")
                    print("1) Change Session Name")
                    print("2) Add Exercise")
                    print("3) Delete Exercise")
                    print("4) View / edit to specific Exercise")
                    print("x) Close\n")

                    entry = input("Enter Command: ")

                    if (entry == "x"):
                        break

                    elif(entry == "1"):
                        new_name = input("Enter New Name for Session: ")
                        session.set_name(new_name)
                        print("Name has been set")
                    
                    elif(entry == "2"):
                        print(session.__str__(True))
                        exercise_name = input("Enter name of exercise: ")
                        session.add_exercise(Exercise(exercise_name))
                        print("Exercise has been added")
                    
                    elif(entry == "3"):
                        if (not session.has_exercises()):
                            print("No exercises to delete")
                        else:
                            print(session.__str__(True))
                            exercise_index = int(input("Enter the number you want to delete: ")) - 1
                            removed_exercise = session.remove_exercise(exercise_index)
                            if (removed_exercise):
                                print(f"{removed_exercise} has been removed from this session.\n")
                    
                    elif(entry == "4"):
                        WorkoutInterface().start()