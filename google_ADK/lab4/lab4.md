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
