from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class AgentMessage(BaseModel):
    sender: str
    recipient: str
    message_type: str  # e.g., "PLAN", "DRAFT", "AUDIT_RESULT"
    content: Dict[str, Any]

class DietConstraints(BaseModel):
    disease_state: str = "UNKNOWN" # FLARE, REMISSION
    max_fiber_per_serving: float
    excluded_textures: List[str]
    allowed_cooking_methods: List[str]

class Recipe(BaseModel):
    name: str
    ingredients: List[str]
    instructions: str
    fiber_content: float

class AuditResult(BaseModel):
    approved: bool
    safety_warnings: List[str]
    modification_instructions: Optional[str] = None
