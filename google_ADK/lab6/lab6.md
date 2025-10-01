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

3. In the left pane, select Environment settings.

4. In Storage settings > Persistent disk settings, specify the following values:

5. Click Create.

6. Click Refresh.

7. Check the Status of the configuration being created. If the status of the configuration is Reconciling or Updating, periodically refresh and wait until the status becomes Ready before moving to the next step.

## Create a workstation
1. In the Navigation pane, click Workstations, and then click Create Workstation.

2. Specify the following values:


add image here and above too

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

> # add image here

<hr>