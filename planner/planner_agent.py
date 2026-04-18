from pathlib import Path

from agents import ModelSettings
from openai.types import Reasoning
from common.agent_creator import AgentCreator
from common.utils import read_file

PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "planner_prompt.txt"


class PlannerAgent:
    def __init__(self):
        instructions = read_file(PROMPT_PATH)
        model_settings = ModelSettings(reasoning=Reasoning(effort="medium"), verbosity="low")
        self.creator = AgentCreator(
            name='planner',
            model_name='gpt-5.4',
            model_settings=model_settings,
            instructions=instructions,
            handoffs=[]
        )

    def get_agent(self):
        return self.creator.get_agent()
