
class SessionInterface:
    def __init__(self, sessions):
        self._sessions = sessions
        
    def start(self):
        print("--WELCOME TO THE WORKOUT SESSION VIEWER AND EDITOR--")

        while(True):
            print("Here are your Sessions")
            print(self._sessions)
            print("x: to exit")

            session_index = input("Which Session will you like to view / edit: ")

            if (session_index == "x"):
                break
            session_index = int(session_index) - 1
            session = self._sessions.get_session(session_index)

            if (session): #checking if a session has been properly accessed       
                print(session.__str__(True))
                while (True):
                    print("\nEditing Commands")
                    print("1) Change Session Name")
                    print("1) Add Workout")
                    print("2) Delete Workout")
                    print("3) View / edit to specific Workout")
                    print("x) Close")