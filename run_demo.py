import sys, os
# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from project.main_agent import run_agent

if __name__ == "__main__":
    print("--- DEMO START ---")
    # Simulating a user in pain (Flare up)
    input_text = "I am having a lot of stomach pain and urgency today. I need dinner."
    print(f"User Input: {input_text}\n")
    
    response = run_agent(input_text)
    print(f"\nFinal Output: {response}")
    print("--- DEMO END ---")
