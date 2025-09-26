# Setup and requirements

## Task 1. Install ADK and set up your environment

```
Note: Using an Incognito browser window is recommended for most Qwiklabs to avoid confusion between your Qwiklabs student account and other accounts logged into Google Cloud. If you are using Chrome, the easiest way to accomplish this is to close any Incognito windows, then right click on the Open Google Cloud console button at the top of this lab and select Open link in Incognito window.
```

## Enable Vertex AI recommended APIs
* In this lab environment, the Vertex AI API and Cloud Run API have been enabled for you. If you were to follow these steps in your own project, you could enable it by navigating to Vertex AI and following the prompt to enable it.

## Download and install the ADK and code samples for this lab

* Install ADK by running the following command in the Cloud Shell Terminal. Note: You will specify the version to ensure that the version of ADK that you install corresponds to the version used in this lab:

```bash
# Install ADK and the A2A Python SDK
cd ~
export PATH=$PATH:"/home/${USER}/.local/bin"
python3 -m pip install google-adk==1.8.0 a2a-sdk==0.2.16
# Correcting a typo in this version
sed -i 's/{a2a_option}"/{a2a_option} "/' ~/.local/lib/python3.12/site-packages/google/adk/cli/cli_deploy.py
```

* Paste the following commands into the Cloud Shell Terminal to copy lab code from a Cloud Storage bucket and unzip it:

```bash
gcloud storage cp gs://YOUR_GCP_PROJECT_ID-bucket/adk_and_a2a.zip ./adk_and_a2a.zip
```

```bash
unzip adk_and_a2a.zip
```

##Task 2. Explore the ADK agent you will make available remotely

* For the purposes of this lab, imagine you work for a stadium maintenance company: Cymbal Stadiums. As part of a recent project, you developed an image generation-agent that can create illustrations according to your brand guidelines. Now, several different teams in your organization want to use it too.

* If you were to copy the code for use as a sub-agent by many agents, it would be very difficult to maintain and improve all of these copies.

* Instead, you can deploy the agent once as an agent wrapped with an A2A server, and the other teams' agents can incorporate it by querying it remotely.

1. In the Cloud Shell Editor's file explorer pane, navigate to the adk_and_a2a/illustration_agent directory. This directory contains the ADK agent you will make available remotely. Click the directory to toggle it open.

2. Open the agent.py file on this directory and scroll to the section labeled # Tools.

3. Notice the generate_image() function, which will be used as a tool by this agent. It receives a prompt as an argument, then uses the Google Gen AI SDK to generate_images(). This call includes an output_gcs_uri argument to store the generated image directly in Cloud Storage. The tool then returns the URL of the stored image.

4. Notice that the instruction provided to the root_agent provides specific instructions to the agent to use image-generation prompts that respect the company's brand guidelines. For example, it specifies:

* a specific illustration style: (Corporate Memphis)
* a color palette (purples and greens on sunset gradients)
* examples of stadium/sports and maintenance imagery because it is a stadium maintenance company

5. To see it in action, you'll first need to write a .env file to set environment variables needed by ADK agents. Run the following in the Cloud Shell Terminal to write this file in this directory.

```bash
cd ~/adk_and_a2a
cat << EOF > illustration_agent/.env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=YOUR_GCP_PROJECT_ID
GOOGLE_CLOUD_LOCATION=GCP_LOCATION
MODEL="gemini-2.0-flash-001"
IMAGE_MODEL="imagen-3.0-generate-002"
EOF
```

6. Run the following to copy the .env to another agent directory you'll use in this lab:

```bash
cp illustration_agent/.env slide_content_agent/.env
```

7. Now from the Cloud Shell Terminal, launch the ADK dev UI with:

```bash
adk web
```

* Output

```output
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

8.To view the web interface in a new tab, click the http://127.0.0.1:8000 link at the bottom of the Terminal output.

9. A new browser tab will open with the ADK Dev UI.

10. From the Select an agent dropdown on the left, select the illustration_agent from the dropdown.

11.Query the agent with some text that could be used in a recruitment slide deck:

```text
By supporting each other, we get big things done!
```

12. After about 10 seconds, the agent should respond with the prompt it generated and a URL to preview the image. Click the image URL to preview the image, then click Back in your browser to return to the Dev UI.
