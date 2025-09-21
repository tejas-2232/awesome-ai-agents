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
