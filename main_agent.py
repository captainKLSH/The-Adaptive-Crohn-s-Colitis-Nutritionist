from project.memory.session_memory import SessionMemory
from project.agents.planner import Planner
from project.agents.worker import Worker
from project.agents.evaluator import Evaluator
from project.core.observability import Logger

class MainAgent:
    def __init__(self):
        self.memory = SessionMemory()
        self.planner = Planner(self.memory)
        self.worker = Worker()
        self.evaluator = Evaluator()

    def handle_message(self, user_input: str) -> dict:
        self.memory.add_turn("user", user_input)
        
        # 1. Planner Phase
        constraints = self.planner.assess_situation(user_input)
        
        # 2. Worker Phase
        recipe_candidate = self.worker.execute_plan(constraints)
        
        # 3. Evaluator Phase
        audit_result = self.evaluator.audit_recipe(recipe_candidate, constraints.disease_state)
        
        # Construct Final Response
        if audit_result.approved:
            final_response = f"I found a recipe: {recipe_candidate.name}. It is safe for your current condition."
        else:
            final_response = (
                f"I found '{recipe_candidate.name}', but we need to modify it for safety.\n"
                f"**Issue:** {audit_result.safety_warnings}\n"
                f"**Fix:** {audit_result.modification_instructions}\n"
                f"Ingredients: {recipe_candidate.ingredients}"
            )
            
        self.memory.add_turn("assistant", final_response)
        
        return {
            "response": final_response,
            "state": constraints.disease_state,
            "recipe": recipe_candidate.dict()
        }

# Exposed function for the prompt requirement
def run_agent(user_input: str):
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result["response"]
