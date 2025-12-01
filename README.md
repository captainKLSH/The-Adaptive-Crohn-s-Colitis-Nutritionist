# The Adaptive Crohn’s & Colitis Nutritionist 🥗🏥

Kaggle Agents for Good Track (Healthcare) > An intelligent multi-agent system that adapts meal plans in real-time based on a patient's active disease state (Flare vs. Remission).

## 📖 Problem Statement

For patients with Inflammatory Bowel Disease (IBD) like Crohn's or Colitis, "healthy eating" is a moving target.

- Remission: Patients need high-nutrient, diverse foods to heal.

- Flare-up: Those same "healthy" foods (fiber, raw veggies, skins) can cause severe pain or hospitalization.

Standard diet apps are static. They don't switch safety protocols when a user reports pain. This project solves that by building an AI agent that acts as a dynamic clinical dietitian, switching between "Healing Mode" and "Safety Mode" instantly.

## 🤖 Multi-Agent Architecture

This system uses a Planner-Worker-Evaluator workflow to ensure medical safety.

1. The Planner (The Triage Nurse) 📋

- Role: Analyzes user input for distress signals (pain, urgency, fatigue).

- Logic:

If pain is detected → Activates FLARE PROTOCOL (Low residue, max 2g fiber, no skins/seeds).

If user is stable → Activates REMISSION PROTOCOL (Balanced diet, reintroduction of nutrients).

- Output: Generates a strict set of DietConstraints.

2. The Worker (The Chef) 👨‍🍳

- Role: Finds recipes that match the Planner's constraints.

- Tools: Uses recipe search APIs (mocked in this demo) to filter by ingredients and fiber content.

- Output: Drafts a candidate meal plan.

3. The Evaluator (The Safety Officer) 🛡️

- Role: The most critical agent. It "audits" the Worker's suggested recipe.

- Logic: It looks for "hidden knives"—ingredients that APIs might miss, such as strawberry seeds or potato skins.

- Output: Either approves the recipe or issues a Safety Warning with modification instructions (__e.g., "Warning: This soup contains celery. You must boil it until mushy or strain it out."__).

## 🛠️ Tech Stack

- Python 3.10+

- Pydantic: For strict data validation between agents.

- Rich: For beautiful console logging and observability.

- Mock Tools: Simulates Recipe API and LLM calls (can be swapped for OpenAI/Spoonacular).

## 🚀 Quick Start

1. Clone the Repository
```
git clone [https://github.com/yourusername/adaptive-nutritionist.git](https://github.com/yourusername/adaptive-nutritionist.git)
cd adaptive-nutritionist
```

2. Install Dependencies
```
pip install -r project/requirements.txt
```

3. Run the Demo

We have included a demo script that simulates a user in a "Flare" state.
```
python project/run_demo.py
```

4. Interactive Mode

To chat with the agent yourself:
```
python project/app.py
```

📂 File Structure
```bash
project/
├── agents/             # The brain of the operation
│   ├── planner.py      # Triage logic
│   ├── worker.py       # Recipe fetching
│   └── evaluator.py    # Safety auditing
├── core/               # Shared utilities
│   ├── a2a_protocol.py # JSON message formats
│   └── observability.py# Logging system
├── memory/             # User profile storage
├── tools/              # Mock APIs (LLM & Recipes)
└── main_agent.py       # The conductor leading the agents
```

📊 Logic Flow
```bash
graph TD
    User[User Input: 'My stomach hurts'] --> Planner
    Planner -->|Detects Flare| Constraints[Constraint: Low Fiber/Soft]
    Constraints --> Worker
    Worker -->|Search: 'Chicken Soup'| Recipe[Candidate Recipe]
    Recipe --> Evaluator
    Evaluator -->|Audit: 'Contains Celery'| Warning[Modify: Boil Celery]
    Warning --> Final[Response to User]
```

🛡️ Safety & Disclaimer

**This is an AI prototype and not a replacement for**
