from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

from app.tools import get_current_time, say_bye

model = LiteLlm(
    model="ollama/gemma4:e2b",
    api_base="http://192.168.1.200:11434"
)

root_agent = Agent(
    name="root_agent",
    model=model,
    description="Tells the current time in a specified city.",
    instruction=(
        "You are a helpful assistant. You have ONLY these tools available:\n"
        "1. get_current_time(city) - Returns the current time in the given city.\n"
        "2. say_bye() - Returns a goodbye message.\n\n"
        "RULES:\n"
        "- When a user asks for the time, call get_current_time with the city name.\n"
        "- When a user says goodbye or bye, call say_bye.\n"
        "- NEVER call any tool that is not listed above.\n"
        "- NEVER use 'root_agent' as a tool name.\n"
        "- Respond directly for any other questions."
    ),
    tools=[get_current_time, say_bye],
)