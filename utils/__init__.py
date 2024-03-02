from main import ManagerLLM

# Define the variable "mangaverse_crew"
mangaverse_crew = ...

# Instantiate the ManagerLLM
manager_llm = ManagerLLM()

# Example of passing the ManagerLLM to an agent (this might vary based on your CrewAI framework's design)
for agent in mangaverse_crew.agents:
    agent.set_manager_llm(manager_llm)

# Alternatively, if your CrewAI framework supports it, you might set the ManagerLLM at the Crew level
mangaverse_crew.set_manager_llm(manager_llm)
