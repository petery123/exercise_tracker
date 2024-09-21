from exercise_manager import SessionManager
from exercise_manager import Session
from exercise_manager import Exercise
from .session_interface import SessionInterface

class UserInterface:
    def __init__(self):
        self._sessions = SessionManager()
    
    def start(self):
        self._sessions.add_session(self._create_demo_session())

        print("--WELCOME TO YOUR WORKOUT TRACKER--\n")

        while (True):
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("**WORKOUT TRACKER HOME**")
            print("Program Commands")
            print("1) View Workout Sessions")
            print("2) Add Session")
            print("3) Delete Session")
            print("4) To view / edit specific Workout Session")
            print("x) Close\n")

            entry = input("Enter a command: ")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

            if(entry == "x"): #stops code run
                break

            elif(entry == "1"): #to view all workout sessions
                print("Your sessions:")
                print(f"{self._sessions}\n")

            elif(entry == "2"): #to add a new session
                session_name = input("Enter Session name: ")
                self._sessions.add_session(Session(session_name))
                print(f"{session_name} has been added to your sessions!\n")
            
            elif(entry == "3"): #to delete a session
                print("Session List:")
                print(self._sessions)       
                session_index = int(input("Enter the number you want to delete: ")) - 1
                removed_session = self._sessions.remove_session(session_index)
                if (removed_session):
                    print(f"{removed_session} has been removed from your sessions.\n")
                else:
                    print("Removal Error!\nNot in range, going back!\n")
            
            elif(entry == "4"): #view and open workout session
                print("Here are your Sessions")
                print(self._sessions)

                session_index = input("Which Session will you like to view / edit: ")
                print(" ")

                session_index = int(session_index) - 1
                session = self._sessions.get_session(session_index)

                if (session): #checking if a session has been properly accessed   
                    SessionInterface(session).start() #start up session interface
                else:
                    print("Access Error!\nNot in range, going back!\n")
            
            else:
                print("Command not valid!\n")

    def _create_demo_session(self):
        demo_session = Session("Demo Session")
        demo_exercise = Exercise("Demo Exercise")
        demo_exercise.add_weight(40)
        demo_exercise.add_weight(50)
        demo_exercise.add_weight(80)
        demo_session.add_exercise(demo_exercise)
        return demo_session

