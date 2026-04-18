from agents import Agent, ModelSettings

class AgentCreator:
    def __init__(self, name: str, model_name: str, model_settings: ModelSettings, instructions: str, handoffs: list):
        self.name = name
        self.model_name = model_name
        self.model_settings = model_settings
        self.instructions = instructions
        self.handoffs = handoffs
        self.agent = self.create_agent()

    def create_agent(self) -> Agent:
        agent = Agent(
            name=self.name,
            instructions=self.instructions,
            model=self.model_name,
            model_settings=self.model_settings,
            handoffs=self.handoffs,
        )
        print('Agent initialized: ' + agent.name)
        return agent

    def get_agent(self) -> Agent:
        return self.agent
