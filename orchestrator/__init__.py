import uuid

from agents import Runner, SQLiteSession

from explainer.explainer_agent import ExplainerAgent
from orchestrator.orchestrator_agent import OrchestratorAgent
from planner.planner_agent import PlannerAgent

if __name__ == '__main__':
    explainer = ExplainerAgent().get_agent()
    planner = PlannerAgent().get_agent()
    orchestrator = OrchestratorAgent(handoffs=[explainer, planner]).get_agent()

    #create a UUID
    session_id = str(uuid.uuid4())
    session = SQLiteSession(
        session_id=session_id,
        db_path="finance_agent.db"
    )

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break

        result = Runner.run_sync(orchestrator,
                                 input=user_input,
                                 session=session)
        print("Agent: ", result.final_output)
        print("Handover Agent: ", result.last_agent.name)