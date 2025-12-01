import json
from project.core.context_engineering import PLANNER_SYSTEM_PROMPT
from project.core.observability import Logger
from project.core.a2a_protocol import AgentMessage, DietConstraints
from project.tools.tools import llm_client

class Planner:
    def __init__(self, memory):
        self.memory = memory

    def assess_situation(self, user_input: str) -> DietConstraints:
        Logger.log_agent_action("Planner", "Analyzing User Input", user_input)
        
        # In a real app, we would pass memory history here
        response_str = llm_client.generate(PLANNER_SYSTEM_PROMPT, user_input)
        
        try:
            data = json.loads(response_str)
            state = data["state"]
            cons_data = data["constraints"]
            
            # Update Memory
            self.memory.update_state(state)
            
            constraints = DietConstraints(
                disease_state=state,
                max_fiber_per_serving=cons_data["max_fiber"],
                excluded_textures=cons_data["exclude"],
                allowed_cooking_methods=[cons_data["texture"]]
            )
            
            Logger.log_agent_action("Planner", "Plan Generated", f"State: {state} | Constraints: {constraints.dict()}")
            return constraints
            
        except Exception as e:
            Logger.log_error("Planner", f"Failed to parse LLM response: {e}")
            # Fallback safe mode
            return DietConstraints(
                disease_state="FLARE",
                max_fiber_per_serving=2.0,
                excluded_textures=["unknown"],
                allowed_cooking_methods=["boiled"]
            )
