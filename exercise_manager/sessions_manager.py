from .session import Session

class SessionManager:
    def __init__(self) -> None:
        self._sessions = [Session("Default Session")]

    def add_session(self, session: Session):
        self._sessions.append(session)
    
    def remove_session(self, session_index: int):
        try:
            return self._sessions.pop(session_index)
        except:
            print("Removal Error!")
            return False
    
    def __str__(self, extend=False) -> str:
        output = ""
        for i, session in enumerate(self._sessions, start=1):
            output += f"{i}. {session}\n"
        return output