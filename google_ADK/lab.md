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
