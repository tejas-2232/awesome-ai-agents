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

# create venue pydnatic object
#create class VenueDetails using pydantic basemodel
#  agents will populate this object with info about different venues by creating different instances of it

from pydantic import BaseModelpip

class VenueDetails(BaseModel):
    name: str
    address: str
    capacity: int
    booking_status: str

# creating tasks
#By using output_json -  you can specify the structure of the output you want from the agent
#by using output_file - yuou can get your outpit in a file
# by setting human_input= True - the task will ask for human feedback (whether you like the resulys or not ) before finalising it

venue_task = Task(
    description= "Find a venue in {event_city}"
                "that meets criteria for {event_topic}."
    expected_output= "All the details of a specifically chosen venue you found to accommodate the event",
    human_input= True,
    output_json= VenueDetails,
    output_file="venue_details.json",
    agent= venue_coordinator
)


# by setting "async_execution= True", it means task can run in pareller with the tasks which come after it

logistics_task = Task(
    description= "Coordinate catering and equipment for an event with {expected_participants} participants on {tentative_date}."
    expected_output= "Confirmation of all logistics arrangements including catering and equipment setup",
    human_input= True,
    async_execution= True,
    agent= logistics_manager
)

marketing_task = Task(
    description= "Promote the {event_topic} aiming to engage at least {expected_participants} potential attendees."
    expected_output = "Report on marketing activities and attendee ebgagement formatted as markdown.",
    async_execution= True,
    output_file= "marketing_report.md",
    agent = marketing_communications_agent
)

