import gradio as gr
from manager_llm import ManagerLLM

# Instantiate the ManagerLLM
manager = ManagerLLM()

def execute_task(agent, task_description):
    """
    Executes a task based on the selected agent and the provided task description.
    
    Parameters:
    - agent (str): The role of the agent selected for task execution.
    - task_description (str): Description of the task to be executed.
    
    Returns:
    - str: The result of the task execution.
    """
    # Here you would define how to select an agent and task description
    # For simplicity, let's assume agent is defined by its role (a string)
    # and task_description is also a string
    result = manager.execute_task(agent, task_description)
    return result

# Define the Gradio interface
iface = gr.Interface(
    fn=execute_task,
    inputs=[
        gr.Dropdown(choices=['Agent1', 'Agent2', 'Agent3'], label="Select Agent"),
        gr.Textbox(label="Task Description")
    ],
    outputs=gr.Text(label="Result"),
    title="Task Execution with ManagerLLM"
)

# Launch the Gradio interface
iface.launch()
