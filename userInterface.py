from exercise_manager import SessionManager
from exercise_manager import Session

class UserInterface:
    def __init__(self):
        self._sessions = SessionManager()
    
    def start(self):
        print("--WELCOME TO YOUR WORKOUT TRACKER--")

        while (True):
            print("\nProgram Commands")
            print("1) View Workout Sessions")
            print("2) Create new Session")
            print("3) Delete Session")
            print("3) To view breakdown of specific Workout Session")
            print("x) Close")

            entry = input("Enter a command: ")
            print("********************************")

            if(entry == "x"):
                break

            elif(entry == "1"):
                print(self._sessions)

            elif(entry == "2"):
                session_name = input("Enter Session name: ")
                self._sessions.add_session(Session(session_name))
            
            elif(entry == "3"):
                print("Session List:")
                print(self._sessions)       
                session_index = int(input("Enter the number you want to delete: ")) - 1
                removed_session = self._sessions.remove_session(session_index)
                if (removed_session):
                    print(f"{removed_session} has been removed.")
            