# Task 1. Install ADK and set up your environment

## Enable Vertex AI recommended APIs

Please enable the Vertex AI API by navigating to Vertex AI and following the prompt to enable it.

## Prepare a Cloud Shell Editor tab

1. With your Google Cloud console window selected, open Cloud Shell by pressing the G key and then the S key on your keyboard. Alternatively, you can click the Activate Cloud Shell button (Activate Cloud Shell) in the upper right of the Cloud console.

2. Click Continue.

3. When prompted to authorize Cloud Shell, click Authorize.

4. In the upper right corner of the Cloud Shell Terminal panel, click the Open in new window button Open in new window button.

5. In the Cloud Shell Terminal, enter the following to open the Cloud Shell Editor to your home directory:

```bash
cloudshell workspace ~
```

6. Close any additional tutorial or Gemini panels that appear on the right side of the screen to save more of your window for your code editor.

7. Throughout the rest of this lab, you can work in this window as your IDE with the Cloud Shell Editor and Cloud Shell Terminal.

## Download and install ADK and code samples for this lab

1. Usually the lab will provide a storage bucket link to download the code samples for this lab. But I've provided code project file directly in this lab.

2. Update your PATH environment variable, install ADK, and install some additional requirements for this lab by running the following commands in the Cloud Shell Terminal.

```bash
export PATH=$PATH:"/home/${USER}/.local/bin"
```

```bash
python3 -m pip install google-adk[extensions] -r adk_tools/requirements.txt
```

> Note: google-adk[extensions] is used to install additional dependencies required for Crew AI tools.

<hr>

## Task 2. Create a search app that will be used to ground responses on your own data

In a later task, __you will use the Google-provided Vertex AI Search tool to ground responses on your own data in an AI Applications data store.__ Since the app's data store needs a little while to ingest data, you will set it up now, then use it to ground responses on your data in a later task.

1. In your browser tab still showing the Cloud Console, navigate to __AI Applications__ by searching for it at the top of the console.

2. Select the terms and conditions checkbox and click Continue and __Activate the API.__

3. From the left-hand navigation menu, select __Data Stores.__

4. Select __Create Data Store.__

5. Find the __Cloud Storage__ card and click __Select__ on it.

6. Select __Unstructured documents (PDF, HTML, TXT and more).__

7. __Example documents have been uploaded to Cloud Storage for you. They relate to the fictional discovery of a new planet named Persephone. A fictional planet is used in this case so that the model cannot have learned anything about this planet during its training.__

For a GCS path, enter YOUR_GCP_PROJECT_ID-bucket/planet-search-docs.

8. Click __Continue.__

9. Keep the location set to global.

10. For a data store name, enter: Planet Search

11. Click __Create.__

12. Click __Apps__ on the left-hand nav.

13. Click __Create a new app.__

14. Find the card for a __Custom search (general) app__ and click __Create.__

15. Name the app __Planet Search__

16. Provide a Company name of __Planet Conferences__

17. Click __Continue.__

18. Select the checkbox next to the __Planet Search data store.__

19. Select __Create.__

20. Once your app is created, click the __AI Applications logo__ in the upper left to return to your app dashboard.

21. __Copy the ID__ value of your app displayed in the Apps table. Save it in a text document as you will need it later.

22. For now, you will give the data store some time to ingest its data. Later you will provide it to an agent to ground its responses.

<hr>

# Task 3. Use a LangChain Tool

The LangChain community has created a large number of tool integrations to access many sources of data, integrate with various web products, and accomplish many things. Using community tools within ADK can save you rewriting a tool that someone has already created.

1. Back in your browser tab displaying the Cloud Shell Editor, use the file explorer on the left-hand side to navigate to the directory __adk_tools/langchain_tool_agent__.

2. Write a .env file to provide authentication details for this agent directory by running the following in the Cloud Shell Terminal:

```bash
cd ~/adk_tools
```

```bash
cat << EOF > langchain_tool_agent/.env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=YOUR_GCP_PROJECT_ID
GOOGLE_CLOUD_LOCATION=GCP_LOCATION
MODEL=gemini-2.5-flash
EOF
```

3. Copy the .env file to the other agent directories you will use in this lab by running the following:

```bash
cp langchain_tool_agent/.env crewai_tool_agent/.env
```

```bash
cp langchain_tool_agent/.env function_tool_agent/.env
cp langchain_tool_agent/.env vertexai_search_tool_agent/.env
```

4. Click on the __agent.py__ file in the __langchain_tool_agent__ directory.

5. Notice the import of the __LangchainTool__ class. This is a wrapper class that allows you to use LangChain tools within Agent Development Kit.

6. Add the following code where indicated in the __agent.py__ file to add the __LangChain Wikipedia__ tool to your agent. This will allow your agent to search for information on Wikipedia:

```py

    tools = [
        # Use the LangchainTool wrapper...
        LangchainTool(
            # to pass in a LangChain tool.
            # In this case, the WikipediaQueryRun tool,
            # which requires the WikipediaAPIWrapper as
            # part of the tool.
            tool=WikipediaQueryRun(
              api_wrapper=WikipediaAPIWrapper()
            )
        )
    ]
```

7. Save the file.

8. In the Cloud Shell Terminal, from the adk_tools project directory, launch the Agent Development Kit Dev UI with the following commands:

```bash
adk web
```
__Output:__
```terminal
INFO:     Started server process [2434]
INFO:     Waiting for application startup.
+-------------------------------------------------------+
| ADK Web Server started                                |
|                                                       |
| For local testing, access at http://localhost:8000.   |
+-------------------------------------------------------+

INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit) 
```

9. To view the web interface in a new tab, click the http://127.0.0.1:8000 link in the Terminal output.

10. A new browser tab will open with the ADK Dev UI.

11. From the Select an agent dropdown on the left, select the langchain_tool_agent from the dropdown.

12. Query the agent with:

```text
Who was Grace Hopper?
```
__Output:__

<img width="1190" height="660" alt="image" src="https://github.com/user-attachments/assets/7123cc2d-5611-4cd8-a8f2-045a29d8104f" />

13. Click the agent icon (agent_icon) next to the agent's chat bubble indicating the use of the wikipedia tool.

14. Notice that the content includes a __functionCall__ with the query to Wikipedia.

15. At the top of the tab, click the forward button to move to the next event.

16. Exploring this event, you can see the result retrieved from __Wikipedia__ used to generate the model's response.

17. When you are finished asking questions of this agent, close the dev UI browser tab.

18. Select the Cloud Shell Terminal panel and press __CTRL + C__ to stop the server.

<hr>

# Task 4. Use a CrewAI Tool

You can similarly use CrewAI Tools, using a CrewaiTool wrapper.

1. To do so, using the Cloud Shell Editor file explorer, navigate to the directory __adk_tools/crewai_tool_agent.__

2. Click on the __agent.py__ file in the __crewai_tool_agent__ directory.

3. Notice the import of the __CrewaiTool__ class from ADK and the __ScrapeWebsiteTool__ from __crewai_tools__.

4. Add the following code where indicated in the __agent.py__ file to add the __CrewAI Scrape Website__ tool to your agent, along with a name and description:

```py
    tools = [
        CrewaiTool(
            name="scrape_apnews",
            description=(
                """Scrapes the latest news content from
                the Associated Press (AP) News website."""
            ),
            tool=ScrapeWebsiteTool("https://apnews.com/")
        )
    ]
```

* The __ScrapeWebsiteTool__ will load content from the Associated Press news website __apnews.com__.

5. Save the file.

6. You'll run this agent using the command line interface to be familiar with it as a convenient way to test an agent quickly. In the Cloud Shell Terminal, from the __adk_tools__ project directory, launch the agent with the ADK command line UI with:

```bash
adk run crewai_tool_agent
```

7. While the agent loads, it may display some warnings. You can ignore these. When you are presented the user: prompt, enter:

```text
Get 10 of the latest headlines from AP News.
```

Output:
```terminal
Using Tool: Read website content
[crewai_tool_agent]: Here are the latest headlines from AP News:
...
```
8. Notice that the command line interface also indicates to you when a tool is being used.

9. In the Terminal, respond to the next user: prompt with _exit_ _to exit the command line interface_.

10. Scroll back in your Terminal history to find where you ran __adk run crewai_tool_agent__, and notice that the command line interface provided you a log file to tail. Copy and run that command to view more details of the execution:

```bash
tail -F /tmp/agents_log/agent.latest.log
```

11. Press __CTRL + C__ to stop tailing the log file and return to the command prompt.

<hr>

# Task 5. Use a function as a custom tool

* When pre-built tools don't fully meet specific requirements, you can create your own tools. This allows for tailored functionality, such as connecting to proprietary databases or implementing unique algorithms.

* The most straightforward way to create a new tool is to write a standard Python function with a docstring written in a standard format and pass it to your model as a tool. This approach offers flexibility and quick integration.

* When writing a function to be used as a tool, there are a few important things to keep in mind:

* __Parameters:__ Your function can accept any number of parameters, each of which can be of any JSON-serializable type (e.g., string, integer, list, dictionary). It's important to avoid setting default values for parameters, as the large language model (LLM) does not currently support interpreting them.

* __Return type:__ The preferred return type for a Python Function Tool is a dictionary. This allows you to structure the response with key-value pairs, providing context and clarity to the LLM. For example, instead of returning a numeric error code, return a dictionary with an "error_message" key containing a human-readable explanation. As a best practice, include a "status" key in your return dictionary to indicate the overall outcome (e.g., "success", "error", "pending"), providing the LLM with a clear signal about the operation's state.

* __Docstring:__ The docstring of your function serves as the tool's description and is sent to the LLM. Therefore, a well-written and comprehensive docstring is crucial for the LLM to understand how to use the tool effectively. Clearly explain the purpose of the function, the meaning of its parameters, and the expected return values.


> Define a function and use it as a tool by completing the following steps:

1. Using the Cloud Shell Editor file explorer, navigate to the directory __adk_tools/function_tool_agent.__

2. In the __function_tool_agent__ directory, click on the __agent.py__ file.

3. Notice that the functions __get_date()__ and __write_journal_entry()__ have docstrings formatted properly for an ADK agent to know when and how to use them. They include:

* A clear description of what each function does
* an __Args:__ section describing the function's input parameters with JSON-serializable types
* a __Returns:__ section describing what the function returns, with the preferred response type of a dict

4. To pass the function to your agent to use as a tool, add the following code where indicated in the __agent.py__ file:

```py
    tools=[get_date, write_journal_entry]
```

5. Save the file.

6. You will run this agent using the dev UI to see how its tools allow you to easily visualize tool requests and responses. In the Cloud Shell Terminal, from the __adk_tools__ project directory, run the dev UI again with the following command (if the server is still running from before, stop the running server first with __CTRL + C__, then run the following to start it again):

```bash
adk web
```

7. Click the __http://127.0.0.1:8000__ link in the Terminal output.

8. A new browser tab will open with the __ADK Dev UI.__

9. From the __Select an agent__ dropdown on the left, select the __function_tool_agent.__

10. Start a conversation with the agent with:

```text
hello
```

11. The agent should prompt you about your day. _Respond with a sentence about how your day is going (like It's been a good day. I did a cool ADK lab.)_ and it will write a journal entry for you.

__Example Output:__

<img width="1640" height="954" alt="image" src="https://github.com/user-attachments/assets/c0726e70-4b3f-4821-b8ec-b4be155e6743" />

12. Notice that your agent shows buttons for your custom tool's request and the response. You can click on each to see more information about each of these events.

13. Close the dev UI tab.

14. In the Cloud Shell Editor, you can find your dated journal entry file in the __adk_tools__ directory. (You may want to use the Cloud Shell Editor's menu to enable View > Word Wrap to see the full text without lots of horizontal scrolling.)

15. Stop the server, by clicking on the Cloud Shell Terminal panel and pressing __CTRL + C.__

```text
__Best practices for writing functions to be used as tools include__

* __Fewer Parameters are Better:__ Minimize the number of parameters to reduce complexity.
* __Use Simple Data Types:__ Favor primitive data types like str and int over custom classes when possible.
* __Use Meaningful Names:__ The function's name and parameter names significantly influence how the LLM interprets and utilizes the tool. Choose names that clearly reflect the function's purpose and the meaning of its inputs.
* __Break Down Complex Functions:__ Instead of a single update_profile(profile: Profile) function, create separate functions like update_name(name: str), update_age(age: int), etc.
* __Return status:__ Include a "status" key in your return dictionary to indicate the overall outcome (e.g., "success", "error", "pending") to provide the LLM a clear signal about the operation's state.
```
<hr>

# Task 6. Use Vertex AI Search as a tool to ground on your own data

* In this task, you will discover how easy it is to deploy a RAG application using an Agent Development Kit agent with the built-in Vertex AI Search tool from Google and the AI Applications data store you created earlier.

1. Return to your __Cloud Shell Editor tab__ and select the __adk_tools/vertexai_search_tool_agent__ directory.

2. Click on the __agent.py__ file in the __vertexai_search_tool_agent__ directory.

3. Add an import of the __VertexAiSearchTool__ class where indicated at the bottom of the imports:

```py
from google.adk.tools import VertexAiSearchTool
```

4. Update the code where the __VertexAiSearchTool__ is instantiated. In the path being passed to __data_store_id__, update __YOUR_PROJECT_ID__ to __YOUR_GCP_PROJECT_ID__ and update __YOUR_SEARCH_APP_ID__ to the search app ID you copied in the earlier task.

5.Add the following line where indicated in the agent definition to provide the agent the tool:

```py
    tools=[vertexai_search_tool]
```

6. Save the agents.py file.

```text
You can confirm your data store is ready for use by selecting the data store's name on the __AI Applications > Data Stores__ page in the console.

The __ACTIVITY__ and __DOCUMENTS__ tabs provide statuses on the import and indexing of your documents. When the __ACTIVITY__ tab reports __"Import completed"__, your data store should be ready to query.
```

7. In the Cloud Shell Terminal, from the __adk_tools__ project directory, launch the command line interface with the following command. You'll include the __--reload_agents__ flag so that the Dev UI reloads your agent when you make changes.

```bash
adk web --reload_agents
```

```text
Note: If you did not shut down your previous adk web session, select the Cloud Shell Terminal panel where it is running and press __CTRL + C__. If you can't find the Cloud Shell Terminal tab you used before, the default port of 8000 will be blocked, but you can launch the Dev UI with a new port by using __adk web --port 8001__.

```

8. Click the __http://127.0.0.1:8000__ to open the ADK Dev UI.


9. From the __Select an agent__ dropdown on the left, select the __vertexai_search_tool_agent.__

10. Query the agent about the fictional planet described in your Cloud Storage documents with:

```text
Is the new planet Persephone suitable for habitation?
```

__Example output (yours may be a little different)__

```text
Based on the "Persephone Survey: What we Know So Far" document, Persephone exhibits several characteristics that suggest it could be habitable:

- Location: It orbits within the habitable zone of its star.
- Temperature: The average surface temperature is estimated to be around 18°C (64°F).
...
```

<hr>

## Using AgentTool to integrate search tools with other tools

Search tools come with an implementation limitation in that you cannot mix search tools and non-search tools in the same agent. To get around this, you can wrap an agent with a search tool with an AgentTool, and then use that agent-as-a-tool to conduct searches alongside other tools.

To see that in action:

1. Ensure you have the __adk_tools/vertexai_search_tool_agent/agent.py__ file open.

2. Update the __root_agent's__ tools parameter to include the __get_date__ function tool:

```py
    tools=[vertexai_search_tool, get_date]
```

3. Save the file.

4. In the ADK Dev UI, ask the agent:

```text
What is today's date?
```
__Expected output:__
<img width="1368" height="202" alt="image" src="https://github.com/user-attachments/assets/54a899bd-aa98-4a77-8a8b-734dec1b2169" />

5. Back in the adk_tools/vertexai_search_tool_agent/agent.py file, paste the following code above your root_agent. This agent is dedicated to using the search tool and contains both the search tool and instructions to use it:

```py
vertexai_search_agent = Agent(
    name="vertexai_search_agent",
    model=os.getenv("MODEL"),
    instruction="Use your search tool to look up facts.",
    tools=[vertexai_search_tool]
)
```

6. Then replace the root_agent's tools parameter with the following to wrap the agent created in the previous step with the AgentTool :

```py
    tools=[
        AgentTool(vertexai_search_agent, skip_summarization=False),
        get_date
    ]
```

7. Now you can query your agent and receive both search results and use the __get_date()__ function.

Back in the ADK Dev UI browser tab, click + New Session.

8. Ask again:

```text
What is today's date?
```

The agent should respond with the correct date.

9. Then to invoke the search tool, ask:

```text
When is the PlanetCon conference?
```

__Expected output:__

```text
The PlanetCon: Persephone conference is scheduled for October 26th - 28th, 2028.
```

10. Feel free to ask the agent more questions about this new planet and the conference where its discovery will be announced. When you are satisfied, close the dev UI tab.

11. When you are finished asking questions of this agent, close the browser tab, select the Cloud Shell Terminal window where the server is running, and press __CTRL + C__ to stop the server.


## Even more Types of Tools

The following tool types are good for you to know about, but you will not implement them in this lab.

## The LongRunningFunctionTool Class

This tool is a subclass of FunctionTool. It's designed for tasks that require a significant amount of processing time that should be called without blocking the agent's execution.

When using a __LongRunningFunctionTool__, your Python function can initiate the long-running operation and optionally return an intermediate result to keep the model and user informed about the progress (e.g., status updates or estimated completion time). The agent can then continue with other tasks.

An example is a __human-in-the-loop__ scenario where the agent needs human approval before proceeding with a task.

## Application Integration workflows as tools

With [Application Integration](https://cloud.google.com/application-integration/docs/overview), you can use a drag-and-drop interface in the Google Cloud Console to build tools, data connections, and data transformations using __Integration Connector’s 100+ pre-built connectors__ for Google Cloud products and third-party systems like Salesforce, ServiceNow, JIRA, SAP, and more. You can then use an ADK ApplicationIntegrationToolset to [allow your agents to connect to those sources or call your workflows.](https://google.github.io/adk-docs/tools/google-cloud-tools/#application-integration-tools)
