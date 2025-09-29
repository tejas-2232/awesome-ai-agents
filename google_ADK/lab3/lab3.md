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