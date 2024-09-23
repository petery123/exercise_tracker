import json
import os
from exercise_manager import SessionManager
from exercise_manager import Session
from exercise_manager import Exercise
from .session_interface import SessionInterface

class UserInterface:
    def __init__(self, filename="data.json"):
        self._sessions = SessionManager()
        self._filename = filename
        self.load_sessions() 
    
    def start(self):
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
                self.save_sessions()
                print("Session saved")
                break

            elif(entry == "1"): #to view all workout sessions
                print("Your sessions:")
                print(f"{self._sessions}\n")
                input()

            elif(entry == "2"): #to add a new session
                session_name = input("Enter Session name: ")
                self._sessions.add_session(Session(session_name))
                print(f"{session_name} has been added to your sessions!\n")
                input()
            
            elif(entry == "3"): #to delete a session
                print("Session List:")
                print(self._sessions)       
                session_index = int(input("Enter the number you want to delete: ")) - 1
                removed_session = self._sessions.remove_session(session_index)
                if (removed_session):
                    print(f"{removed_session} has been removed from your sessions.\n")
                else:
                    print("Removal Error!\nNot in range, going back!\n")
                input()
            
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
                    input()
            
            else:
                print("Command not valid!\n")
                input()

    def load_sessions(self):
        #Load sessions from JSON file
        if os.path.exists(self._filename):
            with open(self._filename, 'r') as f:
                session_data = json.load(f)
                for session in session_data:
                    new_session = Session(session['name'])
                    for exercise in session['exercises']:
                        new_exercise = Exercise(exercise['name'])
                        new_exercise.set_weights(exercise['weights'])  # Restore weights
                        new_session.add_exercise(new_exercise)
                    self._sessions.add_session(new_session)
        else:
            print(f"{self._filename} not found, starting with empty sessions.")

    def save_sessions(self):
        """Save sessions to a JSON file."""
        with open(self._filename, 'w') as f:
            session_data = [
                {
                    'name': session.get_name(),
                    'exercises': [
                        {
                            'name': exercise.get_name(),
                            'weights': exercise.get_weights()
                        } for exercise in session.get_exercises()
                    ]
                } for session in self._sessions.get_sessions()
            ]
            json.dump(session_data, f)

