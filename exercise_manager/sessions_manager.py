from .session import Session

class SessionManager:
    def __init__(self) -> None:
        self._sessions = []

    def add_session(self, session: Session):
        self._sessions.append(session)
    
    def remove_session(self, session_index: int):
        try:
            return self._sessions.pop(session_index)
        except:
            print("Removal Error!\n")
            return False
    
    def get_session(self, session_index):
        try:
            return self._sessions[session_index]
        except:
            print("Access Error!\n")
            return False
    
    def __str__(self) -> str:
        output = ""
        for i, session in enumerate(self._sessions, start=1):
            if (i == len(self._sessions)):
                output += f"{i}. {session}"
            else:
                output += f"{i}. {session}\n"
        return output