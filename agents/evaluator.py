import json
from project.core.context_engineering import EVALUATOR_SYSTEM_PROMPT
from project.core.observability import Logger
from project.core.a2a_protocol import Recipe, AuditResult
from project.tools.tools import llm_client

class Evaluator:
    def audit_recipe(self, recipe: Recipe, state: str) -> AuditResult:
        Logger.log_agent_action("Evaluator", "Auditing Recipe", f"Checking '{recipe.name}' for {state} safety.")
        
        prompt = f"Recipe: {recipe.name}. Ingredients: {recipe.ingredients}. Instructions: {recipe.instructions}. Patient State: {state}"
        response_str = llm_client.generate(EVALUATOR_SYSTEM_PROMPT, prompt)
        
        try:
            data = json.loads(response_str)
            result = AuditResult(
                approved=data["approved"],
                safety_warnings=data["warnings"],
                modification_instructions=data.get("modification")
            )
            Logger.log_agent_action("Evaluator", "Audit Complete", f"Approved: {result.approved} | Notes: {result.modification_instructions}")
            return result
        except Exception as e:
            Logger.log_error("Evaluator", str(e))
            return AuditResult(approved=False, safety_warnings=["Audit Error"], modification_instructions="Consult a doctor.")
