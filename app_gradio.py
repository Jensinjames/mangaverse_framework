# app_gradio.py
import graphlib
import grp
from asyncio import Task
import logging
from multiprocessing import Process
import os

import gradio_client
import graphlib
import grp
from asyncio import Task
from agents.content_creation_agent import ContentCreationAgent
from main import manager_llm  # Assuming ManagerLLM and necessary agents are accessible
from agents.content_creation_agent import ContentCreationAgent
from agents.merchandise_customization_agent import MerchandiseCustomizationAgent
from agents.community_engagement_agent import CommunityEngagementAgent
from agents.subscription_management_agent import SubscriptionManagementAgent
from agents.compliance_ethics_agent import ComplianceEthicsAgent
import gradio_client
from agents.content_creation_agent import ContentCreationAgent
from agents.merchandise_customization_agent import MerchandiseCustomizationAgent
from agents.community_engagement_agent import CommunityEngagementAgent
from agents.subscription_management_agent import SubscriptionManagementAgent
from agents.compliance_ethics_agent import ComplianceEthicsAgent
from agents.crew import Crew
import os
from agents.content_creation_agent import ContentCreationAgent
from agents.merchandise_customization_agent import MerchandiseCustomizationAgent
from agents.community_engagement_agent import CommunityEngagementAgent
from agents.subscription_management_agent import SubscriptionManagementAgent
from agents.compliance_ethics_agent import ComplianceEthicsAgent
from handlers.feedback_handler import FeedbackHandler  # Import the FeedbackHandler module

# Define tools and API key
Reflex, TensorFlow, PyTorch, AIModel, MerchandiseManagementSystem, WebSocket, Redis, Stripe, PayPal, ModerationTools = "Reflex", "TensorFlow", "PyTorch", "AIModel", "MerchandiseManagementSystem", "WebSocket", "Redis", "Stripe", "PayPal", "ModerationTools"
os.environ["OPENAI_API_KEY"] = "your_api_key_here"

# Instantiate agents
content_creation_agent = ContentCreationAgent(role='Content Creator', goal='Generate manga content from user submissions', tools=[Reflex, TensorFlow, PyTorch], verbose=True)
merchandise_customization_agent = MerchandiseCustomizationAgent(role='Merchandise Customizer', goal='Customize merchandise with AI-generated images', tools=[AIModel, MerchandiseManagementSystem], verbose=True)
community_engagement_agent = CommunityEngagementAgent(role='Community Manager', goal='Engage community through voting and discussions', tools=[WebSocket, Redis], verbose=True)
subscription_management_agent = SubscriptionManagementAgent(role='Subscription Manager', goal='Manage user subscriptions and perks', tools=[Stripe, PayPal], verbose=True)
compliance_ethics_agent = ComplianceEthicsAgent(role='Compliance and Ethics Monitor', goal='Ensure content and interactions are compliant and ethical', tools=[ModerationTools], verbose=True)

# Define Tasks
tasks = [
    Task(description='Generate manga from submissions', agent=content_creation_agent),
    Task(description='Customize merchandise', agent=merchandise_customization_agent),
    Task(description='Manage community votes', agent=community_engagement_agent),
    Task(description='Process subscriptions', agent=subscription_management_agent),
    Task(description='Review content for compliance', agent=compliance_ethics_agent)
]

# Instantiate and kickoff Crew
mangaverse_crew = Crew(agents=[content_creation_agent, merchandise_customization_agent, community_engagement_agent, subscription_management_agent, compliance_ethics_agent], tasks=tasks, process=Process.sequential, verbose=True)
result = mangaverse_crew.kickoff()
print(result)
logging.info(f"Mangaverse Crew Result: {result}")

def execute_task(agent_choice, task_description):
    """
    Executes a task for the specified agent.

    Args:
        agent_choice (str): The chosen agent for executing the task.
        task_description (str): The description of the task.

    Returns:
        str: The result of the task execution or a success message.

    """
    agent = next((agent for agent in manager_llm.agents if agent.role == agent_choice), None)
    if agent:
        task = Task(description=task_description, agent=agent)
        result = manager_llm.execute_task(agent, task)
        return result or "Task executed successfully."
    else:
        return "Agent not found."


iface = gradio_client.Interface(
    fn=execute_task,
    inputs=[
        graphlib.Dropdown(choices=['Content Creation', 'Merchandise Customization', 'Community Engagement', 'Subscription Management', 'Compliance and Ethics'], label="Choose an Agent"),
        grp.Textbox(label="Task Description")
    ],
    outputs="text",
    title="MangaVerse CrewAI Management"
)

iface.launch()
