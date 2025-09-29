from google.adk.agents import LlmAgent
from typing import List

from google.adk.agents.remote_a2a_agent import RemoteA2aAgent


# Agents

root_agent = LlmAgent(
            model='gemini-2.0-flash-001',
            name='slide_content_agent',
            description='An agent that writes content for slide decks.',
            #after_tool_callback=self._handle_auth_required_task,
            instruction="""
                A user will ask you to create content for a slide to communicate an idea.
                Write a short headline about this idea.
                Write 1-2 sentences of body text about this idea.
                Share these with the user.
                Then transfer to the 'illustration_agent' to generate an illustration related to this idea.
                """,
	# Add the sub_agents parameter below

        )