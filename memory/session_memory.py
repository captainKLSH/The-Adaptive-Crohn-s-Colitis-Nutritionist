from typing import List, Dict
from pydantic import BaseModel

class UserProfile(BaseModel):
    user_id: str = "default_patient"
    known_triggers: List[str] = ["popcorn", "spicy"]
    safe_foods: List[str] = ["chicken", "rice", "bananas"]
    current_state: str = "UNKNOWN" # Updates based on session

class SessionMemory:
    def __init__(self):
        self.history: List[Dict] = []
        self.user_profile = UserProfile()
        self.current_plan = None

    def add_turn(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def update_state(self, state: str):
        self.user_profile.current_state = state

    def get_profile_summary(self) -> str:
        return f"Triggers: {self.user_profile.known_triggers}, State: {self.user_profile.current_state}"
