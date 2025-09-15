# L5: Automate Event Planning

#In this lesson, you will learn more about Tasks.

## Required libraries
#### !pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29

import warnings
warnings.filterwarnings('ignore')

#import libraries and APIs and LLM

# from crewai import Agent, Crew, Task
from crewAI import Agent, Crew, Task

# you can use gpt-4-turbo

import os
from utils import get_openai_api_key,get_serper_api_key
get_openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4-turbo'
os.environ["SERPER_API_KEY"] = get_serper_api_key()

#crewAI tools
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

# initialize the tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# creating agents

#agent 1 - venue coordinator
venue_coordinator = Agent(
    role="Venue Coordinator",
    goal="Idenify and book a suitable venue for the event based on the event requirements.",
    tools=[search_tool, scrape_tool],
    verbose= True,
    backstory=(
        ""With a keen sense of space and "
        "understanding of event logistics,"
        "you excel at finding and securing"
        "the perfect venue that fits the event's theme,"
        "size and budget."
    )
)

# agent 2 - Logistics manager
logistics_manager = Agent(
    role="Logistics Manager",
    goal="manage all logistics for the event including catering and equipment rentals.",
    tools=[search_tool, scrape_tool],
    backstory=(
        "Organised and detail-oriented" \
        "you ensure that every logistical aspect of the event",
        "from catering to equipment setup",
        "is flawlessly executed to create a seamless experience"
    )
)

#agent 3 - Marketing and communications Agent
marketing_communications_agent = Agent(
    role="Marketing and Communications Agent",
    goal="Effectovely market the event and communicate with participants"
    tools=[search_tool, scrape_tool],
    backstory=(
        "creative and communicative",
        "you craft compelling messages and",
        "engage with potential attendees",
        "to maximize event exposure and participation."
    )
)
