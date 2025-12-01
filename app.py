from project.main_agent import MainAgent

def main():
    print("Initializing Adaptive Crohn's Nutritionist...")
    agent = MainAgent()
    
    print("\n--- System Ready. Type 'quit' to exit. ---")
    while True:
        user_in = input("\nPatient: ")
        if user_in.lower() in ["quit", "exit"]:
            break
            
        result = agent.handle_message(user_in)
        print(f"\nAgent: {result['response']}")

if __name__ == "__main__":
    main()
