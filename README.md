# awesome-ai-agents

### Agent Development Kit

* Agent Development Kit (ADK) is a flexible and modular framework for developing and deploying AI agents. While optimized for Gemini and the Google ecosystem, ADK is model-agnostic, deployment-agnostic, and is built for compatibility with other frameworks.
* ADK was designed to make agent development feel more like software development, to make it easier for developers to create, deploy, and orchestrate agentic architectures that range from simple tasks to complex workflows.

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/6356bee7-13e9-4e40-a0d0-ac3fc6e28789" />


## Build a multi-tool agent

* This quickstart guides you through installing the Agent Development Kit (ADK), setting up a basic agent with multiple tools, and running it locally either in the terminal or in the interactive, browser-based dev UI.

* This quickstart assumes a local IDE (VS Code, PyCharm, IntelliJ IDEA, etc.) with Python 3.9+ or Java 17+ and terminal access. This method runs the application entirely on your machine and is recommended for internal development.

1. Set up a Google Cloud project

* Set up your Google Cloud project and enable the Vertex AI API.
a. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.<br>
b. Select a project: Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. <br>
c. Create a project: To create a project, you need the Project Creator (roles/resourcemanager.projectCreator), which contains the resourcemanager.projects.create permission.

2. Verify that billing is enabled for your Google Cloud project.
3. Enable the Vertex AI API.(roles required to enable APIs =  Service Usage Admin IAM role (roles/serviceusage.serviceUsageAdmin), which contains the serviceusage.services.enable permission.) 

4. Setup credentials

On your local terminal, set up and authenticate with the Google Cloud CLI. If you are familiar with the Gemini API in Google AI Studio, note that the Gemini API in Vertex AI uses Identity and Access Management instead of API keys to manage access.

1. Install and initialize the Google Cloud CLI.
2. If you previously installed the gcloud CLI, ensure your gcloud components are updated by running this command.

```bash
gcloud components update
```

3. Run the following command to generate a local Application Default Credentials (ADC) file. Your agent will use these credentials to access Vertex AI during local application development.

```bash
gcloud auth application-default login
``` 

__Set up Environment & Install ADK__

__Python__

_Create & Activate Virtual Environment (Recommended):_

```python
# Create
python -m venv .venv
# Activate (each new terminal)
# macOS/Linux: source .venv/bin/activate
# Windows CMD: .venv\Scripts\activate.bat
# Windows PowerShell: .venv\Scripts\Activate.ps1
```

_Install ADK:_

```bash
pip install google-adk
```
### create an agent

__Using the terminal, create the folder structure:__

```bash
mkdir multi_tool_agent
touch \
multi_tool_agent/__init__.py \
multi_tool_agent/agent.py \
multi_tool_agent/.env
```

Your structure:
```
parent_folder/
    multi_tool_agent/
        __init__.py
        agent.py
        .env
```

__Copy and paste the following code into the following three files you created:__

* (____init____.py)

```python
from . import agent
```

* .env

```.env
# If using Gemini via Vertex AI on Google Cloud
GOOGLE_CLOUD_PROJECT="your-project-id"
GOOGLE_CLOUD_LOCATION="your-location" #e.g. us-central1
GOOGLE_GENAI_USE_VERTEXAI="True"
```

<hr>
<hr>

# Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

Feel free to contribute by:

* Adding new agent types
* Improving existing implementations
* Adding more examples and use cases
* Enhancing documentation

<hr>
<hr>
