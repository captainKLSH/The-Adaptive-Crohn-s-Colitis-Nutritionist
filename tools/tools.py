import time
from typing import List, Dict
from project.core.a2a_protocol import Recipe

class MockSpoonacularClient:
    """
    Mocks a recipe API. In a real app, this would request spoonacular.com
    """
    def search_recipes(self, query: str, max_fiber: float, exclude: List[str]) -> List[Recipe]:
        # Simulating API return based on query for demonstration
        if "soup" in query.lower():
            return [
                Recipe(
                    name="Grandma's Chicken Rice Soup",
                    ingredients=["chicken breast", "white rice", "carrots", "celery", "onion"],
                    instructions="Boil everything until cooked.",
                    fiber_content=1.5
                )
            ]
        elif "salad" in query.lower():
            return [
                Recipe(
                    name="Fresh Garden Salad",
                    ingredients=["lettuce", "raw tomatoes", "cucumbers", "croutons"],
                    instructions="Toss ingredients.",
                    fiber_content=5.0
                )
            ]
        else:
             return [
                Recipe(
                    name="Safe Plain Potato",
                    ingredients=["potato", "salt"],
                    instructions="Boil and mash.",
                    fiber_content=2.0
                )
            ]

class MockLLM:
    """
    Mocks an LLM to make this notebook runnable without an OpenAI key.
    It uses simple keyword heuristics to simulate intelligence.
    """
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        # PLANNER LOGIC MOCK
        if "Clinical Triage" in system_prompt:
            if "pain" in user_prompt.lower() or "hurt" in user_prompt.lower():
                return '{"state": "FLARE", "constraints": {"max_fiber": 2.0, "exclude": ["skins", "seeds", "nuts", "raw"], "texture": "soft"}}'
            else:
                return '{"state": "REMISSION", "constraints": {"max_fiber": 10.0, "exclude": ["popcorn"], "texture": "normal"}}'
        
        # WORKER LOGIC MOCK handled by python code mostly, but if LLM needed:
        if "Chef" in system_prompt:
             return "Searching for safe recipes..."

        # EVALUATOR LOGIC MOCK
        if "Safety Auditor" in system_prompt:
            # Simple check for demo purposes
            if "raw" in user_prompt.lower() or "celery" in user_prompt.lower(): # Celery is fibrous
                 return '{"approved": false, "warnings": ["Celery is stringy and hard to digest during flare"], "modification": "Boil celery until mushy or use celery seed."}'
            return '{"approved": true, "warnings": [], "modification": null}'
        
        return "I am just a simple mock LLM."

# Instantiate global toolsets
llm_client = MockLLM()
recipe_client = MockSpoonacularClient()
