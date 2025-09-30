# Task 1. Install ADK and set up your environment

## Enable Vertex AI recommended APIs

In this lab environment, the Vertex AI API has been enabled for you. If you were to follow these steps in your own project, you could enable it by navigating to Vertex AI and following the prompt to enable it.

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
python3 -m pip install google-adk
```

3. Install additional lab requirements with:

```bash
python3 -m pip install -r adk_to_agent_engine/requirements.txt
```

4. Run the following commands to create a .env file in the adk_to_agent_engine directory. (Note: To view a hidden file beginning with a period, you can use the Cloud Shell Editor menus to enable View > Toggle Hidden Files):

```bash
cd ~/adk_to_agent_engine
cat << EOF > .env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=YOUR_GCP_PROJECT_ID
GOOGLE_CLOUD_LOCATION=GCP_LOCATION
MODEL=gemini-2.5-flash
EOF
```

5. Copy the .env file to the agent directory to provide your agent necessary authentication configurations once it is deployed:

```bash
cp .env transcript_summarization_agent/.env
```

<hr>


# Task 2. Deploy to Agent Engine using the command line deploy method

ADK's command line interface provides shortcuts to deploy agents to Agent Engine, Cloud Run, and Google Kubernetes Engine (GKE). You can use the following base commands to deploy to each of these services:

* __adk deploy agent_engine__ (with its command line args described under the @deploy.command("agent_engine") decorator)
* __adk deploy cloud_run__ (with its command line args described under the @deploy.command("cloud_run") decorator)
* __adk deploy gke__ (with its command line args described under the @deploy.command("gke") decorator)

`The adk deploy agent_engine` command wraps your agent in a reasoning_engines.AdkApp class and deploys this app to Agent Engine's managed runtime, ready to receive agentic queries.

When an `AdkApp` is deployed to Agent Engine, it automatically uses a [VertexAiSessionService](https://google.github.io/adk-docs/sessions/session/#sessionservice-implementations) for persistent, managed session state. This provides multi-turn conversational memory without any additional configuration. For local testing, the application defaults to a temporary, InMemorySessionService.

To deploy an Agent Engine app using __adk deploy agent_engine,__ complete the following steps:

1. In the __adk_to_agent_engine/transcript_summarization_agent__ directory, click on the _agent.py_ file to review the instructions of this simple summarization agent.

2. To deploy an agent, you must provide its requirements. In Cloud Shell Editor, right-click on the __transcript_summarization_agent__ directory. (You may need to click Allow to enable the right-click menu.)

3. Select New File...

4. Name the file like a standard Python requirements file: requirements.txt

5. Paste the following into the file:

```bash
google-cloud-aiplatform[adk,agent_engines]==1.110.0
```

6. Save the file.

7. In the Cloud Shell Terminal, run the deploy command:

```bash
adk deploy agent_engine transcript_summarization_agent \
--display_name "Transcript Summarizer" \
--staging_bucket gs://YOUR_GCP_PROJECT_ID-bucket
```
You can follow the status from the log file that will be linked from the command's output. During deployment, the following steps are occurring: