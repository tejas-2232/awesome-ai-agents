# Activate Cloud Shell

## List the active account name:

```bash
gcloud auth list
```
```
(Output)

Credentialed accounts:
 - <myaccount>@<mydomain>.com (active)
 ```
 ```
(Example output)

Credentialed accounts:
 - google1623327_student@qwiklabs.net
 ```
 ```

List the project ID:

```bash
gcloud config list project
```


(Output)
```
[core]
project = <project_ID>
```

(Example output)
```
[core]
project = qwiklabs-gcp-44776a13dea667a6
```

<hr>


# Task 1. Configure your environment and account

1. Sign in to the Google Cloud console with your lab credentials, and open the Cloud Shell terminal window.

2. To set your project ID and region environment variables, in Cloud Shell, run the following commands:

```bash
PROJECT_ID=$(gcloud config get-value project)
REGION=us-west1
echo "PROJECT_ID=${PROJECT_ID}"
echo "REGION=${REGION}"
```

3. To store the signed-in Google user account in an environment variable, run the following command:

```bash
USER=$(gcloud config get-value account 2> /dev/null)

echo "USER=${USER}"
```

4. Enable the Cloud AI Companion API for Gemini:

```bash
gcloud services enable cloudaicompanion.googleapis.com --project ${PROJECT_ID}
```

5. To use Gemini, grant the necessary IAM roles to your Google Cloud Qwiklabs user account:

```bash
gcloud projects add-iam-policy-binding ${PROJECT_ID} --member user:${USER} --role=roles/cloudaicompanion.user
```

```bash
gcloud projects add-iam-policy-binding ${PROJECT_ID} --member user:${USER} --role=roles/serviceusage.serviceUsageViewer
```
Adding these roles lets the user use Gemini assistance.

<hr>


# Task 2. Create a Cloud Workstation

This lab uses Gemini assistance to develop an app with the Cloud Code plugin for Cloud Workstations IDE. Cloud Workstations is a fully managed integrated development environment that includes native integration with Gemini.

In this task, you configure and provision your Cloud Workstation environment, and you enable the Cloud Code plugin for Gemini.

## View the workstation cluster

A workstation cluster named my-cluster has been pre-created for this lab. This cluster is used to configure and create a workstation.

1. On the Google Cloud console title bar, type Cloud Workstations in the Search field, then click Cloud Workstations in the search results.

2. In the Navigation pane, click Cluster management.

3. Check the Status of the cluster. If the status of the cluster is Reconciling or Updating, periodically refresh and wait until it becomes Ready before moving to the next step.

## Create a workstation configuration

Before creating a workstation, you must create a workstation configuration in Cloud Workstations.

1. In the Navigation pane, click Workstation configurations, and then click Create Workstation Configuration.

2. Specify the following values:

<img width="683" height="179" alt="image" src="https://github.com/user-attachments/assets/c3264e35-88a3-4764-920a-044c851b6cae" />

3. In the left pane, select Environment settings.

4. In Storage settings > Persistent disk settings, specify the following values:

<img width="647" height="155" alt="image" src="https://github.com/user-attachments/assets/87b68397-0221-4dca-862b-e2b5fe5a7ee6" />

5. Click Create.

6. Click Refresh.

7. Check the Status of the configuration being created. If the status of the configuration is Reconciling or Updating, periodically refresh and wait until the status becomes Ready before moving to the next step.

## Create a workstation
1. In the Navigation pane, click Workstations, and then click Create Workstation.

2. Specify the following values:

<img width="657" height="201" alt="image" src="https://github.com/user-attachments/assets/e24ef94a-ce02-4e54-8c48-9e70e6a0f553" />


3. Click Create.

After the workstation is created, it is listed under My workstations with a status of Stopped.

4. To start the workstation, click Start.

As the workstation starts up, the status changes to Starting. Wait for the status to change to Running which indicates that it is ready to be used. It might take several minutes for the workstation to fully start up.

## Launch the IDE
To function properly, some extensions need third-party cookies to be enabled in your browser.

1. To enable third-party cookies in Chrome, in the Chrome menu, click Settings.

2. In the search bar, type Third-party cookies.

3. Click the Third-party cookies setting, and select Allow third-party cookies.

> Note: If you want to restore your browser to its current settings after the lab, note the original setting for third-party cookies.

* To launch the Code OSS IDE on the workstation, from the Workstations page in the Google Cloud console, click Launch.

The IDE opens in a separate browser tab.

<img width="1493" height="1119" alt="image" src="https://github.com/user-attachments/assets/01b1658c-8253-47d3-bdf6-b2901f4b421c" />

<hr>

# Task 3. Update the Cloud Code extension to enable Gemini
In this task, you enable Gemini in Cloud Code for your Workstation IDE.

Connect to Google Cloud
To connect to Google Cloud in your workstation, perform these steps:

1. At the bottom of the window, on the status bar, click Cloud Code - Sign In.

<img width="754" height="408" alt="image" src="https://github.com/user-attachments/assets/1816ba90-547c-44d8-81d8-d417e286ed6f" />

2. To launch the Cloud Cloud sign-in flow, press Control (for Windows and Linux) or Command (for MacOS) and click the link in the terminal.
3. If you are asked to confirm the opening of the external website, click Open.
4. Click the student email address.
5. When you're prompted to confirm that you downloaded this app from Google, click Sign in.

Your verification code is displayed in the browser tab.
> Note: You may see a warning that you ran a gcloud auth login command. This process is normal. The IDE ran this command on your behalf.

6. Click Copy.
7. Back in the IDE, in the terminal, where it says Enter authorization code, paste the code.
8. If asked to approve copying from the clipboard, click Allow.
9. Click Enter, and then wait for the status bar to show Cloud Code - No Project.

You're now connected to Google Cloud.

## Enable Gemini in Cloud Code
To enable Gemini in Cloud Code for your workstation IDE, perform these steps:

1. In your workstation IDE, click on the Manage icon (Code OSS main menu) in the bottom left corner, then click Settings.
2. On the User tab of the Settings dialog, select Extensions > Gemini Code Assist.
3. In Search settings, enter Gemini.
4. On the Qwiklabs lab credentials panel, to copy the Project ID, click Copy.

5. On the Cloud Code settings page, for Geminicodeassist: Project, paste the Google Cloud project ID.
6. Confirm that Geminicodeassist: Enable is enabled.
7. In the IDE status bar, click Cloud Code - No Project.
8. Click Select a Google Cloud Project, and then click your project ID.
9. The project ID is now shown in the status bar. Gemini is now ready to use

# Task 4. Chat with Gemini
Gemini can help you choose the Google Cloud services that meet the requirements of your application architecture. If you want to develop and test your app in your local IDE, and then deploy it to Google Cloud, you can chat with Gemini to get help.

In this task, you use the Gemini Code Assist pane to enter prompts and view the responses from Gemini.

Prompts are questions or statements that describe the help that you need. Prompts can include context from existing code that Google Cloud analyzes to provide more useful or complete responses. For more information on writing prompts to generate good responses, see Write better prompts for Gemini in Google Cloud.

## Prompt Gemini

To prompt Gemini about Google Cloud services, perform these steps:

1. To open the Gemini chat pane, in the IDE activity bar, click Gemini Code Assist (Code OSS Gemini menu).

> Note: You may see a warning that you are missing a valid license. You may ignore this message for this lab.

2. If an error occurs when trying to open the Gemini chat pane, refresh the browser window.

3. In the Gemini Code Assist pane, type the following prompt, and then click Send (Gemini send):
``` text
I am new to Google Cloud and I want to use the Cloud Code extension. Give me some examples of Google services that I can use to build and deploy a sample app.
```

Gemini responds with a list of Google Cloud services and descriptions.

In this example, assume that Gemini suggests both Cloud Run and Cloud Functions as two Google Cloud services that can help you build and deploy a sample app. You can ask for more information about those services.

4. To provide a follow-up question or prompt, in the Gemini Code Assist pane, type the text below, and then click Send (Gemini send):

```text
What is the difference between Cloud Run and Cloud Functions?
```
Gemini responds with key differences between the two Google Cloud services.

<hr>

# Task 5. Develop a Python app
Let's now use Cloud Run to create and deploy a basic Python app. Because you're new to Cloud Run and Cloud Code, you need help with the steps for creating the app.

In this task, you prompt Gemini for help to build a Hello World Python app in Cloud Run.

## Get help from Gemini

1. In the Gemini Code Assist pane, to learn how to create a Cloud Run app with Cloud Code, type the following prompt, and then click Send (Gemini send):

```
How do I create a new Cloud Run app in Cloud Code using the command palette? What languages are supported?
```

2. In the response from Gemini, view the set of steps to create an app. Gemini also displays the supported languages for the Cloud Run app.

> Note: The command palette in VS Code provides a list of all the commands, including the commands for Cloud Code.


## Create a Python app by using the steps from Gemini

1. Click the menu (Code OSS main menu), and then navigate to View > Command Palette.
2. Type Cloud Code New, and then select Cloud Code: New Application.

<img width="1200" height="362" alt="image" src="https://github.com/user-attachments/assets/3d988c57-5af4-4e0f-9280-2f104be33b8a" />

3. Select Cloud Run application.
4. Select Python (Flask): Cloud Run.
5. Update the name of the app and top-level folder to /home/user/hello-world, and then click Ok.

Cloud Code downloads the template and creates the application files in the folder in your IDE.

## Explore the app with Gemini
Now that you've created your Hello World app in Cloud Run, you can use Gemini to explain the files and code snippets that are deployed in your IDE.

1. If the files are not visible, in the IDE activity bar, click Explorer (Code OSS Explorer menu).

2. In the Explorer pane, select Dockerfile.
3. Select the entire contents of the Dockerfile, click the bulb (Code OSS Gemini bulb), and from the More Actions menu, click Gemini: Explain this.
4. In the Gemini Code Assist pane, click Send (Gemini send).

Gemini generates a natural-language explanation about the contents and function of the Dockerfile. You can also select portions of the file contents, click the bulb (Code OSS Gemini bulb), and then click Gemini: Explain this.

5. Select the line that begins with ENTRYPOINT, click the bulb (Code OSS Gemini bulb), and then click Gemini: Explain this.
6. In the Gemini Code Assist pane, click Send (Gemini send).

Gemini responds with details about the ENTRYPOINT instruction. You learn that, with this instruction, Docker will run the app.py file when the container launches.

7. To view the contents of the app.py file, in the activity bar, click Explorer (Code OSS Explorer menu), and then click app.py.
8. In the hello() function definition, select the lines that contain the K_SERVICE, and K_REVISION environment variables. Click the bulb (Code OSS Gemini bulb), then click Gemini: Explain this.
9. In the Gemini Code Assist pane, click Send (Gemini send).

Gemini responds with a detailed explanation of these two Cloud Run environment variables and how they are used in the application code.

## Run the app locally

You can run your app locally from your IDE by using the Cloud Run emulator. In this case, locally means on the workstation machine.

1. In the activity bar of your IDE, click Cloud Code (Code OSS Cloud Code menu), and then click Cloud Run.
<img width="196" height="145" alt="image" src="https://github.com/user-attachments/assets/84c9d65c-d7b5-4953-b8a2-1d826dd1dfa9" />

> Note: You will first run the app using the Cloud Run Emulator, so you won't need to enable the Cloud Run API yet.

2. In the Cloud Run activity bar, click Run App on Local Cloud Run Emulator (Cloud Run - run on local emulator), and then click Run.

The Output tab in the IDE displays the progress of the build.

3. When prompted at the top of the screen to Enable minikube gcp-auth addon to access Google APIs, select Yes.

<img width="650" height="109" alt="image" src="https://github.com/user-attachments/assets/4c1ccd8a-0984-4466-8d3a-b51a4e5b0e38" />

When you're prompted to sign in, click Proceed to sign in.

A link is displayed in the terminal.

1. To launch the Cloud Cloud sign-in flow, press Control (for Windows and Linux) or Command (for MacOS) and click the link in the terminal.
2. If you are asked to confirm the opening of the external website, click Open.
3. Click the student email address.
4. When you're prompted to continue, click Continue.
5. To let the Google Cloud SDK access your Google Account and agree to the terms, click Allow.
Your verification code is displayed in the browser tab.

6. Click Copy.
7. Back in the IDE, in the terminal, where it says Enter authorization code, paste the code and click Enter.

Wait for the build and deploy to complete.

8. Hold the pointer over the link to the hello-world service at the localhost URL, and click Follow link.

<img width="650" height="334" alt="image" src="https://github.com/user-attachments/assets/7cd4344c-62c4-4f05-8154-1a6fea8bcd94" />

A new tab is opened in the browser that displays a page indicating that the service is running

<hr>

# Task 6. Enhance the Python app
Let's now add data and functionality to the app so that it can be used for management of inventory data.

In this task, you first add inventory data for the app.

> Note: Generative AI does not create the same output every time. If you observe a significant difference in the code generated by Gemini, you can instead use the code snippet provided in the lab.

## Generate sample data using Gemini

1. In the activity bar of your IDE, click Explorer (Code OSS Explorer menu).

Click New file (Explorer - new file), and create a file named inventory.py.

3. To let Gemini generate the sample data, open the Gemini Code Assist pane, type the following prompt, and then click Send:

```
Create a variable called inventory which is a list of 3 JSON objects. Each JSON object has 2 attributes: productid and onhandqty. Both attributes are strings.
```

Gemini generates the inventory JSON array that contains 3 JSON objects.

4. To insert the sample JSON data in the inventory.py file, in the Gemini response, click Insert in current file (Gemini - insert in current file). The contents of the file is similar to:

```python
inventory = [
    {"productid": "12345", "onhandqty": "100"},
    {"productid": "67890", "onhandqty": "50"},
    {"productid": "11122", "onhandqty": "25"}
]
```

To save the inventory.py file in the home/user/hello-world folder, in the IDE menu (Code OSS main menu), click File > Save.

You use this sample inventory data in the next subtask.

## Add the GET /inventory list API method to the app

You now introduce API methods in the app.py file that can operate on the inventory data. To complete this subtask, you use the code generation feature in Gemini.

1. In Explorer, open the file app.py.

2. Modify the flask import statement to include the inventory file and the jsonify library:

```python
from flask import Flask, render_template, jsonify
from inventory import inventory
```

3. In the app.py file, position your cursor below the app assignment statement:

```
app = Flask(__name__)
```

4. To let Gemini Code Assist generate the code for the first API method, in the app.py file, enter the following comment:

```python
# Generate an app route to display a list of inventory items in the JSON format from the inventory.py file.
# Use the GET method.
```

5. Select the comment lines, including the blank line below the comment.

6. Click the bulb (Code OSS Gemini bulb), and then select Gemini: Generate code.

Gemini generates a function for the GET operation that returns a list of items from the inventory.py file. The function generally looks similar to this:

```python
@app.route('/inventory', methods=['GET'])
def inventory_list():
    """Return a list of inventory items in JSON format."""
    return jsonify(inventory)
```

> Note: To learn more about the jsonify(inventory) function, highlight the term and prompt Gemini to explain the code to you.

7. To accept the generated code, hold the pointer over any part of the generated code response, then click Accept.

> Important: Gemini can generate more than one code snippet, and these snippets might differ from the snippet that is displayed above.

8. If the app.route and return statements in your generated code is different from the code shown above, replace the generated code snippet with the snippet displayed above. This should ensure that the lab works as intended.

## Add the GET /inventory/{productID} method to the app

Let's add another API method to return data about a specific inventory item, given its product ID. If the product ID is not found, the API returns the standard HTTP status code of 404.

1. Add a few blank lines following the /inventory route.

2. To let Gemini generate the code for this second API method, in the app.py file, enter the following comment:

```python
# Generate an App route to get a product from the list of inventory items given the productID.
# Use the GET method.
# If there is an invalid productID, return a 404 error with an error message in the JSON.
```

3. Select the 3 comment lines and the blank line that follows the comment, click the bulb (Code OSS Gemini bulb), and then select Gemini: Generate code.

Gemini generates a function for the GET operation that returns the item from the inventory file whose productID is provided in the request, or the 404 status code if the product does not exist.

```python
@app.route('/inventory/<productid>', methods=['GET'])
def inventory_item(productid):
    """Return a single inventory item in JSON format."""
    for item in inventory:
        if item['productid'] == productid:
            return jsonify(item)
    return jsonify({'error': 'Product not found'}), 404
```

4. Hold the pointer over any part of the generated code response. To accept the generated code, in the toolbar, click Accept.

5. If the generated code is different from the code shown above, replace the generated code snippet with the snippet displayed above.

Your app.py file should now look similar to this:

```python
 """
 A sample Hello World server.
 """
 import os

 from flask import Flask, render_template, jsonify
 from inventory import inventory

 # pylint: disable=C0103
 app = Flask(__name__)
 # Generate an app route to display a list of inventory items in the JSON format from the inventory.py file.
 # Use the GET method.
 @app.route('/inventory', methods=['GET'])
 def inventory_list():
     """Return a list of inventory items in JSON format."""
     return jsonify(inventory)


 # Generate an App route to get a product from the list of inventory items given the productID.
 # Use the GET method.
 # If there is an invalid productID, return a 404 error with an error message in the JSON.
 @app.route('/inventory/<productid>', methods=['GET'])
 def inventory_item(productid):
     """Return a single inventory item in JSON format."""
     for item in inventory:
         if item['productid'] == productid:
             return jsonify(item)
     return jsonify({'error': 'Product not found'}), 404

     @app.route('/')
     def hello():
     """Return a friendly HTTP greeting."""
     message = "It's running!"

     """Get Cloud Run environment variables."""
     service = os.environ.get('K_SERVICE', 'Unknown service')
     revision = os.environ.get('K_REVISION', 'Unknown revision')

     return render_template('index.html',
         message=message,
         Service=service,
         Revision=revision)

 if __name__ == '__main__':
     server_port = os.environ.get('PORT', '8080')
     app.run(debug=False, port=server_port, host='0.0.0.0')
 </productid>
```

## Rebuild and redeploy the app locally
You can run your app locally from your IDE using the Cloud Run emulator. In this case, locally means on the workstation machine.

1. In the activity bar of your IDE, click Cloud Code (Code OSS Cloud Code menu).

2. In the Cloud Run activity bar, click Run App on Local Cloud Run Emulator (Cloud Run - run on local emulator).

3. When prompted at the top of the screen to Enable minikube gcp-auth addon to access Google APIs, select Yes.

Wait for the build and deploy to complete.

4. Hold the pointer over the link to the hello-world service at the localhost URL, and click Follow link.

A new tab is opened in the browser that displays a page indicating that the service is running.

## Test the API methods

1. Follow the steps in the earlier task to run the app locally.

2. After following the localhost URL link to view the running app in a separate browser tab, add /inventory to the end of the URL in the same tab and press Enter.

The API returns a JSON response that contains the list of products from the inventory.py file. The JSON response should resemble this:

```json
[{"onhandqty":"100","productid":"12345"},{"onhandqty":"50","productid":"67890"},{"onhandqty":"25","productid":"11122"}]
```
3. Append /{productID} to the URL that ends with /inventory, where {productID} is a product ID in your inventory.

For the example above, the end of a valid URL would be /inventory/12345.

4. Note this product ID, as it will be used in later steps.

5. Type Enter.

The API returns a JSON response that contains data about the specific product.

> Note: If the product was not returned successfully, replace the product ID route with the example code from the lab, and rebuild the app.

6. In the URL, replace the product ID with XXXXX and type Enter.

7. The URL should now end with /inventory/XXXXX.

8. XXXXX is not a valid product ID, so the API returns a JSON error response indicating that the product is not found.

# Task 7. Deploy the app to Cloud Run

You can now deploy the app to Cloud Run on Google Cloud.

1. In the activity bar main menu (Code OSS main menu), click View > Command Palette.

2. In the command palette field, type Cloud Code Deploy, and then select Cloud Code: Deploy to Cloud Run from the list.

3. To enable the Cloud Run API for your project, click Enable API.

4. On the Service Settings page, for Region, select us-central1.

5. Leave the remaining settings as their defaults, and then click Deploy.

Cloud Code builds your image, pushes it to the registry, and deploys your service to Cloud Run. This may take a few minutes.

> Note: To see the detailed logs for the deployment, click Show Detailed Logs.

6. To view your running service, open the URL that is displayed in the Deploy to Cloud Run dialog.

7. Test your service by appending the /inventory, and /inventory/{productID} paths to the URL, and verify the response.

> Note: For the product URL, use the same product ID you used before. The end of the URL should resemble /inventory/12345.

8. To get the URL for the Cloud Run service inventory page, in Cloud Shell, run the following command:

```bash
export SVC_URL=$(gcloud run services describe hello-world \
  --project qwiklabs-gcp-00-c7eaf2bb4a1c \
  --region us-central1 \
  --platform managed \
  --format='value(status.url)')
echo ${SVC_URL}/inventory
``` 

<hr>

# Congratulations!
In this lab you learned how to:

* Explore various Google services that you can use to deploy an app by asking Gemini context-based questions.
* Prompt Gemini to provide templates that you can use to develop a basic app in Cloud Run.
* Create, explore, and modify the app by using Gemini to explain and generate the code.
* Run and test the app locally, and then deploy it to Google Cloud by using Gemini to generate the steps.