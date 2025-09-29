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
