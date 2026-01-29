import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel
from tools.search import web_search

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found! Check your .env file in the root folder.")


# 1. Initialize the OpenAI-compatible Gemini client
# Note the specific base_url for Google's OpenAI endpoint
gemini_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 2. Wrap the client in the Agents SDK Model
# I recommend 'gemini-1.5-flash' for the worker and 'gemini-1.5-pro' for the planner

research_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=gemini_client
)

planner_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=gemini_client
)

# 3. Define the Agents using the Gemini models
researcher = Agent(
    name="Researcher",
    instructions=(
        "You are a web-browsing specialist. "
        "FORBIDDEN: Do not use your internal memory. "
        "MANDATORY: You MUST use the 'web_search' tool to get results."
        "PIPELINE RULE: "
        "1. Call 'web_search' to get technical data. "
        "2. Only after this, you may provide a summary "
        "to the Strategist. "
        "If you don't use the tool, you have failed your mission."
        "If the tool returns 'No results', report that exactly; do not make things up."
        ),
    tools=[web_search],
    model=research_model
)

strategist = Agent(
    name="Strategist",
    instructions=(
        "You are the Lead Strategist. "
        "1. Analyze the user's goal in goal.txt and create a plan. "
        "2. Use the expert provided data"
        "3. Summarize everything"
        "to write the best possible Markdown. "
        "The user MUST receive final output in Markdown format."
    ),
tools=[
        # Provide the name and description here!
        researcher.as_tool(
            tool_name="technical_research_expert",
            tool_description="Finds technical details. Use this first."
        )
    ],
    model=planner_model
)
