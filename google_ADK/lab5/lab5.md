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

1. A bundle of artifacts is generated locally, comprising:

* *.pkl: a pickle file corresponding to local_agent.
* requirements.txt: this file from the agent folder defining [package requirements.](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/deploy#package-requirements)
* dependencies.tar.gz: a tar file containing any [extra packages.](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/deploy#extra-packages)

2. The bundle is uploaded to Cloud Storage (using a defined [directory](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/deploy#gcs-directory) if specified) for staging the artifacts.

3. The Cloud Storage URIs for the respective artifacts are specified in the [PackageSpec.](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.reasoningEngines#PackageSpec)

4. The Vertex AI Agent Engine service receives the request and builds containers and spins up HTTP servers on the backend.

__Note:__ Deployment should take about 10 minutes, but you can continue with this lab while it deploys.

### Quiz While Your Agent is Deploying

Each of the `adk deploy ...` commands requires certain arguments to be set. For the most up-to-date arguments, click the linked commands in the list at the top of this task and look for the arguments marked as "Required".

Some required arguments, like `--project` and `--region` from the `adk deploy agent_engine` deployment can load their values from the agent's .env file if present.

Answer the following questions based on the arguments for `adk deploy agent_engine`:

1. The `--agent_engine_id` argument allows you to update an existing Agent Engine instance.
* True
* False

2. The `--trace_to_cloud` argument has a default value of True.
* True
False

3. Which of the following is true about the `--adk_app` argument?
a. Defaults to use your agent.py file.
b. Accepts a filename to define an ADK app.
c. Is required.
d. Creates app files for you to edit.

__Highlights from Expected Output:__

```output
Copying agent source code...
Copying agent source code complete.
Initializing Vertex AI...
[...]
Creating AgentEngine
Create AgentEngine backing LRO: projects/430282503153/locations/us-central1/reasoningEngines/2902138951282196480/operations/2777364189918789632
View progress and logs at https://console.cloud.google.com/logs/query?project=qwiklabs-gcp-04-f71a2270bd79
AgentEngine created. Resource name: projects/430282503153/locations/us-central1/reasoningEngines/2902138951282196480
To use this AgentEngine in another session:
agent_engine = vertexai.agent_engines.get('projects/430282503153/locations/us-central1/reasoningEngines/2902138951282196480')
Cleaning up the temp folder: /tmp/agent_engine_deploy_src/20250813_175223

```
<hr>

# Task 3. Get and query an agent deployed to Agent Engine

To query the agent, you must first grant it the authorization to call models via Vertex AI.

1. To see the service agent and its assigned role, navigate to IAM in the console.

2. Click the checkbox to `Include Google-provided role grants` .

3. Find the `AI Platform Reasoning Engine Service Agent` (service-PROJECT_NUMBER@gcp-sa-aiplatform-re.iam.gserviceaccount.com), and click the edit pencil icon in this service agent's row.

4. Click `+ Add another role`.

5. In the `Select a role` field, enter `Vertex AI User`. If you deploy an agent that uses tools to access other data, you would grant access to those systems to this service agent as well.

6. Save your changes.

7. Back in the Cloud Shell Editor, within the `adk_to_agent_engine` directory, open the file `query_agent_engine.py`.

8. Review the code and comments to notice what it is doing.

9. Review the transcript passed to the agent, so that you can evaluate if it's generating an adequate summary.

10. In the Cloud Shell Terminal, run the file from the adk_to_agent_engine directory with:

```bash
cd ~/adk_to_agent_engine/transcript_summarization_agent
python3 query_agent_engine.py
```

__Example output (yours results may be a little different):__

```output
[remote response] The user wants to buy a boat, and after being asked about the size, inquires how much boat $50,000 will purchase. The Virtual Agent responds that $50,000 will get a "very nice boat," to which the user agrees to proceed.
```

<hr>

# Task 4. View and delete agents deployed to Agent Engine

1. When your agent has completed its deployment, return to a browser tab showing the Cloud Console and navigate to Agent Engine by searching for it and selecting it at the top of the Console.

2. In the Region dropdown, make sure your location for this lab (`GCP_LOCATION`) is selected.

3. You will see your deployed agent's display name. Click on it to enter its monitoring dashboard.

4. Notice both the Metrics and Session tabs that will each give you insights into how your agent is being used.

5. When you are ready to delete your agent, select Deployment details from the top of its monitoring dashboard.

6. Back in your browser tab running the Cloud Shell Terminal, paste the following command, but don't run it yet:

```bash
cd ~/adk_to_agent_engine
python3 agent_engine_utils.py delete REPLACE_WITH_AE_ID
```

7. From the Agent Engine Deployment info panel, copy the Name field, which will have a format like: `projects/qwiklabs-gcp-02-76ce2eed15a5/locations/us-central1/reasoningEngines/1467742469964693504.`

8. Return to the Cloud Shell Terminal and replace the end of the command REPLACE_WITH_AE_ID with the resource name you've copied.

9. Press Return to run the deletion command.

__Example Output:__

```output
Deleting AgentEngine resource: projects/1029886909158/locations/us-central1/reasoningEngines/1456078850617245696
Delete AgentEngine backing LRO: projects/1029886909158/locations/us-central1/operations/2884525977596067840
AgentEngine resource deleted: projects/1029886909158/locations/us-central1/reasoningEngines/1456078850617245696
```
10. In the Cloud Console, return to the Agent Engine dashboard to see that the agent has been deleted.

11. To view the simple Python SDK code to list and delete agents, view the contents of the file adk_to_agent_engine/agent_engine_utils.py.


# Congratulations!
In this lab, you've learned:

* The benefits of deploying agents to Agent Engine
* How to grant required roles to the Reasoning Engine Service Agent
* How to deploy an agent to Agent Engine using the ADK command line interface
* How to query an agent deployed to Agent Engine
* How to monitor your deployed agents
* How to delete agents