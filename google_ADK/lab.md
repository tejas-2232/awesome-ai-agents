### Setup and requirements
#### These are notes from Google self-paced labs

Before you click the Start Lab button

Read these instructions. Labs are timed and you cannot pause them. The timer, which starts when you click Start Lab, shows how long Google Cloud resources will be made available to you.

This Qwiklabs hands-on lab lets you do the lab activities yourself in a real cloud environment, not in a simulation or demo environment. It does so by giving you new, temporary credentials that you use to sign in and access Google Cloud for the duration of the lab.

What you need
To complete this lab, you need:

Access to a standard internet browser (Chrome browser recommended).
Time to complete the lab.
Note: If you already have your own personal Google Cloud account or project, do not use it for this lab.

Note: If you are using a Pixelbook, open an Incognito window to run this lab.


## Task 1. Install ADK and set up your environment

__Enable Vertex AI recommended APIs:__
You could enable it by navigating to Vertex AI and following the prompt to enable it.


__Prepare a Cloud Shell Editor tab:__

1. With your Google Cloud console window selected, open Cloud Shell by pressing the G key and then the S key on your keyboard. Alternatively, you can click the Activate Cloud Shell button (Activate Cloud Shell) in the upper right of the Cloud console.

2. Click Continue.

3. When prompted to authorize Cloud Shell, click Authorize.

4. In the upper right corner of the Cloud Shell Terminal panel, click the Open in new window button Open in new window button.

5. In the Cloud Shell Terminal, enter the following to open the Cloud Shell Editor to your home directory:

> cloudshell workspace ~

6. Close any additional tutorial or Gemini panels that appear on the right side of the screen to save more of your window for your code editor.

7. Throughout the rest of this lab, you can work in this window as your IDE with the Cloud Shell Editor and Cloud Shell Terminal.


__Download and install the ADK and code samples for this lab__

Update your PATH environment variable and install ADK by running the following commands in the Cloud Shell Terminal. Note: You will specify the version to ensure that the version of ADK that you install corresponds to the version used in this lab:

```bash
export PATH=$PATH:"/home/${USER}/.local/bin"
python3 -m pip install google-adk==1.9.0
```

Paste the following commands into the Cloud Shell Terminal to copy a file from a Cloud Storage bucket, and unzip it, creating a project directory with code for this lab:
```bash
gcloud storage cp gs://qwiklabs-gcp-03-779d2552a2b3-bucket/adk_project.zip ./adk_project.zip
unzip adk_project.zip
```

Install additional lab requirements with:
```bash
python3 -m pip install -r adk_project/requirements.txt
```

<hr>

## Task 2. Review the structure of Agent Development Kit project directories

1. In the Cloud Shell Editor's file explorer pane, find the adk_project folder. Click it to toggle it open.
2. This directory contains three other directories: my_google_search_agent, app_agent, and llm_auditor. Each of these directories represents a separate agent. Separating agents into their own directories within a project directory provides organization and allows Agent Development Kit to understand what agents are present.
3. Click on the `my_google_search_agent` to explore an agent directory.
4. Notice that the directory contains an ```__init__.py``` file and an agent.py file. An ```__init__.py```.py file is typically used to identify a directory as a Python package that can be imported by other Python code. Click the init.py file to view its contents.
5. Notice that the ```__init__.py``` file contains a single line, which imports from the agent.py file. ADK uses this to identify this directory as an agent package:

```bash
from . import agent
```

6. Now click on the agent.py file. This file consists of a simple agent. You will equip it with a powerful tool: the ability to search the internet using Google Search. Notice a few things about the file:
* Notice the imports from google.adk: the Agent class and the google_search tool from the tools module
* Read the code comments that describe the parameters that configure this simple agent.

7. To use the imported google_search tool, it needs to be passed to the agent. Do that by pasting the following line into the agent.py file where indicated at the end of the Agent object creation:

   ```py
   tools=[google_search]
   ```

8. Save the file.

> Tools enable an agent to perform actions beyond generating text. In this case, the google_search tool allows the agent to decide when it would like more information than it already has from its training data. It can then write a search query, use Google Search to search the web, and then base its response to the user on the results. __When a model bases its response on additional information that it retrieves, it is called "grounding,"__ and this overall process is known as __"retrieval-augmented generation" or "RAG."__

> You can learn more about how to use tools with ADK in the lab Empower ADK agents with tools.

<hr>

## Task 3. Run the agent using the ADK's Dev UI

ADK includes a development UI designed to run locally to help you develop and test your agents. It can help you visualize what each agent is doing and how multiple agents interact with one another. You will explore this interface in this task.

> When you run an agent, the ADK needs to know who is requesting the model API calls. You can provide this information in one of two ways. You can:
> 1. Provide a Gemini API key.
> 2. Authenticate your environment with Google Cloud credentials and associate your model API calls with a Vertex AI project and location.

__In this lab, you will take the Vertex AI approach.__


1. In the Cloud Shell Editor menus, select View > Toggle Hidden Files to view or hide your hidden files (files with a period at the start of their filename are hidden by default in most file systems). You may need to scroll down in this menu to find the Toggle Hidden Files option.

2. In the Cloud Shell Editor file explorer pane, navigate to the adk_project/my_google_search_agent directory.
3. Select the .env file in the my_google_search_agent directory.
4. Paste these values over what is currently in the file to update the file to include your project ID:

```sh
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=YOUR_GCP_PROJECT_ID
GOOGLE_CLOUD_LOCATION=GCP_LOCATION
MODEL=gemini-2.5-flash
```

5. Save the file


> These variables play the following roles:
> __GOOGLE_GENAI_USE_VERTEXAI=TRUE__ indicates that you will use Vertex AI for authentication as opposed to Gemini API key authentication.

> __GOOGLE_CLOUD_PROJECT__ and __GOOGLE_CLOUD_LOCATION__ provide the project and location with which to associate your model calls.

> __MODEL__ is not required, but is stored here so that it can be loaded as another environment variable. This can be a convenient way to try different models in different deployment environments.

When you test your agent using ADK's dev UI or the command-line chat interface, they will load and use an agent's `.env` file if one is present or else look for environment variables with the same names as those set here.

6. In the Cloud Shell Terminal, ensure you are in the adk_project directory where your agent subdirectories are located by running:

```bash
cd ~/adk_project
```

7. Launch the Agent Development Kit Dev UI with the following command:

```bash
adk web
```

<img width="602" height="299" alt="image" src="https://github.com/user-attachments/assets/6f6deb81-771a-4895-ba80-693a82c61f82" />

8. To view the web interface in a new tab, click the http://127.0.0.1:8000 link in the Terminal output, which will link you via proxy to this app running locally on your Cloud Shell instance.

9. A new browser tab will open with the ADK Dev UI.

10. From the Select an agent dropdown on the left, select my_google_search_agent.


<img width="2492" height="1318" alt="image" src="https://github.com/user-attachments/assets/88d36f34-1301-49bb-8b17-6af3ac523b62" />

11. In order to encourage the agent to use its Google Search tool, enter the question:

```text
What is some recent global news?
```

12. You will notice from the results that the agent is able to use Google Search to get up-to-date information, rather than having its information stop on the date when its model was trained.

```
A response using grounding with Google search includes ready-to-display HTML "Search Suggestions" like those you see at the bottom of the agent's response. When you use grounding with Google Search, you are required to display these suggestions, which help users follow up on the information the model used for its response.
```

13. Notice that in the left side bar, you are in the Trace tab by default. Click on your last query text _(What is some recent global news?)_ to see a trace of how long different parts of your query took to execute. You can use this to debug more complex executions involving tool calls to understand how various processes contribute to the latency of your responses.

<img width="1062" height="484" alt="image" src="https://github.com/user-attachments/assets/145bd2a8-2821-4671-aecb-2d7ed6e89c19" />

14. Click the agent icon 🤖 next to the agent's response (or an event from the list on the Events tab) to inspect the event returned by the agent, which includes the content returned to the user and groundingMetadata which details the search results that the response was based on.

15. When you are finished exploring the dev UI, close this browser tab and return to your browser tab with the Cloud Shell Terminal, click on the terminal's pane, and press CTRL + C to stop the web server.

<hr>

## Task 4. Run an agent programmatically

While the dev UI is great for testing and debugging, it is not suitable for presenting your agent to multiple users in production.

To run an agent as part of a larger application, you will need to include a few additional components in your agent.py script that the web app handled for you in the previous task. Proceed with the following steps to open a script with these components to review them.

1. In the Cloud Shell Terminal run the following commands to export environment variables. You can use this approach to set environment variables for all of your agents to use if they do not have a .env file in their directory:

```bash
export GOOGLE_GENAI_USE_VERTEXAI=TRUE
export GOOGLE_CLOUD_PROJECT=YOUR_GCP_PROJECT_ID
export GOOGLE_CLOUD_LOCATION=GCP_LOCATION
export MODEL=gemini-2.5-flash
```

2. In the Cloud Shell Editor file browser, select the adk_project/app_agent directory.
3. Select the agent.py file in this directory.
4. This agent is designed to run as part of an application. Read the commented code in agent.py, paying particular attention to the following components in the code:

| Component                               | Feature | Description |
|-----------------------------------------|---------|-------------|
| InMemoryRunnner()                       | Oversight of agent execution |The Runner is the code responsible for receiving the user's query, passing it to the appropriate agent, receiving the agent's response event and passing it back to the calling application or UI, and then triggering the following event. You can read more in the ADK [documentation about the event loop.](https://google.github.io/adk-docs/runtime/#the-heartbeat-the-event-loop-inner-workings) |
| runner.session_service.create_session() | Conversation history & shared state |  Sessions allow an agent to preserve state, remembering a list of items, the current status of a task, or other 'current' information. This class creates a local session service for simplicity, but in production this could be handled by a database.|
| types.Content() and types.Part()        |   Structured, multimodal messages      |   Instead of a simple string, the agent is passed a Content object which can consist of multiple Parts. This allows for complex messages, including text and multimodal content to be passed to the agent in a specific order.          |

```text
When you ran the agent in the dev UI, it created a session service, artifact service, and runner for you. When you write your own agents to deploy programmatically, it is recommended that you provide these components as external services rather than relying on in-memory versions.
```

5. Notice that the script includes a hardcoded query, which asks the agent: "What is the capital of France?"

6. Run the following command in the Cloud Shell Terminal to run this agent programmatically:

```bash
python3 app_agent/agent.py
```

__Selected Output:__

```output
trivia_agent: The capital of France is Paris.
```

7. You can also define specific input and/or output schema for an agent.

You will now add imports for the [Pydantic schema classes](https://docs.pydantic.dev/1.10/usage/schema/) BaseModel and Field and use them to define a schema class consisting of just one field, with a key of "capital" and a string value intended for the name of a country's capital city. You can paste these lines into your __app_agent/agent.py__ file, just after your other imports:

```py
from pydantic import BaseModel, Field

class CountryCapital(BaseModel):
    capital: str = Field(description="A country's capital.")
```

> Important note: When you define an output schema, you cannot use tools or agent transfers.

8. Within your root_agent's Agent definition, add these parameters to disable transfers (as you are required to do when using an output schema) and to set the output to be generated according to the CountryCapital schema you defined above:

```py
        disallow_transfer_to_parent=True,
        disallow_transfer_to_peers=True,
        output_schema=CountryCapital,
```

9. Run the agent script again to see the response following the output_schema:

```bash
python3 app_agent/agent.py
```

__Selected Output:__

```
** User says: {'parts': [{'text': 'What is the capital of France?'}], 'role': 'user'}
** trivia_agent: {"capital": "Paris"}
```

<hr>

