from project.core.context_engineering import WORKER_SYSTEM_PROMPT
from project.core.observability import Logger
from project.core.a2a_protocol import DietConstraints, Recipe
from project.tools.tools import recipe_client

class Worker:
    def execute_plan(self, constraints: DietConstraints) -> Recipe:
        Logger.log_agent_action("Worker", "Executing Search", f"Looking for recipes with max fiber: {constraints.max_fiber_per_serving}")
        
        # Decide query based on state (Mock logic)
        query = "soup" if constraints.disease_state == "FLARE" else "balanced meal"
        
        results = recipe_client.search_recipes(
            query=query, 
            max_fiber=constraints.max_fiber_per_serving,
            exclude=constraints.excluded_textures
        )
        
        candidate = results[0] # Pick top result
        Logger.log_agent_action("Worker", "Candidate Found", f"{candidate.name}: {candidate.ingredients}")
        return candidate
