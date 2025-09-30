# Task 1. Install ADK and set up your environment

__Enable Vertex AI recommended APIs__

### Prepare a Cloud Shell Editor tab

1. In the Cloud Shell Terminal, enter the following to open the Cloud Shell Editor to your home directory:

```bash
cloudshell workspace ~
```

2. Close any additional tutorial or Gemini panels that appear on the right side of the screen to save more of your window for your code editor.

3. Throughout the rest of this lab, you can work in this window as your IDE with the Cloud Shell Editor and Cloud Shell Terminal.

### Download and install ADK and code samples for this lab

1. Usually the lab will provide a storage bucket link to download the code samples for this lab. But I've provided code project file directly in this lab.

2. Update your PATH environment variable, install ADK, and install some additional requirements for this lab by running the following commands in the Cloud Shell Terminal.

```bash
export PATH=$PATH:"/home/${USER}/.local/bin"
```

```bash
python3 -m pip install google-adk -r adk_multiagent_systems/requirements.txt
```

> Note: google-adk is used to install ADK.

<hr>

# Task 2. Explore transfers between parent, sub-agent, and peer agents

The conversation always begins with the agent defined as the __root_agent__ variable.

The default behavior of a __parent__ agent is to understand the description of each __sub-agent__ and __peer__ agent and determine if control of the conversation should be transferred to a sub-agent at any point.

You can help guide those transfers in the parent's __instruction__ by referring to the sub-agents by name (the values of their name parameter, not their variable names). Try an example:

1. In the Cloud Shell Terminal, run the following to create a .env file to authenticate the agent in the parent_and_subagents directory.

```bash
cd ~/adk_multiagent_systems
```

```bash
cat << EOF > parent_and_subagents/.env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=qwiklabs-gcp-03-445dbb776b59
GOOGLE_CLOUD_LOCATION=us-central1
MODEL=gemini-2.5-flash
EOF
```

2. Run the following command to copy that `.env` file to the workflow_agents directory, which you will use later in the lab:

```bash
cp parent_and_subagents/.env workflow_agents/.env
```

3. In the Cloud Shell Editor file explorer pane, navigate to the adk_multiagent_systems/parent_and_subagents directory.

4. Click on the `agent.py` file to open it.

> Tip: Because Python code requires that we define our sub-agents before we can add them to an agent, in order to read an agent.py file in the order of the conversation flow, you may want to start reading with the bottom agent and work back towards the top.

5. Notice that there are three agents here:

* a `root_agent` named `steering` (its name is used to identify it in ADK's dev UI and command line interfaces). It asks the user a question (if they know where they'd like to travel or if they need some help deciding), and the user's response to that question will help this steering agent know which of its two sub-agents to steer the conversation towards. Notice that it only has a simple instruction that does not mention the sub-agents, but it is aware of its sub-agents' descriptions.

* a `travel_brainstormer` that helps the user brainstorm destinations if they don't know where they would like to visit.

* an `attractions_planner` that helps the user build a list of things to do once they know which country they would like to visit.

6. Make `travel_brainstormer` and `attractions_planner` sub-agents of the `root_agent` by adding the following line to the creation of the `root_agent`:

```python
    sub_agents=[travel_brainstormer, attractions_planner]
```


7. Save the file.

8. Note that you don't add a corresponding parent parameter to the sub-agents. The hierarchical tree is defined only by specifying `sub_agents` when creating parent agents.

9. In the Cloud Shell Terminal, run the following to use the ADK command line interface to chat with your agent:

```bash
cd ~/adk_multiagent_systems
```

```bash
adk run parent_and_subagents
```

10. When you are presented the `[user]:` prompt, greet the agent with:

```bash
hello
```

__Example output (yours may be a little different):__

```
user: hello
[steering]: Hi there! Do you already have a country in mind for your trip, or would you like some help deciding where to go?
```

11. Tell the agent:

```
I could use some help deciding.
```

__Example output (yours may be a little different):__

```
user: I could use some help deciding.
[travel_brainstormer]: Okay! To give you the best recommendations, I need to understand what you're looking for in a trip.
...
```

12. Notice from the name `[travel_brainstormer]` in brackets in the response that the `root_agent` (named `[steering]`) has transferred the conversation to the appropriate sub-agent based on that sub-agent's `description` alone.

13. At the `user:` prompt, enter `exit` to end the conversation.

14. You can also provide your agent more detailed instructions about when to transfer to a sub-agent as part of its instructions. In the `agent.py` file, add the following lines to the `root_agent`'s instruction:

```text
        If they need help deciding, send them to
        'travel_brainstormer'.
        If they know what country they'd like to visit,
        send them to the 'attractions_planner'.
```

15. Save the file.



16. In the Cloud Shell Terminal, run the following to start the command line interface again:

```bash
adk run parent_and_subagents
```

17. Greet the agent with:

```bash
hello
```

18. Reply to the agent's greeting with:

```text
I would like to go to Japan.
```

__Example output (yours may be a little different):__

```
user: I would like to go to Japan.
[attractions_planner]: Okay, I can help you with that! Here are some popular attractions in Japan:

*   **Tokyo:**
    *   Senso-ji Temple
    *   Shibuya Crossing
    *   Tokyo Skytree
*   **Kyoto:**
    ...
```
19. Notice that you have been transferred to the other sub-agent, attractions_planner.

20. Reply with:

```text
Actually I don't know what country to visit.
```

__Example output (yours may be a little different):__

```
user: actually I don't know what country to visit
[travel_brainstormer]: Okay! I can help you brainstorm some countries for travel...
```

21. Notice you have been transferred to the travel_brainstormer agent, which is a peer agent to the attractions_planner. This is allowed by default. If you wanted to prevent transfers to peers, you could have set the disallow_transfer_to_peers parameter to True on the attractions_planner agent.

22. At the user prompt, type `exit` to end the session.

<hr>
<hr>

# Task 3. Use session state to store and retrieve specific information
Each conversation in ADK is contained within a Session that all agents involved in the conversation can access. A session includes the conversation history, which agents read as part of the context used to generate a response. The session also includes a `session state dictionary` that you can use to take greater control over the most important pieces of information you would like to highlight and how they are accessed.

This can be particularly helpful to pass information between agents or to maintain a simple data structure, like a list of tasks, over the course of a conversation with a user.

To explore adding to and reading from state:

1. Return to the file `adk_multiagent_systems/parent_and_subagents/agent.py`

2. Paste the following function definition after the `# Tools` header:

```python
def save_attractions_to_state(
    tool_context: ToolContext,
    attractions: List[str]
) -> dict[str, str]:
    """Saves the list of attractions to state["attractions"].

    Args:
        attractions [str]: a list of strings to add to the list of attractions

    Returns:
        None
    """
    # Load existing attractions from state. If none exist, start an empty list
    existing_attractions = tool_context.state.get("attractions", [])

    # Update the 'attractions' key with a combo of old and new lists.
    # When the tool is run, ADK will create an event and make
    # corresponding updates in the session's state.
    tool_context.state["attractions"] = existing_attractions + attractions

    # A best practice for tools is to return a status message in a return dict
    return {"status": "success"}
```

3. In this code, notice:

* The session is passed to your tool function as `ToolContext`. All you need to do is assign a parameter to receive it, as you see here with the parameter named `tool_context`. You can then use `tool_context` to access session information like conversation history (through `tool_context.events`) and the session state dictionary (through `tool_context.state`). When the `tool_context.state` dictionary is modified by your tool function, those changes will be reflected in the session's state after the tool finishes its execution.

* The docstring provides a clear description and sections for argument and return values.

* The commented function code demonstrates how easy it is to make updates to the state dictionary.

4. Add the tool to the `attractions_planner` agent by adding the `tools` parameter when the agent is created:

```python
    tools=[save_attractions_to_state]
```

5. Add the following bullet points to the `attractions_planner` agent's existing instruction:

```text
        - When they reply, use your tool to save their selected attraction
        and then provide more possible attractions.
        - If they ask to view the list, provide a bulleted list of
        { attractions? } and then suggest some more.
```

6. Notice the section in curly braces: `{ attractions? }`. This ADK feature, key templating, loads the value of the attractions key from the state dictionary. The question mark after the attractions key prevents this from erroring if the field is not yet present.

7. You will now run the agent from the web interface, which provides a tab for you to see the changes being made to the session state. Launch the Agent Development Kit Web UI with the following command:

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

8. To view the web interface in a new tab, click the http://127.0.0.1:8000 link in the Terminal output.

9. A new browser tab will open with the ADK Dev UI.

10. From the `Select an agent` dropdown on the left, select the `parent_and_subagents` agent from the dropdown.

11. Start the conversation with: `hello`

12. After the agent greets you, reply with:

```text
I'd like to go to Egypt.
```

You should be transferred to the `attractions_planner` and be provided a list of attractions.

13.Choose an attraction, for example:

```text
I'll go to the Sphinx
```

14.You should receive an acknowledgement in the response, like: _Okay, I've saved The Sphinx to your list. Here are some other attractions..._

15. Click the response tool box (marked with a check mark) to view the event created from the tool's response. Notice that it includes an `actions` field which includes `state_delta` describing the changes to the state.

16. You should be prompted by the agent to select more attractions. Reply to the agent by __naming one of the options it has presented.__

17. On the left-hand navigation menu, click the "X" to exit the focus on the event you inspected earlier.

18. Now in the sidebar, you should see the list of events and a few tab options. Select the `State` tab. Here you can view the current state, including your attractions array with the two values you have requested.

<img width="960" height="432" alt="image" src="https://github.com/user-attachments/assets/2b430912-01f3-4c68-9d61-b4fb50bc2927" />

19. Send this message to the agent:

```text
What is on my list?
```

20. It should return your list formatted as a bulleted list according to its `instruction`.

21. When you are finished experimenting with the agent, close the web browser tab and press CTRL + C in the Cloud Shell Terminal to stop the server.

Later in this lab, you will demonstrate how to use state to communicate between agents.

<hr>

# Workflow Agents

`Parent to sub-agent` transfers are ideal when you have multiple specialist sub-agents, and you want the user to interact with each of them.

However, if you would like agents to act one-after-another without waiting for a turn from the user, you can use `workflow agents`. Some example scenarios when you might use workflow agents include when you would like your agents to:

* __Plan and Execute:__ When you want to have one agent prepare a list of items, and then have other agents use that list to perform follow-up tasks, for example writing sections of a document

* __Research and Write:__ When you want to have one agent call functions to collect contextual information from Google Search or other data sources, then another agent use that information to produce some output.

* __Draft and Revise:__ When you want to have one agent prepare a draft of a document, and then have other agents check the work and iterate on it

To accomplish these kinds of tasks, _workflow agents_ have sub-agents and guarantee that each of their sub-agents acts. Agent Development Kit provides three built-in workflow agents and the opportunity to define your own:

* __SequentialAgent:__
* __LoopAgent:__
* __ParallelAgent:__


* Throughout the rest of this lab, you will build a multi-agent system that uses multiple LLM agents, workflow agents, and tools to help control the flow of the agent.

* Specifically, you will build an agent that will develop a pitch document for a new hit movie: a biographical film based on the life of a historical character.

* Your `sub-agents` will handle the research, an iterative writing loop with a screenwriter and a critic, and finally some additional sub-agents will help brainstorm casting ideas and use historical box office data to make some predictions about box office results.

In the end, your multi-agent system will look like this (you can click on the image to see it larger):

<img width="2112" height="960" alt="image" src="https://github.com/user-attachments/assets/75ac31ba-0452-44d1-ab7a-493dc2181c83" />

But you will begin with a simpler version.

<hr>

# Task 4. Begin building a multi-agent system with a SequentialAgent

The `SequentialAgent` executes its sub-agents in a linear sequence. Each sub-agent in its sub_agents list is run, one after the other, in the order they are defined.

This is ideal for workflows where tasks must be performed in a specific order, and the output of one task serves as the input for the next.

In this task, you will run a `SequentialAgent` to build a first version of your movie pitch-development multi-agent system. The first draft of your agent will be structured like this:

<img width="2112" height="960" alt="image" src="https://github.com/user-attachments/assets/39851a46-200c-451f-b0de-1278092b04a3" />

A `root_agent` named `greeter` to welcome the user and request a historical character as a movie subject

* A `SequentialAgent` called `film_concept_team` will include:

a. A `researcher` to learn more about the requested historical figure from Wikipedia, using a LangChain tool covered in the lab Empower ADK agents with tools. An agent can choose to call its tool(s) multiple times in succession, so the researcher can take multiple turns in a row if it determines it needs to do more research.

b. A `screenwriter` to turn the research into a plot outline.

c. A `file_writer`  to title the resulting movie and write the results of the sequence to a file.

1. In the Cloud Shell Editor, navigate to the directory `adk_multiagent_systems/workflow_agents`.

2. Click on the `agent.py` file in the `workflow_agents` directory.

3. Read through this agent definition file. Because sub-agents must be defined before they can be assigned to a parent, to read the file in the order of the conversational flow, you can read the agents from the bottom of the file to the top.

4. You also have a function tool `append_to_state`. This function allows agents with the tool the ability to add content to a dictionary value in state. It is particularly useful for agents that might call a tool multiple times or act in multiple passes of a LoopAgent, so that each time they act their output is stored.

5. Try out the current version of the agent by launching the web interface from the Cloud Shell Terminal. You will use the --reload_agents argument to enable live reloading of agents based on agent changes:

```bash
cd ~/adk_multiagent_systems
adk web --reload_agents
```

```text
Note: If you did not shut down your previous adk web session, the default port of 8000 will be blocked, but you can launch the Dev UI with a new port by using adk web --port 8001, for example.
```

6. To view the web interface in a new tab, click the http://127.0.0.1:8000 link in the Terminal output.

7. A new browser tab will open with the ADK Dev UI.

8. From the Select an agent dropdown on the left, select workflow_agents.

9. Start the conversation with: hello. It may take a few moments for the agent to respond, but it should request you enter a historical figure to start your film plot generation.

10. When prompted to enter a historical figure, you can enter one of your choice or use one of these examples:

```text
Zhang Zhongjing - a renowned Chinese physician from the 2nd Century CE.
```

```text
Ada Lovelace - an English mathematician and writer known for her work on early computers
```

```text
Marcus Aurelius - a Roman emperor known for his philosophical writings.
```

11. The agent should now call its agents one after the other as it executes the workflow and writes the plot outline file to your `~/adk_multiagent_systems/movie_pitches` directory. It should inform you when it has written the file to disk.


If you don't see the agent reporting that it generated a file for you or want to try another character, you can click + New Session in the upper right and try again.

12. View the agent's output in the Cloud Shell Editor. (You may need to use the Cloud Shell Editor's menu to enable View > Word Wrap to see the full text without lots of horizontal scrolling.)

13. In the ADK Dev UI, click on one of the agent icons (agent_icon) representing a turn of conversation to bring up the event view.

14. The event view provides a visual representation of the tree of agents and tools used in this session. You may need to scroll in the event panel to see the full plot.

<img width="1114" height="362" alt="image" src="https://github.com/user-attachments/assets/cf4714f2-c557-4fc5-989a-cb9f9cd3de4c" />


15. In addition to the graph view, you can click on the Request tab of the event to see the information this agent received as part of its request, including the conversation history.

16. You can also click on the Response tab of the event to see what the agent returned.

> Note: While this system can produce interesting results, it is not intended to imply that instructions can be so brief or adding examples can be skipped. The system's reliability would benefit greatly from the additional layer of adding more rigorous instructions and examples for each agent.

<hr>

# Task 5. Add a LoopAgent for iterative work

The `LoopAgent` executes its sub-agents in a defined sequence and then starts at the beginning of the sequence again without breaking for a user input. It repeats the loop until a number of iterations has been reached or a call to exit the loop has been made by one of its sub-agents (usually by calling a built-in exit_loop tool).

This is beneficial for tasks that require continuous refinement, monitoring, or cyclical workflows. Examples include:

* __Iterative Refinement:__ Continuously improve a document or plan through repeated agent cycles.

* __Continuous Monitoring:__ Periodically check data sources or conditions using a sequence of agents.

* __Debate or Negotiation:__ Simulate iterative discussions between agents to reach a better outcome.

You will add a LoopAgent to your movie pitch agent to allow multiple rounds of research and iteration while crafting the story. In addition to refining the script, this allows a user to start with a less specific input: instead of suggesting a specific historical figure, they might only know they want a story about an ancient doctor, and a research-and-writing iteration loop will allow the agents to find a good candidate, then work on the story.